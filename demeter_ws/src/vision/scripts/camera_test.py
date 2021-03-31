from recognition2 import Camera_Driver_node  as CMD

from matplotlib import pyplot as plt
from vision.srv import *
import rospy 
from sensor_msgs.msg import CompressedImage
import numpy as np
import cv2

rospy.init_node("test",anonymous = True)
ml_srv = rospy.ServiceProxy('ML_req', ML)

camera = CMD("camera_out/", "960x640")
#img_L, img_R = camera.video_Capture()
img_L, img_R = camera.img_Capture()

#plt.imshow(img_R)
#plt.show()
img_L = img_L[115:220,150:250]
plt.imshow(img_L)
plt.show()
images = CompressedImage()
images.header.stamp = rospy.Time.now()
images.format = 'jpg'
images.data = np.array(cv2.imencode('.jpg',img_L)[1]).tostring()

print('send')

print(ml_srv(images))

