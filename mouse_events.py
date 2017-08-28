# @Author: Varoon Pazhyanur <varoon>
# @Date:   15-08-2017
# @Filename: mouse_events.py
# @Last modified by:   varoon
# @Last modified time: 15-08-2017



import cv2
import numpy

#Mouse handler function
def draw_circle(event, x,y, flags, param):
    if(event==cv2.EVENT_LBOTTONDLCLK):
        cv2.circle(image, (x,y),100,(255,255,0),-1)
#make black image
image = numpy.zeros((512,512,3),numpy.uint32)
cv2.namedWindow("WINDOW NAME")
cv2.setMouseCallback('WINDOW NAME', draw_circle)
while(True):
    cv2.imshow('WINDOW NAME', image)
    if(cv2.waitkey(20) & 0xFF==27):
        break
cv2.destroyAllWindows
