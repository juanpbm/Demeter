#!/usr/bin/env python3

import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
import subprocess 
import time 

from vision.msg import image_Pair
from sensor_msgs.msg import CompressedImage

class Camera_Driver_node:

    def __init__(self, out_path, res):
        self.out_path = out_path 
        self.res = res #in the from of #x#
        self.command = "sudo fswebcam -q -r " + res + " -S 15 " + out_path 

    def video_Capture(self):
        #Capture video and processing of each frame
        print("video Capture is On:") 
        self.command += "video.jpg"
        red = 0
        our_count = 0
        while not red:
            print("-")
            process = subprocess.Popen(self.command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            
            img = cv2.imread(self.out_path+"video.jpg")
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            red = self.red_Finder(img)
            
        print("Red Found in the Frame. End video capture")
        #split 
        img_L, img_R = self.split_Img(img)  
        return(img_L, img_R)

    def img_Capture(self):
        #Capture image and senf it backi
        self.command += "img.jpg"
        process = subprocess.Popen(self.command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        img = cv2.imread(self.out_path+"img.jpg")
        img_L, img_R = self.split_Img(img) 
        print("Image Capture Complete")
        return(img_L, img_R)


    def red_Finder(self, img):

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
        if np.count_nonzero(thresh_img > 0) >= (len(thresh_img)*len(thresh_img[0])*0.2):
            print('there may be peppers')
            return(True)
        else:
            #print("no red")
            return(False)   
    
    def split_Img(self,img):
    
        img_width = int(self.res.split('x')[0])//2
        img_height = int(self.res.split('x')[1])
        img_L = img[0:img_height,0:img_width] #Y+H and X+W
        img_R = img[0:img_height,img_width:img_width*2]
        return(img_L, img_R)


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
