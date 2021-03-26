#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:37:47 2021

@author: amieramie
"""

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
                #!!!!!TODO: wrong syntax here - implement how to actually get the initial coordinates from the arm!!!!!
                X_coord, Y_coord = coordinatesFromArm
                contour_BB, cutoff_pepper,BB_size = self.find_BoundingBox(img_L)
                for contour_index in range(0,len(contour_BB)):
                    print(f'Contour {contour_index}:')
                    #bounding box dimensions based on pixels within frame [left, top, right bottom]
                    boundingBox = np.array(contour_BB[contour_index])
                    cutoff = cutoff_pepper[contour_index]
                    size = BB_size[contour_index]   
                    #if the contour around the red object is deemed as cutoff or if it is > than a certain sizxe then we will
                    #treat the contoured object as a pepper and navigate toward it. If not we will ignore the contoured object
                    if ((len(boundingBox)>0)&((size>750)|(sum(cutoff)>0))):
                        #increasing the bounding box size to help navigate towards the right contour
                        correctBoundingBox = boundingBox + [-11,-11,11,11]
                        initialCutoffs = np.array(cutoff)
                        print(initialCutoffs)
                        attempt = 0
                        stop = False
                        fullPepperFound = False
                        movements = np.array([0,0,0,0])
                        while(((sum(movements!=0)>=1)|(attempt == 0))&((stop == False)&(fullPepperFound==False))):
                            movements = np.array([0,0,0,0])
                            attempt+=1
                            print(f'Attempt {attempt}:')
                            #we may need to change the movement magnitudes depending on the coordinates coming from the arm
                            if cutoff[0] ==True:
                                print('left')
                                movements[0] = -10
                                movements[2] = -10
                            if  cutoff[1] == True:
                                print('top')
                                movements[1] = -10
                                movements[3] = -10
                            if cutoff[2] == True:
                                print('right')
                                movements[2] = 10
                                movements[0] = 10
                            if  cutoff[3] == True:
                                print('bottom')
                                movements[3] = 10
                                movements[1] = 10
                            if ((movements[0]!=0) &(movements[2]!=0))|((movements[1]!=0) &(movements[3]!=0)):
                                #TODO: implement a way to zoom out -> move camera back on z axis, and feedback for getting new movement coordinates
                                print('Zoom out')
                            else:
                                #!!!!TODO: implement how this will actually feedback to the coordinates the arm is tracking
                                X_coord+=(movements[0]+movements[2])
                                Y_coord+=(movements[1]+movements[3])
                            if attempt>5:
                                #!!!!!TODO: might be worth it to implement a zoom out system here as well since
                                #if the attempts reach 6 it likely means that the magnitude is too large and we keep over correcting in each
                                #direction
                                stop = True
                            else:
                                #attempting to reposition arm based on coordinates take another image and go through the
                                #process again
                                #!!!!!TODO: Syntax might be wrong here for commincation with the arm and camera
                                #change if wrong
                                self.reposition_srv([X_coord,Y_coord])
                                img_L,_ = self.camera.video_Capture()
                                print("got left img")
                                #Take a new image in case the are moved
                                img_L, img_R = self.camera.img_Capture()
                                
                                
                                contours, cutoffs, BB_sizes = find_BoundingBox(imgL)
                                for contour_index in range(0,len(contours)):
                                    if np.array_equal((np.array(contours[contour_index])<correctBoundingBox),np.array([False,False,True,True])):
                                        mainContour = contour_index
                                cutoff = np.array(cutoffs[mainContour])
                                correctBoundingBox = np.array(contours) + [-11,-11,11,11]
                                fullPepperFound = (sum(cutoff)==0)
                        if fullPepperFound:
                            print(f'Full Pepper Found Here is the Bounding Box: {np.array(contours[mainContour])+[-5,-5,5,5]}')
                            coordinates_of_BB = np.array(contours[mainContour])
                            #!!!!TODO: implement send_toMLModel function and check if this is extracting the right bounding box
                            send_toMLModel(imgL[coordinates_of_BB[0]:coordinates_of_BB[2],coordinates_of_BB[1]:coordinates_of_BB[3]])
                        else:
                            print('Full Pepper was unable to be found from this starting frame')
                    else:
                        print('Contour was not recognized as a pepper')
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
        right = len(cols) - 1 - cols[::-1].index(1)
        bottom = len(rows) - 1 - rows[::-1].index(1)

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
        
#        print(len(pepper_cont))       
#        imga = cv2.drawContours(crop_img, pepper_cont, -1, (0,255,0), 3)
#        plt.imshow(imga)
#        plt.show()

        
        #TODO what are the return values and how to manage error 
        #IDEA return count of peppers, and contours if more than on flag them in the other function
        if len(pepper_cont) <= 0:
            return pepper_cont
        elif len(pepper_cont) == 1:
            return pepper_cont
        else:
            #TODO what can be done if many 
            return pepper_cont, contours
        
    def find_BoundingBox(self, imgSection):
        stop = False
        contour_BB = []
        BB_size = []
        cutoff_pepper = []
        try:
            treshold, imgt = self.camera.red_Finder(imgSection)
        except:
            stop = True
        #Find contours
        if not(stop):
            pepper_cont = self.contour_Finder(imgt, [0,0,imgt.shape[1],imgt.shape[0]])
            try:
                if len(pepper_cont) == 0:
                    stop = True
            except:
                print('Contours found')

        if not(stop):
            #depending on the number of contours found the data structure of the output of the contour function wil be different
            if isinstance(pepper_cont,tuple):
                pepper_cont_temp = pepper_cont[0]
            else:
                pepper_cont_temp = pepper_cont

            for contour in pepper_cont_temp:
                #print(contour.shape)
                contour = contour.transpose(1,0,2)[0]
                left = min(contour[:,0])
                right = max(contour[:,0])
                bottom = max(contour[:,1])
                top = min(contour[:,1])
                bb_coord = [left,top,right,bottom]
                #gives the actual bounding box of the contoured red object
                contour_BB.append(bb_coord)
                #help determine the bounding box size of the contoured red object
                BB_size.append(abs((bb_coord[2] - bb_coord[0])*(bb_coord[3]-bb_coord[1])))
                #helps check whether a contoured pepper is cutoff or fully in frame
                
                #if the contour around the red object is deemed as cutoff or if it is > than a certain sizxe then we will
                #treat the contoured object as a pepper and navigate toward it. If not we will ignore the contoured object
                
                cutoff = [False, False, False, False]
                for coord_index in range(0,len(bb_coord)):
                    if coord_index%2 == 0:
                        rows = np.where(contour[:,0] == bb_coord[coord_index])[0]
                        #print(f'Rows: {rows}')
                        if len(rows)>1:
                            otherDim = contour[rows][:,1]
                            #print(otherDim)
                            if max(otherDim)-min(otherDim) >= 15:
                                if coord_index==0:
                                    if abs(0-contour[rows][0][0])<3:
                                        cutoff[coord_index] = True
                                else:
                                    if abs(imgt.shape[1]-contour[rows][0][0])<3:
                                        cutoff[coord_index] = True
                    else:
                        rows = np.where(contour[:,1] == bb_coord[coord_index])[0]
                        #print(f'Rows: {rows}')
                        if len(rows)>1:
                            otherDim = contour[rows][:,0]
                            #print(otherDim)
                            if max(otherDim)-min(otherDim) >= 11:
                                if coord_index==1:
                                    if abs(0-contour[rows][0][1])<3:
                                        cutoff[coord_index] = True
                                else:
                                    if abs(imgt.shape[0]-contour[rows][0][1])<3:
                                        cutoff[coord_index] = True  
                cutoff_pepper.append(cutoff)
        return contour_BB, cutoff_pepper, BB_size

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