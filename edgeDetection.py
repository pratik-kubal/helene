#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 15:36:26 2018

@author: pratik
TO DO:
    Need to check if the window is using pad digits or not
    Nomalize the black values
"""
from functions.py import rgbToGrayscale,sliceMat,windowMult
import numpy as np
import cv2

a = cv2.imread("./proj1_cse573/task1.png")
b = rgbToGrayscale(a)

#def normNeg(matA):

sobel_op_x = [[-1,0,1],
              [-2,0,2],
              [1,0,-1]]
sobel_op_y = [[-1,-2,-1],
              [0,0,0],
              [1,2,1]]

resultImage = [[]for i in range(602-3)]
for window_h in range(0,602-3):
    holdRow = []
    for window_w in range(0,902-3):
        #print(window_h,window_w)
        window = sliceMat(b,window_h,window_h+3,window_w,window_w+3)
        #print("Line:" + str(window_h))
        opResult = windowMult(sobel_op_x,window)
        #if(opResult < 0): opResult = 0
        resultImage[window_h].append(opResult)
        
for window_h in range(0,600-1-3):
    holdRow = []
    for window_w in range(0,900-1-3):
        #print(window_h,window_w)
        window = b[window_h:window_h+3,window_w:window_w+3]
        #print("Line:" + str(window_h))
        opResult = windowMult(sobel_op_y,window)
        #if(opResult < 0): opResult = 0
        resultImage[window_h].append(opResult)

display = np.asarray(resultImage)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', display)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Check
a = cv2.imread("./proj1_cse573/task1.png",0)
# Computing vertical edges
edge_x = cv2.Sobel(a, cv2.CV_32F, 1, 0, ksize=3)
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