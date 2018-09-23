#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 15:36:26 2018

@author: pratik
"""

import cv2

def rgbToGrayscale(image):
    # https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
    r,g,b = image[:,:,0],image[:,:,1],image[:,:,2]
    grayscaleImage =  0.299*r + 0.587*g + 0.114* b
    # Normalize Grayscale
    grayscaleImage = grayscaleImage / 255
    return grayscaleImage

a = cv2.imread("proj1_cse573/task1.png")


b = rgbToGrayscale(a)
print(b)
type(b)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', b)
cv2.waitKey(0)
cv2.destroyAllWindows()