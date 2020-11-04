#!/usr/bin/env python3

import numpy as np
import rospy
from matplotlib import pyplot as plt 
from kinematics.msg import data_3D

#TODO find the angles using inv kinematics

#TODO find the size of the pepper 

#TODO publisher of the angles 


def inv_K(points_Data):
    print(points_Data)


if __name__ == '__main__':
    try: 
        rospy.init_node('Inv_Kinematics', anonymous = True)
        
        r = rospy.Rate(10)
        rospy.Subscriber('Kinematics_Data', data_3D, inv_K)
        rospy.spin()
    
    except rospy.ROSInterruptException:    
        pass
