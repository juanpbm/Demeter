#!/usr/bin/env python

import rospy
import actionlib

import kinova_msgs.msg
import vision.msg
from vision.srv import Action
from vision.srv import Reposition
import std_msgs.msg
import geometry_msgs.msg
from math import sqrt

from tf.transformations import *

import moveit_commander
import moveit_msgs.msg 

from scipy import signal
import numpy as np

'''
Globals, could be passed as arguments. Not implemented because this is designed for a specific arm
'''
finger_maxTurn = 6800   #closed
finger_minTurn = 0      #all the way open
prefix = "j2n6s300"

#should be added as and argument displacementThreshold for 
#how much displacement from spot is considered there

'''
Creates Quaternion from Euler angles
'''
def EulerXYZ2Quaternion(EulerXYZ_):
    tx_, ty_, tz_ = EulerXYZ_[0:3]
    sx = math.sin(0.5 * tx_)
    cx = math.cos(0.5 * tx_)
    sy = math.sin(0.5 * ty_)
    cy = math.cos(0.5 * ty_)
    sz = math.sin(0.5 * tz_)
    cz = math.cos(0.5 * tz_)

    qx_ = sx * cy * cz + cx * sy * sz
    qy_ = -sx * cy * sz + cx * sy * cz
    qz_ = sx * sy * cz + cx * cy * sz
    qw_ = -sx * sy * sz + cx * cy * cz

    Q_ = [qx_, qy_, qz_, qw_]
    return Q_
    

