import cv2
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as patches

img = cv2.imread("peppercorn.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25
imgblur = cv2.filter2D(img,-1,kernel)
#plt.imshow(imgblur)
#plt.show()

imgblured = cv2.cvtColor(imgblur, cv2.COLOR_BGR2HSV)
mask_lower = cv2.inRange(imgblured,(0,120,70),(30,255,255))
mask_upper = cv2.inRange(imgblured,(110,120,70),(180,250,250))
mask = mask_lower+mask_upper

result = cv2.bitwise_and(imgblured, imgblured, mask=mask)
result2 = cv2.cvtColor(result, cv2.COLOR_HSV2RGB)
result2 = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
plt.imshow(result2)
plt.show()

edges = cv2.Canny(result, 100, 500)
plt.imshow(edges)
plt.show()

ret,thresh = cv2.threshold(edges,100,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

include = []
for c in contours:
    if cv2.contourArea(c) > 700:
        include.append(c)


imga = cv2.drawContours(img, include, -1, (0,255,0), 3)
plt.imshow(imga)
plt.show()

rows = [1 if 255 in i else 0 for i in edges]
cols = [1 if 255 in edges[:,i] else 0 for i in range(0, len(edges[0]))]

top = rows.index(1)
left = cols.index(1)
rows.reverse()
cols.reverse()
right = len(cols) - cols.index(1)-1
bottom = len(rows) - rows.index(1)-1
print(top, bottom, left, right)

cv2.rectangle(img,(left,top),(right,bottom),(0,255,0),2)
fig, ax = plt.subplots()
ax.imshow(img)
plt.show()
