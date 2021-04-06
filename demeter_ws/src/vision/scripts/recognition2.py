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
from matplotlib import patches 
import os 
import subprocess 
import time 
import json 
from stereovision.calibration import StereoCalibrator
from stereovision.calibration import StereoCalibration
from datetime import datetime

from vision.srv import * 
from vision.msg import image_Pair
from sensor_msgs.msg import CompressedImage

class Stereo_Vision():
    def __init__(self):
        # Depth map default preset
        self.SWS = 5
        self.PFS = 5
        self.PFC = 29
        self.MDS = -30
        self.NOD = 160
        self.TTH = 100
        self.UR = 10
        self.SR = 14
        self.SPWS = 100

        # Camera settimgs
        cam_width = 1280
        cam_height = 480

        # Final image capture settings
        scale_ratio = 0.5

        # Camera resolution height must be dividable by 16, and width by 32
        cam_width = int((cam_width+31)/32)*32
        cam_height = int((cam_height+15)/16)*16
        print ("Used camera resolution: "+str(cam_width)+" x "+str(cam_height))

        #TODO Buffer for captured image settings maybe remove 
        self.img_width = int (cam_width * scale_ratio)
        self.img_height = int (cam_height * scale_ratio)
        #self.capture = np.zeros((img_height, img_width, 4), dtype=np.uint8)
        #print ("Scaled image resolution: "+str(img_width)+" x "+str(img_height))

        # Implementing calibration data
        print('Read calibration data and rectifying stereo pair...')
        self.calibration = StereoCalibration(input_folder='calib_result')

        self.disparity = np.zeros((self.img_width, self.img_height), np.uint8)
        self.sbm = cv2.StereoBM_create(numDisparities=0, blockSize=21)
        self.load_map_settings ("3dmap_set.txt")
        
    def stereo_depth_map(self, img_L, img_R):
        
        rectified_pair = self.calibration.rectify((img_L, img_R))
        Left = rectified_pair[0]
        Right = rectified_pair[1]
        self.disparity = self.sbm.compute(img_L,img_R)
        #Z = (10000*6*0.3)/self.disparity[coord]
        return (self.disparity)

    def load_map_settings(self, fName ):
            
        print('Loading parameters from file...')
        f=open(fName, 'r')
        data = json.load(f)
        self.SWS=data['SADWindowSize']
        self.PFS=data['preFilterSize']
        self.PFC=data['preFilterCap']
        self.MDS=data['minDisparity']
        self.NOD=data['numberOfDisparities']
        self.TTH=data['textureThreshold']
        self.UR=data['uniquenessRatio']
        self.SR=data['speckleRange']
        self.SPWS=data['speckleWindowSize']    
        
        #self.sbm.setSADWindowSize(SWS)
        self.sbm.setPreFilterType(1)
        self.sbm.setPreFilterSize(self.PFS)
        self.sbm.setPreFilterCap(self.PFC)
        self.sbm.setMinDisparity(self.MDS)
        self.sbm.setNumDisparities(self.NOD)
        self.sbm.setTextureThreshold(self.TTH)
        self.sbm.setUniquenessRatio(self.UR)
        self.sbm.setSpeckleRange(self.SR)
        self.sbm.setSpeckleWindowSize(self.SPWS)
        f.close()
        print ('Parameters loaded from file '+fName)



