# @Author: Varoon Pazhyanur <varoon>
# @Date:   15-08-2017
# @Filename: video_capture.py
# @Last modified by:   varoon
# @Last modified time: 15-08-2017

## Show greyscale video from webcam.

import numpy
import cv2

capture = cv2.VideoCapture(0) #Argument: Device index or name of video file
while(True):
    ret,frame = capture.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', grey)
    if(cv2.waitKey(1) & 0xff==ord('q')):
        break

capture.release()   #Release video capture
cv2.destroyAllWindows()
