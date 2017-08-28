# @Author: Varoon Pazhyanur <varoon>
# @Date:   17-08-2017
# @Filename: drawing_with_mouse_more.py
# @Last modified by:   varoon
# @Last modified time: 17-08-2017


import cv2
import numpy as np

drawing = False #True when mouse pressed
mode = True #True if rect. Press m to toggle to curve
ix,iy = -1,-1

#MOUSE CALLBACK!
def draw_circle(event,x,y,flags,param):
    global ix,iy, drawing, mode
    if(event == cv2.EVENT_LBUTTONDOWN):
        drawing = True
        ix,iy = x,y
    elif(event == cv2.EVENT_MOUSEMOVE):
        if(drawing==True):
            if(mode==True):
                cv2.rectangle(img, (ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img, (x,y),5,(0,0,255),-1)
    elif(event == cv2.EVENT_LBUTTONUP):
        drawing = False
        if(mode == True):
            cv2.rectangle(img, (ix,iy), (x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow("Image")
cv2.setMouseCallback("Image",draw_circle)

while(True):
    cv2.imshow("Image", img)
    k = cv2.waitKey(1) & 0xFF
    if(k==ord('m')):
        mode = not mode
    elif(k==27):
        break

cv2.destroyAllWindows()