class Camera_Driver_node:

    def __init__(self, out_path, res):
        self.out_path = out_path 
        self.res = res #in the from of #x# 
        self.stereo = Stereo_Vision()

    def video_Capture(self):
        #Capture video and processing of each frame
        print("video Capture is On:") 
        red = 0
        cap = cv2.VideoCapture(0)
        while not red:
            print("-")
            ret,frame=cap.read()
            img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            #split 
            img_L, img_R = self.split_Img(img)  
            red,_ = self.red_Finder(img_L)
            
        cap.release()
        rectified_pair = self.stereo.calibration.rectify((img_L, img_R))
        img_L = rectified_pair[0]
        img_R = rectified_pair[1]
        print("Red Found in the Frame. End video capture")
        return(img_L, img_R)

    def img_Capture(self):
        #Capture image and send it back
       
        while (True):
            try:
                print('Taking Img') 
                cap = cv2.VideoCapture(0)
                ret,frame = cap.read()
                cap.release()
                if (frame.size != 0):
                    break 
            except:
                print ("Camera error!!!")

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_L, img_R = self.split_Img(img) 
        rectified_pair = self.stereo.calibration.rectify((img_L, img_R))
        img_L = rectified_pair[0]
        img_R = rectified_pair[1]
        plt.imshow(img_L)
        plt.show()
        print("Image Capture Complete")
        return(img_L, img_R)


    def red_Finder(self, img):

        #Bluring 
        kernel = np.ones((5,5),np.float32)/25
        img_blured = cv2.filter2D(img,-1,kernel)
        img_blured = cv2.cvtColor(img_blured, cv2.COLOR_RGB2HSV)                                            
        
        #Thresholding
        mask_lower = cv2.inRange(img_blured,(0,120,70),(12,255,255))      
        mask_upper = cv2.inRange(img_blured,(160,120,70),(180,250,250))
        mask = mask_lower + mask_upper
        
        thresh_img = cv2.bitwise_and(img_blured, img_blured, mask=mask)
        thresh_img = cv2.cvtColor(thresh_img, cv2.COLOR_HSV2RGB)        
    
        if np.count_nonzero(thresh_img > 0) >= (len(thresh_img)*len(thresh_img[0])*0.1):
            print('there may be peppers')
            return(True, thresh_img)
        else:
            print("no red")
            return(False, thresh_img)   
    
    def split_Img(self,img):
        img_width =  int(self.res.split('x')[1])//2
        img_height = int(self.res.split('x')[0])
        img_L = img[0:img_height,0:img_width] #Y+H and X+W
        img_R = img[0:img_height,img_width:img_width*2]
        return(img_L, img_R)


