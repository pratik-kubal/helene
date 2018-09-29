#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 15:36:26 2018

@author: pratik
TO DO:
    Need to check if the window is using pad digits or not
    Nomalize the black values
"""
from functions import rgbToGrayscale,windowMult,padMat,sliceMat,normImage,getShape,invertMat
import numpy as np
import cv2

a = cv2.imread("./proj1_cse573/task1.png")
b = rgbToGrayscale(a)

sobel_op_x = [[1,0,-1],
              [2,0,-2],
              [1,0,-1]]
sobel_op_y = [[-1,-2,-1],
              [0,0,0],
              [1,2,1]]

def sobel(matA,sobel_op):
    matA = padMat(matA)
    resultImage = [[]for i in range(600)]
    for window_h in range(0,getShape(matA)[0]-2):
        for window_w in range(0,getShape(matA)[1]-2):
            window = sliceMat(matA,window_h,window_h+3,window_w,window_w+3)
            opResult = windowMult(sobel_op,window)
            resultImage[window_h].append(opResult)
    resultImage = normImage(resultImage)
    return resultImage

edge_x = sobel(b,invertMat(sobel_op_x))
edge_y = sobel(b,invertMat(sobel_op_y))

display = np.asarray(edge_y)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', display)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Compare
# Check
img = cv2.imread("./proj1_cse573/task1.png",0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite()

# Computing vertical edges
edge_x = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
cv2.namedWindow('edge_x_dir', cv2.WINDOW_NORMAL)
cv2.imshow('edge_x_dir', edge_x)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Eliminate zero values with method 2
pos_edge_x = np.abs(edge_x) / np.max(np.abs(edge_x))
cv2.namedWindow('pos_edge_x_dir', cv2.WINDOW_NORMAL)
cv2.imshow('pos_edge_x_dir', pos_edge_x)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Computing horizontal edges
edge_y = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)
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

# magnitude of edges (conbining horizontal and vertical edges)
edge_magnitude = np.sqrt(edge_x ** 2 + edge_y ** 2)
edge_magnitude /= np.max(edge_magnitude)
cv2.namedWindow('edge_magnitude', cv2.WINDOW_NORMAL)
cv2.imshow('edge_magnitude', edge_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()

edge_direction = np.arctan(edge_y / (edge_x + 1e-3))
edge_direction = edge_direction * 180. / np.pi
edge_direction /= np.max(edge_direction)
cv2.namedWindow('edge_direction', cv2.WINDOW_NORMAL)
cv2.imshow('edge_direction', edge_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Original image size: {:4d} x {:4d}".format(img.shape[0], img.shape[1]))
print("Resulting image size: {:4d} x {:4d}".format(edge_magnitude.shape[0], edge_magnitude.shape[1]))