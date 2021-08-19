#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np


#Reading Images
img1 = cv2.imread("scrambled1.png")
img2 = cv2.imread("scrambled2.png")

print(img1.shape)
print(img2.shape)


"""

The following function basically is an operation that will be performed on
the corresponding pixels of the given images.

What does this function do?
It takes two linear arrays each of three elements adding them essentially 
flipping one of them and returning a linear array of 3 elements

"""
def decrypt(x, y):
    return np.array([x[0]+y[2],x[1]+y[1],x[2]+y[0]])


"""
We are creating an array of the same the size as of the given images.

Corresponding pixels of both images are taken and decrypt function defined 
above is performed on them and pasted over the corresponding pixel of the answer image.
"""
arr = np.zeros((256, 256, 3), dtype='uint8') #answer to be stored in this image array  

for i in range(256):
    for j in range(256):
        arr[i, j] = decrypt(img1[i, j, :], img2[i, j, :])


#Below 3 lines of code is to show the answer image using opencv window

cv2.imshow('answer image', arr)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows()


#Uncoment the following line to save the answer image 

# cv2.imwrite('answer.png', arr)
