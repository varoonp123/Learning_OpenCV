# @Author: Varoon Pazhyanur <varoon>
# @Date:   28-08-2017
# @Filename: image_combine.py
# @Last modified by:   varoon
# @Last modified time: 28-08-2017



import cv2
import numpy as np

#GOAL: put the opencv logo on an image and make it opaque(rather than transparent)
messi = cv2.imread("messi5.jpg")
cv_logo = cv2.imread("opencv-logo.png")

rows,cols,channels = cv_logo.shape
roi = messi[0:rows, 0:cols]   #going to put logo in top left

#using a mask because the CV logo is not a rectangle. Find pixels of interest with threshold.
cv_logo_grey = cv2.cvtColor(cv_logo, cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(cv_logo_grey,10,255,cv2.THRESH_BINARY) #THRESHOLD IMAGE
mask_inv = cv2.bitwise_not(mask)

messi_bg=cv2.bitwise_and(roi,roi,mask = mask_inv)

cv_logo_fg = cv2.bitwise_and(cv_logo,cv_logo,mask=mask)
cv2.imshow("test",mask)
res = cv2.add(messi_bg, cv_logo_fg)
messi[0:rows, 0:cols] = res

cv2.imshow("Messi and CV Logo", messi)
cv2.waitKey(0)
cv2.destroyAllWindows()
