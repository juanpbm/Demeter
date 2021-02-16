import cv2
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as patches
import os

def thresh_image(img):

    #Bluring 
    kernel = np.ones((5,5),np.float32)/25
    imgblur = cv2.filter2D(img,-1,kernel)
    imgblured = cv2.cvtColor(imgblur, cv2.COLOR_RGB2HSV)
    
    #Thresholding
    mask_lower = cv2.inRange(imgblured,(0,120,70),(10,255,255))
    mask_upper = cv2.inRange(imgblured,(165,120,70),(180,250,250))
    mask = mask_lower+mask_upper

    result = cv2.bitwise_and(imgblured, imgblured, mask=mask)
    result = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)

    #plt.imshow(result)
    #plt.show()
    return (result)

def pepper_finder(img, imgt):
    #find edges
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

def contour_finder(img, coord):
    #TODO return bool if there is only one countour inside else return how many and the coords
    crop_img = img[coord[1]:coord[3], coord[0]:coord[2]]
    #plt.imshow(crop_img)
    #plt.show()

    crop_img_gry = cv2.cvtColor(crop_img, cv2.COLOR_RGB2GRAY)
    ret,thresh = cv2.threshold(crop_img_gry,50,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_L1)
     
    pepper_cont = []
    threshold = (len(imgt)*len(imgt[0])*0.01)

    for i in range(0,len(contours)):
        if hierarchy[0,i,3] == -1 and cv2.contourArea(contours[i]) > threshold:
            pepper_cont.append(contours[i])
    
    print(len(pepper_cont))       
    imga = cv2.drawContours(crop_img, pepper_cont, -1, (0,255,0), 3)
    plt.imshow(imga)
    plt.show()

    #TODO what are the return values and how to manga error 
    if len(pepper_cont) == 0:
        return(-1,-1)
    elif len(pepper_cont) == 1:
        return(True, pepper_cont)
    else:
        #TODO what can be done if many 
        return(False, pepper_cont)


if __name__ == "__main__":

    for i in os.listdir('test/'):
        img = cv2.cvtColor(cv2.imread("test/" + i), cv2.COLOR_BGR2RGB)
        imgt = thresh_image(img)

        print(np.count_nonzero(imgt >0)/3)
        if np.count_nonzero(imgt > 0) >= (len(imgt)*len(imgt[0])*0.2):
            print('there may be peppers')

            coord = pepper_finder(img, imgt)
            #contours to see if there are multiple
            single_pepper, pepper_contour = contour_finder(imgt,coord)
            
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
        else:
            print("no pepper here")
