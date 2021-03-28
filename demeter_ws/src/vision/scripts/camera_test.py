from recognition2 import Camera_Driver_node  as CMD

from matplotlib import pyplot as plt

camera = CMD("camera_out/", "960x640")
#img_L, img_R = camera.video_Capture()
img_L, img_R = camera.img_Capture()
plt.imshow(img_L)
plt.show()
plt.imshow(img_R)
plt.show()
