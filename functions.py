#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 00:48:24 2018

@author: pratik
"""

def rgbToGrayscale(image):
    # https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
    r,g,b = image[:,:,0],image[:,:,1],image[:,:,2]
    grayscaleImage =  0.299*r + 0.587*g + 0.114*b
    # Normalize Grayscale
    #grayscaleImage = grayscaleImage / 255
    return grayscaleImage

def windowMult(matA,matB):
    matResult = 0
    for x_iter in range(0,3):
        for y_iter in range(0,3):
            if not len(matA) or not len(matB) == 0:
                matResult += matA[x_iter][y_iter] * matB[x_iter][y_iter]
    return matResult

def padMat(matA):
    skeleton=[[] for i in range(0,602)]
    for window_h in range(0,602):
        for window_w in range(0,902):
            if(window_h == 0 or window_h == 601):
                skeleton[window_h].append(0)
            else:
                if(window_w == 0 or window_w == 901):
                    skeleton[window_h].append(0)
                else:
                    skeleton[window_h].append(matA[window_h-1][window_w-1])
    return skeleton

def sliceMat(matrix,window_h_start,window_h_stop,window_w_start,window_w_stop):
    retMat = matrix[window_h_start:window_h_stop]
    holdWindow = []
    #retMat = [[]for i in range(len(retMat))]
    for i in range(0,len(retMat)):
        #print(holdWindow[i])
        holdWindow.append(retMat[i][window_w_start:window_w_stop])
    return holdWindow