import cv2
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as patches
import os

def thresh_image(img):

    #Bluring 
    kernel = np.ones((5,5),np.float32)/25
    imgblur = cv2.filter2D(img,-1,kernel)
    imgblured = cv2.cvtColor(imgblur, cv2.COLOR_BGR2HSV)
    
    #thresholding
    mask_lower = cv2.inRange(imgblured,(0,120,70),(30,255,255))
    mask_upper = cv2.inRange(imgblured,(120,120,70),(180,250,250))
    mask = mask_lower+mask_upper

    result = cv2.bitwise_and(imgblured, imgblured, mask=mask)
    result = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)

    #plt.imshow(result)
    #plt.show()
    return (result)

def pepper_finder(img, imgt):
    #find edges
    edges = cv2.Canny(imgt, 100, 500)
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
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.show()
    return (coord)

def contour_finder(img, coord):
    #TODO return bool if there is only one countour inside else return how many and the coords
    crop_img = img[coord[1]:coord[3], coord[0]:coord[2]]
    plt.imshow(crop_img)
    plt.show()

    crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(crop_img,100,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    include = []
    for c in contours:
        if cv2.contourArea(c) > 700:
            include.append(c)
            
    imga = cv2.drawContours(crop_img, include, -1, (0,255,0), 3)
    plt.imshow(imga)
    plt.show()

if __name__ == "__main__":

    for i in os.listdir('ltest/'):
        img = cv2.cvtColor(cv2.imread("ltest/" + i), cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.show()

        imgt = thresh_image(img)
        coord = pepper_finder(img, imgt)
        
        #contours to see if there are multiple
        #contour_finder(imgt,coord)
        
        if coord[0] < 10:
            print ("move camera to the left")
        elif coord[1] < 10:
            print("move camera up")
        elif coord[2] > len(img[0])-10:
            print("move camera to the right")
        elif coord[3] > len(img)-10:
            print("move camera down")
        else:
            print("the pepper is in the picture")
            #ML model to see if the peper is ready
