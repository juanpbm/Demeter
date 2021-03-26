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

def PredictPepperImage(imgArr):
    image = np.expand_dims(imageArr, axis=0)
    image = preprocess_input(imageArr)
    model = VGG16(weights="imagenet")
    P = decode_predictions(preds)[0]
    this_is_a_pepper = False
    for (i, (imagenetID, label, prob)) in enumerate(P[0]):
        if (i==0)&(label == 'bell_pepper')&(prob>.9):
            this_is_a_pepper = True
    return this_is_a_pepper