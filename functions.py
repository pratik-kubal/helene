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
    for i in range(0,len(retMat)):
        holdWindow.append(retMat[i][window_w_start:window_w_stop])
    return holdWindow

def normImage(matA):
    skeleton=[[] for i in range(0,600)]
    maxValue = 0
    absValue = 0
    for window_h in range(0,600):
        for window_w in range(0,900):
            absValue = abs(matA[window_h][window_w])
            skeleton[window_h].append(absValue)     
            if(maxValue < absValue) : maxValue = absValue
    returnMat=[[] for i in range(0,600)]
    for window_h in range(0,600):
        for window_w in range(0,900):
            returnMat[window_h].append(skeleton[window_h][window_w] / maxValue)
    return returnMat

def getShape(matA):
    height = len(matA)
    width = len(matA[1])
    for i in range(0,height):
        if(len(matA[i]) != width):
            return -1
        else:
            return (height,width)

def invertMat(matA):
    skeleton=[[] for i in range(0,getShape(matA)[0])]
    i = 0
    for window_h in range(getShape(matA)[0]-1,-1,-1):
        for window_w in range(getShape(matA)[1]-1,-1,-1):
            skeleton[i].append(matA[window_h][window_w])
        i += 1
    return skeleton 
    
    