#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 15:36:26 2018

@author: pratik
"""
from functions import rgbToGrayscale,windowMult,padMat,sliceMat,normImage,getShape,invertMat,combineEdges,sobel
import numpy as np
import cv2

# Reading the Image
a = cv2.imread("./proj1_cse573/task1.png")
b = rgbToGrayscale(a)

# Define Operators
sobel_op_x = [[1,0,-1],
              [2,0,-2],
              [1,0,-1]]
sobel_op_y = [[-1,-2,-1],
              [0,0,0],
              [1,2,1]]

# Sobel Edges in x
edge_x = sobel(b,invertMat(sobel_op_x))
# Converting the image to display and write using cv libraries
edge_x_norm = np.asarray(edge_x)
edge_x_norm = edge_x_norm * 255
edge_x_norm = edge_x_norm.astype('uint8')
print("Writing edge_x.jpg")
cv2.imwrite("edge_x.jpg",edge_x_norm)

# Sobel Edges in y
edge_y = sobel(b,invertMat(sobel_op_y))
# Converting the image to display and write using cv libraries
edge_y_norm = np.asarray(edge_y)
edge_y_norm = edge_y_norm * 255
edge_y_norm = edge_y_norm.astype('uint8')
print("Writing edge_y.jpg")
cv2.imwrite("edge_y.jpg",edge_y_norm)

# Combining edge detection in x and y
combined = combineEdges(edge_x,edge_y)
# Converting the image to display and write using cv libraries
combined_norm = np.asarray(combined)
combined_norm = combined_norm * 255
combined_norm = combined_norm.astype('uint8')
print("Writing combined.jpg")
cv2.imwrite("combined.jpg",combined_norm)

print("Original image size: {:4d} x {:4d}".format(a.shape[0], a.shape[1]))
print("Resulting image size: {:4d} x {:4d}".format(combined_norm.shape[0], combined_norm.shape[1]))