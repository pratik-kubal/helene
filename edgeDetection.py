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
    grayscaleImage =  0.299*r + 0.587*g + 0.114*b
    # Normalize Grayscale
    grayscaleImage = grayscaleImage / 255
    return grayscaleImage

a = cv2.imread("./proj1_cse573/task1.png")
b = rgbToGrayscale(a)

def matMult(matA,matB):
    matResult = 0
    for x_iter in range(0,3):
        for y_iter in range(0,3):
            matResult += sobel_op_x[x_iter][y_iter] * matB[x_iter][y_iter]
    return matResult

sobel_op_x = [[1,0,-1],
              [2,0,-2],
              [1,0,-1]]
sobel_op_y = [[1,2,1],
              [0,0,0],
              [-1,-2,-1]]

for window_w in range(0,600):
    for window_h in range(0,900):
        window = b[0:3,0:3]

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', b)
cv2.waitKey(0)
cv2.destroyAllWindows()