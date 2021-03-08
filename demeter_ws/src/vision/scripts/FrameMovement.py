#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:30:52 2021

@author: amieramie
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt 
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
    edges = cv2.Canny(imgt, 400, 50, L2gradient = True)
    #plt.imshow(edges)
    #plt.show()

    #which cols and rows have an edge
    rows = [1 if 255 in edges[i,:] else 0 for i in range(0,edges.shape[0])]
    cols = [1 if 255 in edges[:,i] else 0 for i in range(0,edges.shape[1])]

    #find the bounding box 
    top = rows.index(1)
    left = cols.index(1)
    right = len(cols) - 1 - cols[::-1].index(1)
    bottom = len(rows) - 1 - rows[::-1].index(1)

    print(left, right)

    
    #coord = [left,top,right,bottom]
#     cv2.rectangle(img,(left,top),(right,bottom),(0,255,0),2)
#     plt.imshow(img)
#     plt.show()

    return left, top, right, bottom, rows, cols
def contour_Finder(img, coord):

    crop_img = img[coord[1]:coord[3], coord[0]:coord[2]]
    #plt.imshow(crop_img)        
    #plt.show()

    crop_img_gry = cv2.cvtColor(crop_img, cv2.COLOR_RGB2GRAY)
    ret,thresh = cv2.threshold(crop_img_gry,50,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_L1)

    threshold = (len(crop_img)*len(crop_img[0])*0.01)
    pepper_cont = [contours[i] for i in range (0,len(contours)) if (hierarchy[0,i,3] == -1 and cv2.contourArea(contours[i]) > threshold)]

#     print(len(pepper_cont))       
#     imga = cv2.drawContours(crop_img, pepper_cont, -1, (0,255,0), 1)
#     plt.imshow(imga)
#     plt.show()


    #TODO what are the return values and how to manage error 
    #IDEA return count of peppers, and contours if more than on flag them in the other function
    if len(pepper_cont) <= 0:
        return pepper_cont
    elif len(pepper_cont) == 1:
        return pepper_cont
    else:
        #TODO what can be done if many 
        return pepper_cont, contours
def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax
rightLeft = [0,2]
upDown = [1,3]
frameSize = 75
for i in range(0,math.ceil(fullImg.shape[1]/frameSize)):
    for j in range(0,math.ceil(fullImg.shape[0]/frameSize)): 
        initials = np.array([i*frameSize,j*frameSize,min((i+1)*frameSize,fullImg.shape[0]),min((j+1)*frameSize,fullImg.shape[1])])
        imgSeg = fullImg[initials[1]:initials[3]-1,initials[0]:initials[2]-1]
        print('Moving From this Frame')
        print(initials)
        plt.imshow(imgSeg)
        plt.show()
        movements = np.array([0,0,0,0])
        stop = False
        attempt = 0
        while(((sum(movements!=0)>=1)|(attempt == 0))&(stop == False)):
            movements = np.array([0,0,0,0])
            try:
                imgt = red_Finder(imgSeg)
                #Find edges
            except:
                stop = True
            try:
                left, top, right, bottom = box_Finder(imgSeg, imgt)
            except:
                stop == True
            if not(stop):
                print(f'Attempt {attempt}')
                attempt+=1
                if left ==0:
                    print('left')
                    movements[0] = -10
                    movements[2] = -10
                elif  top == 0:
                    print('top')
                    movements[1] = -10
                    movements[3] = -10
                elif right == imgSeg.shape[0]-1:
                    print('right')
                    movements[2] = 10
                    movements[0] = 10
                elif  bottom == imgSeg.shape[1]-1:
                    print('bottom')
                    movements[3] = 10
                    movements[1] = 10
                print(f'Initials 1: {initials}')
                initials = initials+movements
                initials = np.array(list(map(lambda x: max(x,0),initials)))
                imgSeg = fullImg[initials[1]:initials[3]-1,initials[0]:initials[2]-1]
                print(movements)
                print(f'Initials 2: {initials}')
                stop = len(np.where(initials<0)[0])>0
                cv2.imwrite(f'/Users/amieramie/Desktop/Capstone\ Computer\ Vision/testImages/{i}_{j}_try{attempt}.jpg',imgSeg)
                plt.imshow(imgSeg)
                plt.show()
        
        if (attempt>0)&(stop==False):
            print('Full Pepper Found')
        else:
            print('No Pepper in Frame')
#         left, top, right, bottom = box_Finder(imgSeg, imgt)
#         coord = [left,top,right,bottom]
#         cv2.rectangle(imgSeg,(left,top),(right,bottom),(0,255,0),1)
#         plt.imshow(imgSeg)