class Recognition:

    def __init__(self):
    
        rospy.init_node("Recognition", anonymous = True)
        self.camera = Camera_Driver_node("camera_out/", "240x640")
        self.stereo = Stereo_Vision()
        self.stop_srv = rospy.ServiceProxy('stop', Action)
        self.reposition_srv = rospy.ServiceProxy('reposition', Reposition)
        self.harvest_srv = rospy.ServiceProxy('harvest', Reposition)
        self.s = rospy.Service('start', Action, self.start)
        self.ml_srv = rospy.ServiceProxy('ML_req', ML)
        print ("Recognition Node has been setup")

    def pepper_Finder(self):
        
        print("Recognition system initialized")
        position = geometry_msgs.msg.Point()
        
        while(True): 
            
            #Captrure video and split images
            img_L,_ = self.camera.video_Capture()
            
            #Ask the arm to stop if it gets a false back keep asking until it stops
            while (True):
                s = self.stop_srv(True)
                if(s.Ack):
                    break 

            #Take a new image in case the are moved
            img_L, img_R = self.camera.img_Capture();      
            
            #Find if there is enough read in the frames
            treshold, thresh_img = self.camera.red_Finder(img_L)
            
            if treshold:
                
                #Initial coordinates from the arm
                X_coord = s.Location.x
                Y_coord = s.Location.y
                Z_coord = s.Location.z
                print(s.Location) 
                
                contour_BB, cutoff_pepper,BB_size = self.find_BoundingBox(img_L)
                print("Number of contours", len(contour_BB))
                
                if len(contour_BB)>0:
                    for contour_index in range(0,len(contour_BB)):
                        print(f'Contour {contour_index}:')
                        #Bounding box dimensions based on pixels within frame [left, top, right bottom]
                        boundingBox = np.array(contour_BB[contour_index])
                        cutoff = cutoff_pepper[contour_index]
                        size = BB_size[contour_index]   
                        
                        #If the contour around the red object is deemed as cutoff or if it is > than a certain sizxe then we will
                        #Treat the contoured object as a pepper and navigate toward it. If not we will ignore the contoured object
                        if ((len(boundingBox)>0)&((size>50)|(sum(cutoff)>0))):
                            
                            #Increasing the bounding box size to help navigate towards the right contour
                            correctBoundingBox = boundingBox + [-11,-11,11,11]
                            initialCutoffs = np.array(cutoff)
                        
                            attempt = 0
                            stop = False
                            fullPepperFound = False
                            movements = np.array([0,0,0,0])
                            
                            while(((sum(movements!=0)>=1)|(attempt == 0))&((stop == False)&(fullPepperFound==False))):
                            
                                movements = np.array([0,0,0,0], dtype=float)
                                attempt+=1
                                print(f'Attempt {attempt}:')
                                
                                if cutoff[0] ==True:
                                    print('left')
                                    movements[0] += -0.10
                                    movements[2] += -0.10
                                    Y_coord += 0.05
                                if  cutoff[1] == True:
                                    print('top')
                                    movements[1] += -0.10
                                    movements[3] += -0.10
                                    Z_coord += 0.05
                                if cutoff[2] == True:
                                    print('right')
                                    movements[2] -= 0.10
                                    movements[0] -= 0.10
                                    Y_coord -= 0.05
                                if  cutoff[3] == True:
                                    print('bottom')
                                    movements[3] -= 0.10
                                    movements[1] -= 0.10
                                    Z_coord -= 0.05
                                #TODO one if??
                                if ((cutoff[0]) &(cutoff[2]))|((cutoff[1]) &(cutoff[3])):
                                    #Move camera back on z axis, and feedback for getting new movement coordinates
                                    print('Zoom out')
                                    position.x = X_coord - 0.05
                                    position.y = Y_coord 
                                    position.z = Z_coord   
                                    position_ack= self.reposition_srv(position)
                                if attempt>5:
                                    #implement a zoom out system here as well since
                                    #if the attempts reach 6 it likely means that the magnitude is too large and we keep over correcting in each
                                    #direction
                                    position.x = X_coord - 0.05
                                    position.y = Y_coord 
                                    position.z = Z_coord 
                                    position_ack= self.reposition_srv(position)
                                    stop = True
                                else:
                                    print("Attempting to reposition arm based on coordinates and take another image")
                                    
                                    position.x = X_coord
                                    position.y = Y_coord
                                    position.z = Z_coord 
                                    
                                    position_ack = self.reposition_srv(position)
                                    time.sleep(5)
                                    #Take a new image in case the are moved
                                    img_L, img_R = self.camera.img_Capture()
                                    
                                    if sum(movements!=0)>0:
                                        hasMoved = True
                                    else:
                                        hasMoved = False
                                    
                                    contours, cutoffs, BB_sizes = self.find_BoundingBox(img_L)
                                    print(contours,cutoffs,BB_sizes)
                                    mainContour = 0
                                    for contour_index in range(0,len(contours)):
                                        print(f'The contour is within the correct bounding box: {(np.array(contours[contour_index])<correctBoundingBox)}')
                                        print(contours[contour_index])
                                        print(correctBoundingBox)
                                        if np.array_equal((np.array(contours[contour_index])<correctBoundingBox),np.array([False,False,True,True])):
                                            print(f'The nmain Contour was found: {(np.array(contours[contour_index])<correctBoundingBox)}')
                                            print(contours[contour_index])
                                            print(correctBoundingBox)
                                            mainContour = contour_index
                                            break
                                    print(f'Movements: {movements}')
                                    if len(contours)==0:
                                        stop = True
                                    else:
                                        cutoff = np.array(cutoffs[mainContour])
                                        if (hasMoved):
                                            correctBoundingBox = np.array(contours[mainContour]) + [-11,-11,11,11]
                                        fullPepperFound = (sum(cutoff)==0)
                            if fullPepperFound:
                                print(f'Full Pepper Found Here is the Bounding Box: {np.array(contours[mainContour])}')
                                coordinates_of_BB = np.array(contours[mainContour])

                                #Send to ML Model and check if this is a pepper 
                                img_ML = img_L[coordinates_of_BB[1]:coordinates_of_BB[3], coordinates_of_BB[0]:coordinates_of_BB[2]]
                                images = CompressedImage()
                                images.header.stamp = rospy.Time.now()
                                images.format = 'jpg'
                                images.data = np.array(cv2.imencode('.jpg',img_ML)[1]).tostring()
                                prob = self.ml_srv(images)                
                                
                                #show original image plus bounding box
                                fig, ax = plt.subplots()
                                ax.imshow(img_L)
                                rect = patches.Rectangle((coordinates_of_BB[0], coordinates_of_BB[1]), coordinates_of_BB[2]-coordinates_of_BB[0], coordinates_of_BB[3]-coordinates_of_BB[1], linewidth=1, edgecolor='r', facecolor='none')
                                ax.add_patch(rect)
                                plt.show()
                                

                                if prob.Percentage >= 0.8:
                                    #print("prob > 80")
                                    #Stereo Vision
                                    img_L = cv2.cvtColor(img_L, cv2.COLOR_RGB2GRAY)
                                    img_R = cv2.cvtColor(img_R, cv2.COLOR_RGB2GRAY)
                                    point_coord = (coordinates_of_BB[1],((coordinates_of_BB[2]+coordinates_of_BB[0])//2))

                                    disp_map = self.stere6.stereo_depth_map(img_L,img_R)
                                    stereo_BB = disp_map[coordinates_of_BB[1]:coordinates_of_BB[3], coordinates_of_BB[0]:coordinates_of_BB[2]]
                                    stereo_BB = ((6*0.3)/stereo_BB)*100
                                    stereo_BB_Norm =np.array([j for i in stereo_BB for j in i if (j > 0 and j < 0.5)])
                                    
                                    camera_to_blade = 0.05
                                    camera_to_blade_height = 0.15
                                    camera_to_center = 0.06
                                    z = np.median(stereo_BB_Norm)
                                    x = (((((coordinates_of_BB[0]+coordinates_of_BB[2])/2)-160)*z)/0.3)/1000
                                    y = ((((-coordinates_of_BB[1])+120)*z)/0.3)/1000
                                    print("X",x,"y",y,"Z",z)

                                    harvest_pos = geometry_msgs.msg.Point(x = X_coord + z - camera_to_blade, y = Y_coord - x - camera_to_center , z = Z_coord + y + camera_to_blade_height)
                                    print("harvest",harvest_pos)
                                    print(self.harvest_srv(harvest_pos))
                            else:
                                print('Full Pepper was unable to be found from this starting frame')
                        else:
                            print('Contour was not recognized as a pepper')
                else:
                    print('No Contours were found')
            else:
                #Reposition the arm to go back if it moved after possible pepper was found 
                position_ack = self.reposition_srv (s.Location)
            
            x = input("next round")
            s = self.stop_srv(False)
    
      
#TODO remove 
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

        crop_img_gry = cv2.cvtColor(crop_img, cv2.COLOR_RGB2GRAY)
        ret,thresh = cv2.threshold(crop_img_gry,50,255,0)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_L1)

        threshold = (len(crop_img)*len(crop_img[0])*0.01)
        pepper_cont = [contours[i] for i in range (0,len(contours)) if (hierarchy[0,i,3] == -1 and cv2.contourArea(contours[i]) > threshold)]
              
        imga = cv2.drawContours(crop_img, pepper_cont, -1, (0,255,0), 3)
        plt.imshow(imga)
        plt.show()

        
        #TODO what here or do you just need the pepper count?
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
            #print('coont')
            try:
                if len(pepper_cont) == 0:
                    stop = True
                    print('function find_BoundingBox: no pepper_cont')
                else:
                    #print(pepper_cont)
                    print("function find_BoundingBox: contours found")
            except:
                print('function find_BoundingBox: Contours not found')

        if not(stop):
            #depending on the number of contours found the data structure of the output of the contour function wil be different
            if isinstance(pepper_cont,tuple):
                pepper_cont_temp = pepper_cont[0]
            else:
                pepper_cont_temp = pepper_cont

            for contour in pepper_cont_temp:
                
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
                        
                        if len(rows)>1:
                            otherDim = contour[rows][:,1]
                            
                            if max(otherDim)-min(otherDim) >= 15:
                                if coord_index==0:
                                    if abs(0-contour[rows][0][0])<3:
                                        cutoff[coord_index] = True
                                else:
                                    if abs(imgt.shape[1]-contour[rows][0][0])<3:
                                        cutoff[coord_index] = True
                    else:
                        rows = np.where(contour[:,1] == bb_coord[coord_index])[0]

                        if len(rows)>1:
                            otherDim = contour[rows][:,0]
                            
                            if max(otherDim)-min(otherDim) >= 11:
                                if coord_index==1:
                                    if abs(0-contour[rows][0][1])<3:
                                        cutoff[coord_index] = True
                                else:
                                    if abs(imgt.shape[0]-contour[rows][0][1])<3:
                                        cutoff[coord_index] = True  
                cutoff_pepper.append(cutoff)
        return contour_BB, cutoff_pepper, BB_size
    #TODO remove 
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
        print("Welcome to Demeter the Bell Pepper Harvester")
        rec_system = Recognition()
        
        print("Waiting for the arm driver to be online")
        rospy.wait_for_service('stop')
        
        print("arm driver detected")
        rec_system.pepper_Finder()
    except rospy.ROSInterruptException:
               print('!!!!!!!!!There has been an Unknown Error')
