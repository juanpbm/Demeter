#!/usr/bin/env python3

import numpy as np
import rospy 
import cv2
from matplotlib import pyplot as plt
from vision.msg import image_Pair 
from kinematics.msg import data_3D


#Stereo Vision calculations
def stereo(images):

    base_Line = 232
    focal_Length = 18
    print('got it')
    
    #decompress the images
    array = np.frombuffer(images.left_Img.data, np.uint8)
    imgL = cv2.imdecode(array,cv2.IMREAD_COLOR)
    imgL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)

    array = np.frombuffer(images.right_Img.data, np.uint8)
    imgR = cv2.imdecode(array, cv2.IMREAD_COLOR)
    imgR = cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)
    
    #tuples to array 
    center = np.asarray(images.center, dtype = np.intc)
    top = np.asarray(images.top, dtype = np.intc)
    bottom = np.asarray(images.bottom, dtype= np.intc)

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
     
    disparity = stereo.compute(imgL,imgR).astype(np.float32) / 16
    h, w = imgL.shape[:2]
    Q = np.float32([[1, 0, 0, -0.5*w],
                   [0, -1, 0, 0.5*h],
                   [0, 0, 0, focal_Length*w],
                   [0, 0, 1, 0]])
    points = cv2.reprojectImageTo3D(disparity, Q)
    #msg init 
    point_Data = data_3D()

    #center Calculation 
    point_Data.center.z = (base_Line * focal_Length) / disparity[center[0], center[1]]
    point_Data.center.x = (point_Data.center.z * center[0]) / focal_Length
    point_Data.center.y = (point_Data.center.z * center[1]) / focal_Length
    
    #top 
    point_Data.top.z = (base_Line * focal_Length) / disparity[top[0], top[1]]
    point_Data.top.x = (point_Data.top.z * top[0]) / focal_Length
    point_Data.top.y = (point_Data.top.z * top[1]) / focal_Length
    
    #bottom 
    point_Data.bottom.z = (base_Line * focal_Length) / disparity[bottom[0], bottom[1]]
    point_Data.bottom.x = (point_Data.bottom.z * bottom[0]) / focal_Length
    point_Data.bottom.y = (point_Data.bottom.z * bottom[1]) / focal_Length
    

    print(point_Data.center)
    print(points[center[0], center[1]])
    #plt.imshow(disparity,'gray')
    #plt.show() 
    
    pub.publish(point_Data)

if __name__ == '__main__':
    try:   

        rospy.init_node('Stereo_Vision', anonymous=True)
        pub = rospy.Publisher('Kinematics_Data', data_3D, queue_size=10)
        r = rospy.Rate(10)
        rospy.Subscriber('Rec_Image',image_Pair,stereo)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
