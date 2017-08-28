# @Author: Varoon Pazhyanur <varoon>
# @Date:   17-08-2017
# @Filename: drawing_with_mouse.py
# @Last modified by:   varoon
# @Last modified time: 17-08-2017


#GOAL: Make a blank canvas that will draw a blue filled circle on each left click. Press ESC to exit.

import cv2
import numpy
#This uses mouse events. To see all events, in a python shell, import cv2 then run
#print([i for i in dir(cv2) if 'EVENT' in i])

#MOUSE CALLBACK
def draw_circle(event, x, y, flags, param):
    if(event==cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img, (x,y),100,(255,0,0),-1)

img = numpy.zeros((512,512,3), numpy.uint8)
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_circle)

while(1):
    cv2.imshow("Image", img)
    if(cv2.waitKey(20) & 0xFF==27):
        break
cv2.destroyAllWindows()
