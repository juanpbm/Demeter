from camera_driver import Camera_Driver_node  as CMD

camera = CMD("camera_out/", "640x480")
camera.video_Capture()
#camera.img_Capture()
