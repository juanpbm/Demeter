#!/usr/bin/env python3

import numpy as np
import rospy
import cv2
from matplotlib import pyplot as plt 
import os 
import subprocess 
import time 

from vision.srv import * 
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
            return(True, thresh_img)
        else:
            #print("no red")
            return(False, thresh_img)   
    
    def split_Img(self,img):
    
        img_width = int(self.res.split('x')[0])//2
        img_height = int(self.res.split('x')[1])
        img_L = img[0:img_height,0:img_width] #Y+H and X+W
        img_R = img[0:img_height,img_width:img_width*2]
        return(img_L, img_R)


class Recognition:

    def __init__(self):
        rospy.init_node("Recognition", anonymous = True)

        self.camera = Camera_Driver_node("camera_out/", "640x480")
        self.stop_srv = rospy.ServiceProxy('stop', Action)
        self.reposition_srv = rospy.ServiceProxy('reposition', Reposition)
        self.harvest_srv = rospy.ServiceProxy('harvest', Reposition)
        self.s = rospy.Service('start', Action, self.start)
        print ("Recognition Node has been setup")

    def pepper_Finder(self):
        
        print("Recognition system initialized")

        while(True): 
            
            #Captrure video and split images
            img_L,_ = self.camera.video_Capture()
            print("got left img")
            
            #ask the arm to stop if it gets a false back keep asking until it stops
            while (True):
                if(self.stop_srv(True)):
                    break 
            
            #Take a new image in case the are moved
            img_L, img_R = self.camera.img_Capture();      
            
            #Find if there is enough read in the frames
            treshold, thresh_img = self.camera.red_Finder(img_L)
         
            if threshold:
                
                #TODO add amrits code here 
                
        
                #TODO return what the arm needs to reposition
                #TODO are we moving a set distance or to the center of the box
                '''
                if coord[0] < 10:
                    print ("move camera to the left")
                elif coord[1] < 10:
                    print("move camera up")
                elif coord[2] > len(img_L[0])-10:
                    print("move camera to the right")
                elif coord[3] > len(img_L)-10:
                    print("move camera down")
                else:
                    
                    #unsure if it will read the image properly
                    image = image_utils.imresize(img_L, size=(224, 224), interpolate='bilinear', channel_first=False, **kwargs)
                    image = image_utils.img_to_array(image)
                    image = np.expand_dims(image, axis=0)
                    image = preprocess_input(image)
                    preds = self.model.predict(image)
                    P = decode_predictions(preds)[0]
                    print(f"the pepper is in the picture with a prob of: {P[['bell_pepper'  in i for i in P].index(True)][2]}")
                    '''
                    #TODO stereo srv call 
            else:
                #tell the arm to go back since it moved after possible pepper was found 
                pass
      

    def box_Finder(self, img, imgt):
        
        #Find edges
        edges = cv2.Canny(imgt, 800, 50, L2gradient = True)
        #plt.imshow(edges)
        #plt.show()
    
        #which cols and rows have an edge
        rows = [1 if 255 in i else 0 for i in edges]
        cols = [1 if 255 in edges[:,i] else 0 for i in range(0, len(edges[0]))]
        
        #find the bounding box 
        top = rows.index(1)
        left = cols.index(1)
        rows.reverse()
        cols.reverse()
        right = len(cols) - cols.index(1)-1
        bottom = len(rows) - rows.index(1)-1

        coord = [left,top,right,bottom]
        cv2.rectangle(img,(left,top),(right,bottom),(0,255,0),2)
        plt.imshow(img)
        plt.show()
    
        return left, top, right, bottom, rows, cols

    def contour_Finder(self, img, coord):

        crop_img = img[coord[1]:coord[3], coord[0]:coord[2]]
        #plt.imshow(crop_img)        
        #plt.show()

        crop_img_gry = cv2.cvtColor(crop_img, cv2.COLOR_RGB2GRAY)
        ret,thresh = cv2.threshold(crop_img_gry,50,255,0)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_L1)

        threshold = (len(crop_img)*len(crop_img[0])*0.01)
        pepper_cont = [contours[i] for i in range (0,len(contours)) if (hierarchy[0,i,3] == -1 and cv2.contourArea(contours[i]) > threshold)]
        
        print(len(pepper_cont))       
        imga = cv2.drawContours(crop_img, pepper_cont, -1, (0,255,0), 3)
        plt.imshow(imga)
        plt.show()

        
        #TODO what are the return values and how to manage error 
        #IDEA return count of peppers, and contours if more than on flag them in the other function
        if len(pepper_cont) <= 0:
            return(-1,-1)
        elif len(pepper_cont) == 1:
            return(True, pepper_cont)
        else:
            #TODO what can be done if many 
            return(False, pepper_cont)

    def gen_Image_Pair(self, img_L, img_R, coords):
    
        images = image_Pair()

        images.left_Img.header.stamp = rospy.Time.now()
        images.left_Img.format = 'jpg'
        images.left_Img.data = np.array(cv2.imencode('.jpg',img_L)[1]).tostring()

        images.right_Img.header.stamp = rospy.Time.now()
        images.right_Img.format = 'jpg'
        images.right_Img.data = np.array(cv2.imencode('.jpg',img_R)[1]).tostring()
         
        images.coordinates = coords
        return(images)
    
    def start(self,req):
        return ActionResponce(True)

if __name__ == '__main__':
   
    try:
        print("Welcmoe to Demeter the Bell Pepper Harvester")
        rec_system = Recognition()
        
        print("Waiting for the arm driver to be online")
        rospy.wait_for_service('stop')
        
        print("arm driver detected")
        rec_system.pepper_Finder()
    except rospy.ROSInterruptException:
               print('!!!!!!!!!There has been an Unknown Error')
