# @Author: Varoon Pazhyanur <varoon>
# @Date:   18-08-2017
# @Filename: kernel_convolution_ex.py
# @Last modified by:   varoon
# @Last modified time: 18-08-2017



import cv2
import numpy as np

#GOAL: Apply the following kernel convolution to an image: [-1,0,1||-1,5,-1||0,-1,0]
#applying a sharpening kernel convolution manually. Bad way.
def sharpen(image):
    image = cv2.cvtColor(image, c2.CV_8U)
    height, width, num_channels = image.shape
    result = np.zeros(image.shape, image.dtype)
    for i in range(1,height-1):
        for j in range(1,width-1):
            for k in range(0,num_channels):
                sum = 5*image[i,j,k] - image[i+1, j, k]\
                    -image[i-1,j,k] - image[i,j+1,k] - image[i,j-1,k]

                if(sum>255):
                    sum = 255
                if(sum<0):
                    sum=0
                result[i,j,k] = sum
    return result


#THE EASY WAY:
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32) #KERNEL NEEDS TO BE A FLOAT MATRIX

res = cv2.filter2D(I,-1,kernel) #ddepth = -1 means res image has same depth as I
