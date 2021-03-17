#!/usr/bin/env python

import rospy
import actionlib

import kinova_msgs.msg
import arm_and_chasis_driver.msg
from arm_and_chasis_driver.srv import PepperInHand
from arm_and_chasis_driver.srv import StopMovement
import std_msgs.msg
import geometry_msgs.msg
from math import sqrt

from tf.transformations import *

import moveit_commander
#from moveit.move_group_interface import *
#from moveit.planning_scene_interface import *
import moveit_msgs.msg 

#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit_msgs/DisplayRobotState.h>
#include <moveit_msgs/DisplayTrajectory.h>
#include <moveit_msgs/AttachedCollisionObject.h>
#include <moveit_msgs/CollisionObject.h>

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
        self.btoBasket = False
        self.btoCut = False
        self.bbyCamera = False
        self.bbyScan = True
        self.goalLocation = [0,0,0]
        self.basketLocation = [0,0,0]
        self.currentLocation = [0,0,0]
        self.lastCutLocation = [0,0,0]
        self.scanEndpoints = [[0.35, -0.6, 0.6],[0.35, -0.6, 0.1],[0.35, -0.35, 0.1],[0.35, -0.35, 0.6],[0.35, 0.35, 0.6],[0.35, 0.35, 0.1]]
        self.scanLocation = 0
        self.thresholdDisplacement = .08

        #action clients
        print'making action client'
        self.driverClient = actionlib.SimpleActionClient('/' + prefix + '_driver/pose_action/tool_pose', kinova_msgs.msg.ArmPoseAction)

        #services
        print'making services'
        # self.stopService = rospy.Service('stop', arm_and_chasis_driver.srv.Action, self.handle_stop)
        # self.repositionService = rospy.Service('reposition', arm_and_chasis_driver.srv.Reposition, self.handle_stop)
        # self.harvestService = rospy.Service('harvest', arm_and_chasis_driver.srv.Reposition, self.handle_stop)

        #clients
        print'making clients'
        # self.startClient = rospy.client('start', arm_and_chasis_driver.srv.Action)

        #test locations, wont be in final code
        #self.test_locations()

        #change to call client and send start message then while. and break while once we get to end
        print'starting movement'
        while 1:
            self.send_move_command()
            # rospy.sleep(1)
        
    '''
    Stores the current location of the arm as our current location used when bootup
    '''
    def setcurrentCartesianCommand(self, feedback):

        currentCartesianCommand_str_list = str(feedback).split("\n")

        for index in range(0,2):
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
    Stores the location that the computer vision says we want to move to 
    '''
    def handle_get_location(self, req):
        self.goalLocation = req.location
        return arm_and_chasis_driver.msg.CoordinateActionResponse()

    '''
    Sets internal value for stopping motion
    '''
    def handle_stop(self, req):
        self.bstop = req.bstop
        return arm_and_chasis_driver.srv.StopMovementResponse(bstop)

    '''
    Sets boolean so we move to the basket
    '''
    def handle_pepper_in_hand(self, req):
        btoBasket = True
        return arm_and_chasis_driver.srv.PepperInHandResponse(True)

    '''
    Hold postion
    '''
    def move_nowhere(self):
        return self.currentLocation

    '''
    Move to the basket or place to put the peper when it has been cut
    '''
    def move_to_basket(self):
        #if at basket switch to stop and send client to drop pepper off
        if self.atLocation(self.basketLocation, self.currentLocation):
            self.bstop = True
            return self.currentLocation
        else:
            return self.basketLocation

    '''
    Move to where the peper was picked to restart the CV
    '''
    def move_to_last_position(self):
        #if at location switch stop and send client to restart cv
        if self.atLocation(self.lastCutLocation, self.currentLocation):
            self.bstop = True
            return self.currentLocation
        else: 
            return selflastCutLocation

    '''
    Move based on values coming from xyz ActionServer
    '''
    def move_by_camera(self):
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
        orientation = quaternion_from_euler(1.31737184525,1.1596698761,-3.04842185974)
#         ThetaX: 1.31737184525
#         ThetaY: 1.1596698761
#         ThetaZ: -3.04842185974

        bMove = False
        #stopped
        if self.bstop:
            position = self.moveMethod[0](self)
            bMove = True
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
            #send in client using location gotten above to move to the new location
            bMove = False
            #goal = kinova_msgs.msg.ArmPoseGoal()
            #goal.pose.header = std_msgs.msg.Header(frame_id=(prefix + '_link_base'))
            #goal.pose.pose.position = geometry_msgs.msg.Point(
            #    x=position[0], y=position[1], z=position[2])
            #goal.pose.pose.orientation = geometry_msgs.msg.Quaternion(
            #    x=orientation[0], y=orientation[1], z=orientation[2], w=orientation[3])
            goal = geometry_msgs.msg.Pose()
            goal.position = geometry_msgs.msg.Point(
                x=position[0], y=position[1], z=position[2])
            goal.orientation = geometry_msgs.msg.Quaternion(
                x=orientation[0], y=orientation[1], z=orientation[2], w=orientation[3])

            # Moveit
            robot = moveit_commander.RobotCommander()

            group = moveit_commander.MoveGroupCommander("arm")

            #gripper_group = moveit.planning_interface.MoveGroupInterface("gripper")
            
            planning_scene_interface = moveit_commander.PlanningSceneInterface()  

            # Create a publisher for visualizing plans in Rviz.
            #display_trajectory = moveit_msgs.DisplayTrajectory 

            # Planning to a Pose goal
            group.set_pose_target(goal)

            # Now, we call the planner to compute the plan and visualize it.
            #my_plan = moveit_commander.MoveGroupCommander.plan 

            group.plan()
            # if group.plan() == moveit_commander.move_group.MoveItErrorCodes.Success:
            #     success = True
            # else:
            #     success = False 
            #ROS_INFO("Visualizing plan (pose goal) %s",success)  
            
            # move the robot 
            print "Attention: moving the arm"
            # gripper_action(0.0); // open the gripper
            group.go()
            # self.driverClient.wait_for_server()
            # self.driverClient.send_goal(goal)

            # if self.driverClient.wait_for_result(rospy.Duration(10.0)):
            #     return self.driverClient.get_result()
            # else:
            #     self.driverClient.cancel_all_goals()
            #     print 'the cartesian action timed-out'
            #     return None

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
    rospy.init_node('jacoDriver')
    
    try:
        jaco = jacoDriver()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass