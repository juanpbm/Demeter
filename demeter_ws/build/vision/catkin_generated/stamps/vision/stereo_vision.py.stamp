#!/usr/bin/env python3

import numpy as np
import rospy 
import cv2
from matplotlib import pyplot as plt
from vision.msg import image_Pair 

#Stereo Vision calculations
def stereo(images):

    base_Line = 232
    focal_Length = 18
    print('got it')
    
    array = np.frombuffer(images.left_Img.data, np.uint8)
    imgL = cv2.imdecode(array,cv2.IMREAD_COLOR)
    imgL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)

    array = np.frombuffer(images.right_Img.data, np.uint8)
    imgR = cv2.imdecode(array, cv2.IMREAD_COLOR)
    imgR = cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)

    center = np.asarray(images.center, dtype = np.intc)

    """
    #show the iamges 
    plt.imshow(imgL,"gray")
    plt.show()
    
    plt.imshow(imgR,"gray")
    plt.show()
    """
    #Disparity map calculation 
    stereo = cv2.StereoSGBM_create(minDisparity = 16,
                                numDisparities=64, 
                                blockSize=16) 
    #is it necesary to compute the map? whats the num of disp and size 
    disparity = stereo.compute(imgL,imgR).astype(np.float32) / 16
    #h, w = imgL.shape[:2]
    #Q = np.float32([[1, 0, 0, -0.5*w],
     #           [0, -1, 0, 0.5*h],
      #          [0, 0, 0, focal_Length],
       #         [0, 0, 1, 0]])
    #points = cv2.reprojectImageTo3D(disparity, Q)

    #Depth Calculation 
    center_Depth = (base_Line * focal_Length) / disparity[center[0], center[1]]
    print(type(disparity))

    print(center)
    print("Z = ", center_Depth)

    #Position Calculation 
    x = (center_Depth*images.center[0])/focal_Length
    y = (center_Depth*images.center[1])/focal_Length

    print("X = ", x)
    print("Y = ", y)

    plt.imshow(disparity,'gray')
    plt.show()

#ROS subscribing to Rec_image 
def subscriber ():
    rospy.init_node('Stereo_Vision', anonymous=True)
    rospy.Subscriber('Rec_Image',image_Pair,stereo)
    rospy.spin()


#TODO ROS publishing of 3D_Data

if __name__ == '__main__':
    subscriber()
