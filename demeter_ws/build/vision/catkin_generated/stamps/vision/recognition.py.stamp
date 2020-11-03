#!/usr/bin/env python3

import numpy as np
import rospy
import cv2
from matplotlib import pyplot as plt 
#import keras 
from vision.msg import image_Pair 
from sensor_msgs.msg import CompressedImage

#TODO CCN goes here
#def CNN():

def gen_Image_Pair():
    
    images = image_Pair()

    imgL = cv2.imread('/home/juanpbm/capstone/Demeter/demeter_ws/src/images/wall/left.jpg')
    imgR = cv2.imread('/home/juanpbm/capstone/Demeter/demeter_ws/src/images/wall/right.jpg')

    images.left_Img.header.stamp = rospy.Time.now()
    images.left_Img.format = 'jpg'
    images.left_Img.data = np.array(cv2.imencode('.jpg',imgL)[1]).tostring()

    images.right_Img.header.stamp = rospy.Time.now()
    images.right_Img.format = 'jpg'
    images.right_Img.data = np.array(cv2.imencode('.jpg',imgR)[1]).tostring()

    images.center = (820,810)
    images.top = (1,2)
    images.bottom = (2,3)

    input('wait')
    return(images)

def publisher():
    
    pub = rospy.Publisher('Rec_Image', image_Pair, queue_size=10)
    rospy.init_node('Recognition',anonymous=True)
    r = rospy.Rate(10)  

    while not rospy.is_shutdown():

        images = gen_Image_Pair()
        #rospy.loginfo(images)
        pub.publish(images)
        r.sleep()

    
if __name__ == '__main__':
    try: 
        publisher()
    except rospy.ROSInterruptException:
        pass
