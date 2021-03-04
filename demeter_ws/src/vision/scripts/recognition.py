#!/usr/bin/env python3

import numpy as np
import rospy
import cv2
from matplotlib import pyplot as plt 
import os 
from camera_driver import Camera_Driver_node as CDN

import vision.srv  
from vision.msg import image_Pair
from sensor_msgs.msg import CompressedImage

from keras.preprocessing import image as image_utils
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.imagenet_utils import preprocess_input
from keras.applications import VGG16


class Recognition_Server:

    def __init__(self):
        rospy.init_node("Recognition", anonymous = True)
        self.model = VGG16(weights="imagenet")
        slef.camera = CDN("camera_out/", "640x480")
        print ("the camera is good to go")

    def pepper_Finder():
        #TODO captrure video and split images
        img_L,_ = slef.camera.video_Capture()
        print("got left img")
        #Find if there is enough read in the frames
        thresh_img = red_Finder(img_L)

        if np.count_nonzero(thresh_img > 0) >= (len(thresh_img)*len(thresh_img[0])*0.2):
            
            #TODO add amrits code here 
            coord = box_finder(img_L, thresh_img)
            single_pepper, pepper_contours = contour_finder(thresh_img, coord)
            
            #TODO return what the arm needs to reposition
            #TODO are we moving a set distance or to the center of the box
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
                #TODO stereo srv call 

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

    def box_Finder(img, imgt):
        
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
    
        return (coord)

    def contour_Finder(img, coord):

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

    def gen_Image_Pair(img_L, img_R, coords):
    
        images = image_Pair()

        images.left_Img.header.stamp = rospy.Time.now()
        images.left_Img.format = 'jpg'
        images.left_Img.data = np.array(cv2.imencode('.jpg',img_L)[1]).tostring()

        images.right_Img.header.stamp = rospy.Time.now()
        images.right_Img.format = 'jpg'
        images.right_Img.data = np.array(cv2.imencode('.jpg',img_R)[1]).tostring()
        
        #TODO change the msg to include coordinates instead 
        images.coordinates = coords
        return(images)

if __name__ == '__main__':
   
    try:
        print("Welcmoe to Demeter the Bell Pepper Harvester")
        print('Init')
        rec_system = Recognition()
        rec_system.pepper_finder()
    except rospy.ROSInterruptException:
        pass