class jacoDriver():

    '''
    Initalize the ros conponents
    '''
    def __init__(self):

        print 'Initializing'

        #helper variables
        self.bstop = False
        self.bgripper = False
        self.btoBasket = False
        self.btoCut = False
        self.bharvest = False
        self.bbyCamera = False
        self.bbyScan = True
        self.bupdateXYZ = False
        self.depth = 0.3
        self.finger_turn = 0
        self.goalLocation = [0,0,0]
        self.basketLocation = [0.28455504179,-0.630760550499,0.219844207168]
        self.currentLocation = [0,0,0]
        self.currentRPY = [1.45472896099,1.25785517693,0.216061984897]
        self.basketRPY = [1.29518580437,-0.0317357964814,0.23147310019]
        self.lastCutLocation = [0,0,0]
        self.scanEndpoints = []
        self.scan = [[0.35, -0.55, 0.4],[0.35, -0.55, 0],[0.35, -0.35, 0],[0.35, -0.35, 0.4],[0.35, 0.1, 0.4],[0.35, 0.1, 0]]
        for i in range(0,len(self.scan)-1):
            if self.scan[i][2] != self.scan[i+1][2]:
                for j in np.linspace(self.scan[i][2],self.scan[i+1][2],10):
                    self.scanEndpoints.append([self.scan[i][0],self.scan[i][1],round(j,2)])
            else:
                for j in np.linspace(self.scan[i][1],self.scan[i+1][1],10):
                    self.scanEndpoints.append([self.scan[i][0],round(j,2),self.scan[i][2]])
        self.scanEndpoints.insert(0,self.scan[0])
        self.scanLocation = 0
        self.thresholdDisplacement = .05
        self.topic_address = '/' + prefix + '_driver/out/cartesian_command'

        #action clients
        print'making action client'
        #arm client not needed since using MoveIt
        #self.driverClient = actionlib.SimpleActionClient('/' + prefix + '_driver/pose_action/tool_pose', kinova_msgs.msg.ArmPoseAction)
        self.fingerClient = actionlib.SimpleActionClient('/' + prefix + '_driver/fingers_action/finger_positions', kinova_msgs.msg.SetFingersPositionAction)

        #services
        print'making services'
        self.repositionService = rospy.Service('reposition', vision.srv.Reposition, self.handle_reposition)
        self.harvestService = rospy.Service('harvest', vision.srv.Reposition, self.handle_harvest)

        #get into starting location, self.scanLocation will be 1 once that happens
        while self.scanLocation == 0:
            self.send_move_command()

        #create stop serivce which the recongition node is waiting for. this allows for node sycronization
        self.stopService = rospy.Service('stop', vision.srv.Action, self.handle_stop)
        rospy.wait_for_service('start')
        
        #clients
        print'making clients'
        self.startClient = rospy.ServiceProxy('start', vision.srv.Action)

        #test locations moves arm back and forth with action client. used in early testing
        #self.test_locations()
        
        rospy.sleep(3)

        while 1:
            self.send_move_command()

    '''
    Stores the current location of the arm as our current location used when bootup
    '''
    def setcurrentCartesianCommand(self, feedback):

        currentCartesianCommand_str_list = str(feedback).split("\n")

        for index in range(0,3):
            temp_str=currentCartesianCommand_str_list[index].split(": ")
            self.currentLocation[index] = float(temp_str[1])

        if (self.bupdateXYZ):
            self.bupdateXYZ = False
            i = 0
            for index2 in range(3,6):
                temp_str=currentCartesianCommand_str_list[index2].split(": ")
                self.currentRPY[i] = float(temp_str[1])
                i += 1

    '''
    Compares a to b and returns 1 if they are within a certain distance from each other
    '''
    def atLocation(self, a, b):
        displacement = sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - b[2])**2)
        if (displacement < self.thresholdDisplacement):
            return True
        else:
            return False

    '''
    Stores the location that the computer vision says we want to move to and
    changes booleans to move by camera
    '''
    def handle_reposition(self, req):
        print 'handle repostion'
        self.bbyCamera = True
        self.bbyScan = False
        self.bstop = False
        self.goalLocation[0] = req.Location.x
        self.goalLocation[1] = req.Location.y
        self.goalLocation[2] = req.Location.z
        return vision.srv.RepositionResponse(True)

    '''
    Sets internal value for stopping motion, and returns our current location
    '''
    def handle_stop(self, req):
        print 'handle stop'
        self.bstop = req.Action
        print self.bstop
        if self.bstop == False:
            self.bbyScan = True
            self.bbyCamera = False
        location = geometry_msgs.msg.Point(x = self.currentLocation[0], y = self.currentLocation[1], z = self.currentLocation[2])
        return vision.srv.ActionResponse(True, location)

    '''
    Sets boolean so we move to pepper then cut the pepper
    '''
    def handle_harvest(self, req):
        print'harvest'
        self.bharvest = True
        self.bbyCamera = True
        self.bbyScan = False
        self.depth = self.currentLocation[0]
        self.finger_turn = finger_maxTurn
        self.goalLocation[0] = req.Location.x
        self.goalLocation[1] = req.Location.y
        self.goalLocation[2] = req.Location.z
        self.lastCutLocation = self.currentLocation
        return vision.srv.RepositionResponse(True)

    '''
    Hold postion
    '''
    def move_nowhere(self):
        
        #get new currentLocation
        rospy.Subscriber(self.topic_address, kinova_msgs.msg.KinovaPose, self.setcurrentCartesianCommand)
        rospy.wait_for_message(self.topic_address, kinova_msgs.msg.KinovaPose)
        return self.currentLocation

    '''
    Move to the basket or place to put the peper when it has been cut
    '''
    def move_to_basket(self):

        print 'move to basket'
        #get new currentLocation
        rospy.Subscriber(self.topic_address, kinova_msgs.msg.KinovaPose, self.setcurrentCartesianCommand)
        rospy.wait_for_message(self.topic_address, kinova_msgs.msg.KinovaPose)
        
        #if at basket move set gripper to open
        if self.atLocation(self.basketLocation, self.currentLocation):
            self.bgripper = True
            return self.currentLocation
        else:
            return self.basketLocation

    '''
    Move to where the peper was picked to restart the recognition system
    '''
    def move_to_last_position(self):

        print 'move to last cut location'
        #get new currentLocation
        rospy.Subscriber(self.topic_address, kinova_msgs.msg.KinovaPose, self.setcurrentCartesianCommand)
        rospy.wait_for_message(self.topic_address, kinova_msgs.msg.KinovaPose)

        #if at location switch to by camera for more peppers
        #recognition is currently manually reset. with and action client/server it wouldnt need to be
        if self.atLocation(self.lastCutLocation, self.currentLocation):
            self.btoCut = False
            self.bbyCamera = True
            return self.currentLocation
        else: 
            return self.lastCutLocation

    '''
    Move based on values coming from reposition service, and harvest service
    '''
    def move_by_camera(self):
        
        print 'move by camera'
        #get new currentLocation
        rospy.Subscriber(self.topic_address, kinova_msgs.msg.KinovaPose, self.setcurrentCartesianCommand)
        rospy.wait_for_message(self.topic_address, kinova_msgs.msg.KinovaPose)

        if self.bharvest:
            if self.atLocation(self.goalLocation,self.currentLocation):
                self.bgripper = True
                self.bharvest = False
            if abs(self.currentLocation[2] - self.goalLocation[2]) < .1 and abs(self.currentLocation[1]-self.goalLocation[1] < .1):
                return self.goalLocation
            else:
                return [self.depth,self.goalLocation[1],self.goalLocation[2]]
        return self.goalLocation

    '''
    Move to scan the plant for peppers
    '''
    def move_by_scan(self):
        
        print 'move by scan'
        #get new currentLocation
        rospy.Subscriber(self.topic_address, kinova_msgs.msg.KinovaPose, self.setcurrentCartesianCommand)
        rospy.wait_for_message(self.topic_address, kinova_msgs.msg.KinovaPose)
        
        #check if we reached end point
        if self.atLocation(self.currentLocation, self.scanEndpoints[self.scanLocation]):
            self.scanLocation = self.scanLocation + 1
            print 'next location'
            if (self.scanLocation == len(self.scanEndpoints)):
                #finished, end programing undefined what to do at the moment
                print'Finished running all peppers picked'
            print self.scanLocation
        return self.scanEndpoints[self.scanLocation]

    '''
    Chooses the correct method for moving
    '''
    moveMethod = {  0:move_nowhere,
                    1:move_to_basket,
                    2:move_to_last_position,
                    3:move_by_camera,
                    4:move_by_scan
    }

    '''
    Uses internal variables to choose the correct move algorithm
    '''
    def send_move_command(self):

        #We want orientation to always be the same
        bMove = False
        #stopped
        if self.bstop:
            rospy.sleep(1)
            bMove = False
        #move to basket
        elif self.btoBasket:
            position = self.moveMethod[1](self)
            bMove = True
        #move to last cut location
        elif self.btoCut:
            position = self.moveMethod[2](self)
            bMove = True
        #move by camera
        elif self.bbyCamera:
            position = self.moveMethod[3](self)
            bMove = True
        #move by scan
        elif self.bbyScan:
            position = self.moveMethod[4](self)
            bMove = True

        if bMove:
            print position 
            if self.bgripper:
                #make new message
                goal = kinova_msgs.msg.SetFingersPositionGoal()
                goal.fingers.finger1 = self.finger_turn
                goal.fingers.finger2 = goal.fingers.finger1
                goal.fingers.finger3 = goal.fingers.finger1 
                print goal

                #send through client
                self.fingerClient.send_goal(goal)
                print "Attention: moving the gripper"
                if self.fingerClient.wait_for_result(rospy.Duration(5.0)):
                    print 'Success'
                else:
                    self.fingerClient.cancel_all_goals()
                    print' Error: the cartesian action timed-out'
    
                self.bgripper = False
                if self.finger_turn == finger_minTurn:
                    #if we just opened fingers return to last cut location
                    self.btoBasket = False
                    self.btoCut = True
                    self.finger_turn = finger_maxTurn
                else:
                    #if we just closed to fngers move to basket
                    self.finger_turn = finger_minTurn
                    self.btoBasket = True


            else:
                #basket has a different orientation
                orientation = EulerXYZ2Quaternion(self.currentRPY)
                if self.btoBasket:
                    orientation = EulerXYZ2Quaternion(self.basketRPY)
                
                #send with Moveit using location gotten above to move to the new location
                goal = geometry_msgs.msg.Pose()
                goal.position = geometry_msgs.msg.Point(
                    x=position[0], y=position[1], z=position[2])
                goal.orientation = geometry_msgs.msg.Quaternion(
                    x=orientation[0], y=orientation[1], z=orientation[2], w=orientation[3])

                # Moveit
                robot = moveit_commander.RobotCommander()
                group = moveit_commander.MoveGroupCommander("arm")
                planning_scene_interface = moveit_commander.PlanningSceneInterface()  

                # Planning to a Pose goal
                group.set_pose_target(goal)

                # Now, we call the planner to compute the plan and visualize it.
                group.plan()
                # we should add something hear to handle failures 
                
                # move the robot 
                print "Attention: moving the arm"
                group.go()

    '''
    Used for early testing, moves to a location, back and there again
    '''
    def test_locations(self):
        #get current location
        topic_address = '/' + prefix + '_driver/out/cartesian_command'
        rospy.Subscriber(topic_address, kinova_msgs.msg.KinovaPose, self.setcurrentCartesianCommand)
        rospy.wait_for_message(topic_address, kinova_msgs.msg.KinovaPose)
        print 'position listener obtained message for Cartesian pose. '

        #move 10cm +z
        action_address = '/' + prefix + '_driver/pose_action/tool_pose'
        client = actionlib.SimpleActionClient(action_address, kinova_msgs.msg.ArmPoseAction)
        client.wait_for_server()
        print 'move 10cm +z'
        goal = kinova_msgs.msg.ArmPoseGoal()
        goal.pose.header = std_msgs.msg.Header(frame_id=(prefix + '_link_base'))
        #goal.pose.pose.position = geometry_msgs.msg.Point(
        #    x=self.currentLocation[0], y=self.currentLocation[1], z=(self.currentLocation[2]))
        goal.pose.pose.position = geometry_msgs.msg.Point(x=0.3, y=0.3, z=0.4)
        goal.pose.pose.orientation = geometry_msgs.msg.Quaternion(x=0, y=0, z=0, w=1.0)

        client.send_goal(goal)

        if client.wait_for_result(rospy.Duration(20.0)):
            print 'Success'
        else:
            client.cancel_all_goals()
            print' Error: the cartesian action timed-out'

        #move to position A
        goal = kinova_msgs.msg.ArmPoseGoal()
        goal.pose.header = std_msgs.msg.Header(frame_id=(prefix + '_link_base'))
        goal.pose.pose.position = geometry_msgs.msg.Point(x=0.2, y=-0.1, z=0.3)
        goal.pose.pose.orientation = geometry_msgs.msg.Quaternion(x=0, y=0, z=0, w=1.0)

        client.send_goal(goal)

        if client.wait_for_result(rospy.Duration(20.0)):
            print 'Success'
        else:
            client.cancel_all_goals()
            print' Error: the cartesian action timed-out'

        #move back
        goal = kinova_msgs.msg.ArmPoseGoal()
        goal.pose.header = std_msgs.msg.Header(frame_id=(prefix + '_link_base'))
        goal.pose.pose.position = geometry_msgs.msg.Point(x=0.3, y=0.3, z=0.4)
        goal.pose.pose.orientation = geometry_msgs.msg.Quaternion(x=0, y=0, z=0, w=1.0)

        client.send_goal(goal)

        if client.wait_for_result(rospy.Duration(20.0)):
            print 'Success'
        else:
            client.cancel_all_goals()
            print' Error: the cartesian action timed-out'


if __name__ == '__main__':
    print 'start'
    rospy.init_node('jacoDriver')

    try:
        jaco = jacoDriver()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass