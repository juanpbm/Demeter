#!/usr/bin/env python

import rospy
import actionlib

import kinova_msgs.msg
#from vision import vision.msg
import vision.msg
from vision.srv import Action
from vision.srv import Reposition
import std_msgs.msg
import geometry_msgs.msg
from math import sqrt

from tf.transformations import *

import moveit_commander
import moveit_msgs.msg 

'''
Globals, could be passed as arguments. Not implemented because this is designed for a specific arm
'''
finger_maxDist = 18.9/2/1000  # max distance for one finger
finger_maxTurn = 6800  # max thread rotation for one finger
robot_category = 'j'
robot_category_version = 2
wrist_type = 'n'
arm_joint_number = 6
robot_mode = 's'
finger_number = 3
prefix = "j2n6s300"

#arguments i want, thresholdDisplacement, 

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
        self.finger_turn = 0
        self.goalLocation = [0,0,0]
        self.basketLocation = [0,0,1]
        self.currentLocation = [0,0,0]
        self.lastCutLocation = [0,0,0]
        self.scanEndpoints = [[0.5, -0.6, 0.6],[0.5, -0.6, 0.1],[0.5, -0.35, 0.1],[0.5, -0.35, 0.6],[0.5, 0.35, 0.6],[0.5, 0.35, 0.1]]
        self.orientationRPY = [[2.58831644058, 1.38926029205, -1.23999965191],[-2.99477958679,1.39808034897, -1.22968423367],[-2.14679527283, 1.4113227129, -1.24613773823],[2.6834628582,1.38840186596,-1.20909225941],[-0.882254958153, 1.43556320667,-1.47972130775],[ -2.29393768311,1.43471097946, -1.11946737766]]
        self.scanLocation = 0
        self.thresholdDisplacement = .08

        #action clients
        print'making action client'
        self.driverClient = actionlib.SimpleActionClient('/' + prefix + '_driver/pose_action/tool_pose', kinova_msgs.msg.ArmPoseAction)
        self.fingerClient = actionlib.SimpleActionClient('/' + prefix + '_driver/pose_action/tool_pose', kinova_msgs.msg.SetFingersPositionAction)

        #services
        print'making services'
        self.stopService = rospy.Service('stop', vision.srv.Action, self.handle_stop)
        self.repositionService = rospy.Service('reposition', vision.srv.Reposition, self.handle_reposition)
        self.harvestService = rospy.Service('harvest', vision.srv.Reposition, self.handle_harvest)

        rospy.wait_for_service('start')
        #clients
        print'making clients'
        self.startClient = rospy.ServiceProxy('start', vision.srv.Action)

        #test locations, wont be in final code
        #self.test_locations()
        
    
        while 1:
            self.send_move_command()
            # rospy.sleep(1)

    '''
    Stores the current location of the arm as our current location used when bootup
    '''
    def setcurrentCartesianCommand(self, feedback):

        currentCartesianCommand_str_list = str(feedback).split("\n")

        for index in range(0,3):
            temp_str=currentCartesianCommand_str_list[index].split(": ")
            self.currentLocation[index] = float(temp_str[1])

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
    Sets internal value for stopping motion
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
    Sets boolean so we cut the pepper
    '''
    def handle_harvest(self, req):
        self.bharvest = True
        self.bbyCamera = True
        self.bbyScan = False
        self.finger_turn = 0
        self.goalLocation[0] = req.Location.x
        self.goalLocation[1] = req.Location.y
        self.goalLocation[2] = req.Location.z
        self.lastCutLocation = self.goalLocation
        return vision.srv.RepositionResponse(True)

    '''
    Hold postion
    '''
    def move_nowhere(self):
        return self.currentLocation

    '''
    Move to the basket or place to put the peper when it has been cut
    '''
    def move_to_basket(self):
        print 'move to basket'
        #if at basket switch to stop and send client to drop pepper off
        if self.atLocation(self.basketLocation, self.currentLocation):
            self.bgripper = True
            return self.currentLocation
        else:
            return self.basketLocation

    '''
    Move to where the peper was picked to restart the CV
    '''
    def move_to_last_position(self):
        print 'move to last cut location'
        #if at location switch stop and send client to restart cv
        if self.atLocation(self.lastCutLocation, self.currentLocation):
            self.btoCut = False
            self.bbyCamera = True
            return self.currentLocation
        else: 
            return self.lastCutLocation

    '''
    Move based on values coming from xyz ActionServer
    '''
    def move_by_camera(self):
        print 'move by camera'
        if self.bharvest:
            if self.atLocation(self.goalLocation,self.currentLocation):
                self.bgripper = True
        return self.goalLocation

    '''
    Move to scan the plant for peppers
    '''
    def move_by_scan(self):
        #check if we reached end point
        print 'move by scan'
        topic_address = '/' + prefix + '_driver/out/cartesian_command'
        rospy.Subscriber(topic_address, kinova_msgs.msg.KinovaPose, self.setcurrentCartesianCommand)
        rospy.wait_for_message(topic_address, kinova_msgs.msg.KinovaPose)
        
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

        #I think we want orientation to always be zero, need to play with control some first to see
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
                if self.fingerClient.wait_for_result(rospy.Duration(20.0)):
                    print 'Success'
                else:
                    self.fingerClient.cancel_all_goals()
                    print' Error: the cartesian action timed-out'
        
                self.bgripper = False
                if self.finger_turn == finger_maxTurn:
                    self.btoBasket = False
                    self.btoCut = True
                    self.finger_turn = 0
                else:
                    self.finger_turn = finger_maxTurn
                    self.btoBasket = True


            else:
                print position
                #position = [0.451476633549,0.318827390671,0.655069053173]
                orientation = quaternion_from_euler(self.orientationRPY[self.scanLocation][0], self.orientationRPY[self.scanLocation][1], self.orientationRPY[self.scanLocation][2])
                print orientation
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
                # if group.plan() == moveit_commander.move_group.MoveItErrorCodes.Success:
                #     success = True
                # else:
                #     success = False 
                
                # move the robot 
                print "Attention: moving the arm"
                group.go()

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