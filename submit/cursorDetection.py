#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:34:47 2018

@author: pratik
"""

import cv2
import numpy as np
import imutils
from functions import matchTemplate

img = cv2.imread('./proj1_cse573/task3/pos_6.jpg')
template = cv2.imread('./proj1_cse573/task3/green_template.jpg')
template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
(val,(temph,tempw),(x,y)) = matchTemplate(gray,template)
cv2.rectangle(img,(x, y),(x+temph, y+tempw),(255,0,0),2)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


logan=matchTemplateAdv(gray,template)

cv.G

gaussian1 = cv2.GaussianBlur(gray,(3,3),3)
lap = cv2.Laplacian(gray,ddepth=8,ksize = 3)
lapTemplate = cv2.Laplacian(template,ddepth=32,ksize=3)
#lapTemplate= cv2.dilate(lapTemplate,(3,5),iterations = 3)

lapTemplate = imutils.resize(lapTemplate,int(lapTemplate.shape[1]*0.65))
    
a = cv2.matchTemplate(lap,lapTemplate,cv2.TM_CCOEFF_NORMED)
b = cv2.minMaxLoc(a)
(_,_,_,(xval,yval)) = b
cv2.rectangle(gray,(338, 482),(338+2, 482+2),(255,0,0),2)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

canyTemplate_small = imutils.resize(canyTemplate,int(canyTemplate.shape[1]*0.8))

a = cv2.matchTemplate(cany,canyTemplate_small,cv2.TM_CCORR_NORMED)
cany = cv2.Canny(gaussian1,100,700)
b = cv2.minMaxLoc(a)
(_,_,_,(xval,yval)) = b
cv2.rectangle(cany,(xval, yval),(xval+np.shape(canyTemplate_small)[0], yval+np.shape(canyTemplate_small)[1]),(255,0,0),2)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',cany)
cv2.waitKey(0)
cv2.destroyAllWindows()

canyTemplate_small_small = imutils.resize(canyTemplate,int(canyTemplate.shape[1]*0.6))
cany = cv2.Canny(gaussian1,100,700)
a = cv2.matchTemplate(cany,canyTemplate_small_small,cv2.TM_CCORR_NORMED)
b = cv2.minMaxLoc(a)
(_,_,_,(xval,yval)) = b
cv2.rectangle(cany,(xval, yval),(xval+np.shape(canyTemplate_small_small)[0], yval+np.shape(canyTemplate_small_small)[1]),(255,0,0),2)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',cany)
cv2.waitKey(0)
cv2.destroyAllWindows()

canyTemplate_small_small_small = imutils.resize(canyTemplate,int(canyTemplate.shape[1]*0.4))
cany = cv2.Canny(gaussian1,10,700)
a = cv2.matchTemplate(cany,canyTemplate_small_small_small,cv2.TM_CCORR_NORMED)
b = cv2.minMaxLoc(a)
(_,_,_,(xval,yval)) = b
cv2.rectangle(cany,(xval, yval),(xval+np.shape(canyTemplate_small_small_small)[0], yval+np.shape(canyTemplate_small_small_small)[1]),(255,0,0),2)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',cany)
cv2.waitKey(0)
cv2.destroyAllWindows()


canyTemplate_small_small_small = imutils.resize(canyTemplate,int(canyTemplate.shape[1]*0.2))
cany = cv2.Canny(gray,500,700)
a = cv2.matchTemplate(cany,canyTemplate_small_small_small,cv2.TM_CCORR_NORMED)
b = cv2.minMaxLoc(a)
(_,_,_,(xval,yval)) = b
cv2.rectangle(cany,(xval, yval),(xval+np.shape(canyTemplate_small_small_small)[0], yval+np.shape(canyTemplate_small_small_small)[1]),(255,0,0),2)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',cany)
cv2.waitKey(0)
cv2.destroyAllWindows()


