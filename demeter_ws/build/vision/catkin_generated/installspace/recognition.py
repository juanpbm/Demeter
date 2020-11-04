#!/usr/bin/env python3

import numpy as np
import rospy
import cv2
from matplotlib import pyplot as plt 
#import keras 
from vision.msg import image_Pair 
from sensor_msgs.msg import CompressedImage

#TODO how will it know when the arm is ready in position 
#to take the pics of the next pepper

#TODO publish to next flag topic 

#TODO take images or subscribe to the camera topic

#TODO CNN

#TODO How is the robot gonna know/inform there are no more ppepers (END) 
#would it go here on in the previous package

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
    pub.publish(images)
    #return(images)

    
if __name__ == '__main__':
    try: 
        
        rospy.init_node('Recognition',anonymous=True)
        pub = rospy.Publisher('Rec_Image', image_Pair, queue_size=10)
        r = rospy.Rate(10)  
        
        while not rospy.is_shutdown():
            gen_Image_Pair()
            r.sleep()

    except rospy.ROSInterruptException:
        pass
