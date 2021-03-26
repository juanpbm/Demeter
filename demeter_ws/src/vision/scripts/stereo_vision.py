#!/usr/bin/env python3

import numpy as np
import rospy 
import cv2
from matplotlib import pyplot as plt
from vision.msg import image_Pair 
from kinematics.msg import data_3D
from mpl_toolkits.mplot3d import Axes3D

#Stereo Vision calculations
def stereo(img_L, img_R, coord):

    base_Line = 232
    focal_Length = 18
    
    #Disparity map calculation 
    stereo = cv2.StereoSGBM_create(minDisparity = 16,
                                   numDisparities=64, 
                                   blockSize=16) 
     
    disparity = stereo.compute(img_L,img_R).astype(np.float32) / 16
    h, w = imgL.shape[:2]
    Q = np.float32([[1, 0, 0, -0.5*w],
                   [0, -1, 0, 0.5*h],
                   [0, 0, 0, focal_Length],
                   [0, 0, 1, 0]])
    
    points = cv2.reprojectImageTo3D(disparity, Q)
