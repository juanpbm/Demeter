
import recognition2 as r

stereo = r.Stereo_Vision()

img=cv2.imread('./scenes/photo.png')
img = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
img_width = 320
img_height = 480
img_L = img[0:img_height,0:img_width] #Y+H and X+W
img_R = img[0:img_height,img_width:img_width*2]

print (stereo.stereo_depth_map(img_L, img_R, (120,220)))
