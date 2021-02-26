#!/usr/bin/env python3

import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
from vision.msg import image_Pair
from sensor_msgs.msg import CompressedImage

import picamera
from picamera import PiCamera
import time
from datetime import datetime

class Camera_Driver_node:

    def __init__(self):
        #camera set up 
        self.filename = './scenes/photo.png'

        # Camera settimgs
        self.cam_width = 1280
        self.cam_height = 480

        # Final image capture settings
        slef.scale_ratio = 0.5

        # Camera resolution height must be dividable by 16, and width by 32
        self.cam_width = int((cam_width+31)/32)*32
        self.cam_height = int((cam_height+15)/16)*16
        print ("Used camera resolution: "+str(cam_width)+" x "+str(cam_height))

        # Buffer for captured image settings
        self.img_width = int (cam_width * scale_ratio)
        self.img_height = int (cam_height * scale_ratio)
        self.capture = np.zeros((img_height, img_width, 4), dtype=np.uint8)
        print ("Scaled image resolution: "+str(img_width)+" x "+str(img_height))

        # Initialize the camera
        self.camera = PiCamera(stereo_mode='side-by-side',stereo_decimate=False)
        self.camera.resolution=(cam_width, cam_height)
        self.camera.framerate = 20
        self.camera.hflip = True


        self.t2 = datetime.now()
        self.counter = 0
        self.avgtime = 0
    
    def video_Capture():
        #TODO capture of video and processing of frame
        for frame in camera.capture_continuous(capture, format="bgra", use_video_port=True, resize=(img_width,img_height)):
            counter+=1
            t1 = datetime.now() 
            timediff = t1-t2
            avgtime = avgtime + (timediff.total_seconds())
            cv2.imshow("pair", frame)
            key = cv2.waitKey(1) & 0xFF
            t2 = datetime.now()
                
            # if the `q` key was pressed, break from the loop and save last image    
            if key == ord("q") :
                avgtime = avgtime/counter
                print ("Average time between frames: " + str(avgtime))
                print ("Average FPS: " + str(1/avgtime))
                if (os.path.isdir("./scenes")==False):
                    os.makedirs("./scenes")
                    cv2.imwrite(filename, frame)                        
                    break

    def img_Capture():
        #TODO capture image and senf it back
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





