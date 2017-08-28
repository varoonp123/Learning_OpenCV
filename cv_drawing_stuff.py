# @Author: Varoon Pazhyanur <varoon>
# @Date:   15-08-2017
# @Filename: cv_drawing_stuff.py
# @Last modified by:   varoon
# @Last modified time: 15-08-2017



import numpy
import cv2

image = numpy.zeros((512,512,3),numpy.uint8)  #create a black image
cv2.line(image, (384,0),(511,511), (255,0,0),5)   #image, start point, stop point, color, thickness
cv2.rectangle(image, (384,0), (510,128),(0,255,0),3)  #Image, top left, bottom right, color, thickness
cv2.circle(image, (477,63),63,(0,0,255),-1) #image, center raduis, color, thickness (-1=filled)
cv2.ellipse(image, (256,256),(100,50),0,0,180,255,-1) #image, center, major axis length, minor axis length, angle (counterclockwise, degrees)

#dray a polygon
points = numpy.array([[10,5],[20,30],[70,20],[50,10]], numpy.int32)
points = points.reshape((-1,1,2))
cv2.polylines(image ,[points],True,(0,255,255)) #true gives closed shape. False joins all points

#Note: Polylines can let you draw lots of lines quickly.

cv2.putText(image, 'OpenCV',(10,500),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),2,cv2.LINE_AA)  #image, text to be written, bottem left coord of where text starts, font type, font scale, color/thickness/linetype/etc.
cv2.imshow('Drawing In OpenCV Example', image)
cv2.waitKey(0)
