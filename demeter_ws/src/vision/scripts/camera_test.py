from camera_driver import Camera_Driver_node  as CMD

from matplotlib import pyplot as plt

camera = CMD("camera_out/", "640x480")
#camera.video_Capture()
img_L, img_R = camera.img_Capture()
plt.imshow(img_L)
plt.show()
