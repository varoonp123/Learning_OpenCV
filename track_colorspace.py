# @Author: Varoon Pazhyanur <varoon>
# @Date:   28-08-2017
# @Filename: track_colorspace.py
# @Last modified by:   varoon
# @Last modified time: 29-08-2017

#GOAL: Track all blue objects on webcam

import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while(True):
    #get frame
    _,frame = capture.read()

    #change color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([240,255,255])

    #threshold to get mask of pixels in blue range
    mask = cv2.inRange(hsv,lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('RESULT',result)
    k=cv2.waitKey(5) & 0xFF
    if(k==27):
        break
cv2.destroyAllWindows()
