#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:55:13 2021

@author: amieramie
"""

from keras.preprocessing import image as image_utils
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.imagenet_utils import preprocess_input
from keras.applications import VGG16
import numpy as np
import argparse
import cv2
import rospy
from vision.srv import *
from matplotlib import pyplot as plt 

def PredictPepperImage(req):
    print ('got it')
    imageArr = decompress(req.Left_Img)
    image = cv2.resize(imageArr,(224,224))
    plt.imshow(image)
    plt.show()
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
  
    preds = model.predict(image)
    P = decode_predictions(preds)[0]
    this_is_a_pepper = 0
    print (P) 
    bp_exists=['bell_pepper' in i for i in P]
    if sum(bp_exists)>0:
        this_is_a_pepper = P[bp_exists.index(True)][2]
    else:
        this_is_a_pepper = 0
    #for (i, (imagenetID, label, prob)) in enumerate(P[0]):
        #if (i==0)&(label == 'bell_pepper')&(prob>.9):
            #this_is_a_pepper = prob
    return MLResponse(this_is_a_pepper)

def decompress(Left_Img): 
    #to decompress the image from ros srv dont change
    array = np.frombuffer(Left_Img.data, np.uint8)
    img = cv2.imdecode(array,cv2.IMREAD_COLOR)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return(img)

if __name__ == '__main__':
     
    model = VGG16(weights="imagenet") 
    rospy.init_node('ML_Model', anonymous=True)
    s = rospy.Service('ML_req', ML, PredictPepperImage)
    print("ml_srv")
    rospy.spin()
