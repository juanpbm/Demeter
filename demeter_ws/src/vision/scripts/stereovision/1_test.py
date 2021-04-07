import numpy as np
import cv2
import recognition2 as r
cap = cv2.VideoCapture(0)
camera = r.Camera_Driver_node("camera_out/", "240x640")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Our operations on the frame come here
    t, imgt = camera.red_Finder(frame)
    img = cv2.cvtColor(imgt, cv2.COLOR_RGB2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',imgt)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
