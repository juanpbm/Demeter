#!/usr/bin/env python3

import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
from vision.msg import image_Pair
from sensor_msgs.msg import CompressedImage

class Camera_Driver_node:

    def __init__(self):
        #TODO msg or service ?
    
    def capture():
        #TODO capture of video and processing of frame
        pass

    def red_Finder(img):

        #Bluring 
        kernel = np.ones((5,5),np.float32)/25
        img_blured = cv2.filter2D(img,-1,kernel)
        img_blured = cv2.cvtColor(img_blured, cv2.COLOR_RGB2HSV)                                            
        
        #Thresholding
        mask_lower = cv2.inRange(img_blured,(0,120,70),(10,255,255))      
        mask_upper = cv2.inRange(img_blured,(165,120,70),(180,250,250))
        mask = mask_lower + mask_upper
        
        thresh_img = cv2.bitwise_and(img_blured, img_blured, mask=mask)
        thresh_img = cv2.cvtColor(thresh_img, cv2.COLOR_HSV2RGB)        
        #plt.imshow(result)    
        #plt.show()
        return(thresh_img)   
    

    def gen_Image_Pair(img_L, img_R, coords):
                
        images = image_Pair()

        images.left_Img.header.stamp = rospy.Time.now()
        images.left_Img.format = 'jpg'
        images.left_Img.data = np.array(cv2.imencode('.jpg',img_L)[1]).tostring()

        images.right_Img.header.stamp = rospy.Time.now()
        images.right_Img.format = 'jpg'
        images.right_Img.data = np.array(cv2.imencode('.jpg',img_R)[1]).tostring()
            
        images.coordinates = coords            
        return(images)

if __name__ == "__main__":





