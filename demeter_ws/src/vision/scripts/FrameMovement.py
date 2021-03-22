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

def find_BoundingBox(imgSection):
    stop = False
    contour_BB = []
    BB_size = []
    cutoff_pepper = []
    try:
        imgt = red_Finder(imgSection)
    except:
        stop = True
    #Find contours
    if not(stop):
        pepper_cont = contour_Finder(imgt, [0,0,imgt.shape[1],imgt.shape[0]])
        try:
            if len(pepper_cont) == 0:
                stop = True
        except:
            print('Contours found')
        
    if not(stop):
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
            contour_BB.append(bb_coord)
            BB_size.append(abs((bb_coord[2] - bb_coord[0])*(bb_coord[3]-bb_coord[1])))
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

rightLeft = [0,2]
upDown = [1,3]
frameSize = 75
for i in range(0,math.ceil(fullImg.shape[1]/frameSize)):
    for j in range(0,math.ceil(fullImg.shape[0]/frameSize)): 
        initialValues = [i*frameSize,j*frameSize,min((i+1)*frameSize,fullImg.shape[1]),min((j+1)*frameSize,fullImg.shape[0])]
        initials = np.array(initialValues)
        imgSeg = fullImg[initials[1]:initials[3]-1,initials[0]:initials[2]-1]
        frameShape = fullImg.shape
        print('Moving From this Frame')
        print(initials)
        plt.imshow(imgSeg)
        plt.show()
        contour_BB, cutoff_pepper,BB_size = find_BoundingBox(imgSeg)
        for contour_index in range(0,len(contour_BB)):
            print(f'Contour {contour_index}:')
            boundingBox = np.array(contour_BB[contour_index])
            cutoff = cutoff_pepper[contour_index]
            size = BB_size[contour_index]
            if ((len(boundingBox)>0)&((size>750)|(sum(cutoff)>0))):
                #print(boundingBox)
                correctBoundingBox = boundingBox + [-11,-11,11,11]
                initialCutoffs = np.array(cutoff)
                print(initialCutoffs)
                attempt = 0
                stop = False
                fullPepperFound = False
                movements = np.array([0,0,0,0])
                print('Navigating towards contour from: ')
                initials = np.array(initialValues)
                imgSeg = fullImg[initials[1]:initials[3],initials[0]:initials[2]]
                plt.imshow(imgSeg)
                plt.show()
                while(((sum(movements!=0)>=1)|(attempt == 0))&((stop == False)&(fullPepperFound==False))):
                    movements = np.array([0,0,0,0])
                    attempt = attempt + 1
                    print(f'Attempt {attempt}:')
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
                    initials = initials+movements
                    initials = np.array(list(map(lambda x: x,initials)))
                    print(initials)
                    if (initials[0]<0)|(initials[1]<0)|(initials[2]>frameShape[1])|(initials[0]>frameShape[0]):
                        stop = True
                    elif attempt>5:
                        stop = True
                    else:
                        imgSeg = fullImg[initials[1]:initials[3],initials[0]:initials[2]]
                        plt.imshow(imgSeg)
                        plt.show()
                        contours, cutoffs, BB_sizes = find_BoundingBox(imgSeg)
                        for contour_index in range(0,len(contours)):
                            if np.array_equal((np.array(contours[contour_index])<correctBoundingBox),np.array([False,False,True,True])):
                                mainContour = contour_index
                        cutoff = np.array(cutoffs[mainContour])
                        correctBoundingBox = np.array(contours) + [-11,-11,11,11]
                        fullPepperFound = (sum(cutoff)==0)
                if fullPepperFound:
                    print(f'Full Pepper Found Here is the Bounding Box: {np.array(contours[mainContour])+[-5,-5,5,5]}')
            else:
                print('Contour was not recognized as a pepper')
#         left, top, right, bottom = box_Finder(imgSeg, imgt)
#         coord = [left,top,right,bottom]
#         cv2.rectangle(imgSeg,(left,top),(right,bottom),(0,255,0),1)
#         plt.imshow(imgSeg)
