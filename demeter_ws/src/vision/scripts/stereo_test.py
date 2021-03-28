
import recognition2 as r
import cv2
stereo = r.Stereo_Vision()
camera = r.Camera_Driver_node("camera_out/", "240x640")
img_L, img_R = camera.img_Capture()
img_L = cv2.cvtColor(img_L, cv2.COLOR_RGB2GRAY)
img_R = cv2.cvtColor(img_R, cv2.COLOR_RGB2GRAY)

print (stereo.stereo_depth_map(img_L, img_R, (100,150)))
