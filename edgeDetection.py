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
            if not len(matA) or not len(matB) == 0:
                matResult += matA[x_iter][y_iter] * matB[x_iter][y_iter]
    return matResult

sobel_op_x = [[-1,0,1],
              [-2,0,2],
              [1,0,-1]]
sobel_op_y = [[-1,-2,-1],
              [0,0,0],
              [1,2,1]]

resultImage = [[]for i in range(600-1-3)]
for window_h in range(0,600-1-3):
    holdRow = []
    for window_w in range(0,900-1-3):
        #print(window_h,window_w)
        window = b[window_h:window_h+3,window_w:window_w+3]
        #print("Line:" + str(window_h))
        opResult = matMult(sobel_op_x,window)
        if(opResult < 0): opResult = 0
        resultImage[window_h].append(opResult)
        
for window_h in range(0,600-1-3):
    holdRow = []
    for window_w in range(0,900-1-3):
        #print(window_h,window_w)
        window = b[window_h:window_h+3,window_w:window_w+3]
        #print("Line:" + str(window_h))
        opResult = matMult(sobel_op_y,window)
        if(opResult < 0): opResult = 0
        resultImage[window_h].append(opResult)


import numpy as np
display = np.asarray(resultImage)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', display)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Check
a = cv2.imread("./proj1_cse573/task1.png",0)
# Computing vertical edges
edge_x = cv2.Sobel(b, cv2.CV_32F, 1, 0, ksize=3)
cv2.namedWindow('edge_x_dir', cv2.WINDOW_NORMAL)
cv2.imshow('edge_x_dir', edge_x)
cv2.waitKey(0)
cv2.destroyAllWindows()
import numpy as np
pos_edge_x = (edge_x - np.min(edge_x)) / (np.max(edge_x) - np.min(edge_x))
cv2.namedWindow('pos_edge_x_dir', cv2.WINDOW_NORMAL)
cv2.imshow('pos_edge_x_dir', pos_edge_x)
cv2.waitKey(0)
cv2.destroyAllWindows()
pos_edge_x = np.abs(edge_x) / np.max(np.abs(edge_x))
cv2.namedWindow('pos_edge_x_dir', cv2.WINDOW_NORMAL)
cv2.imshow('pos_edge_x_dir', pos_edge_x)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Computing horizontal edges
edge_y = cv2.Sobel(a, cv2.CV_32F, 0, 1, ksize=3)
cv2.namedWindow('edge_y_dir', cv2.WINDOW_NORMAL)
cv2.imshow('edge_y_dir', edge_y)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Eliminate zero values with method 2
pos_edge_y = np.abs(edge_y) / np.max(np.abs(edge_y))
cv2.namedWindow('pos_edge_y_dir', cv2.WINDOW_NORMAL)
cv2.imshow('pos_edge_y_dir', pos_edge_y)
cv2.waitKey(0)
cv2.destroyAllWindows()