#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 20:28:52 2018

@author: pratik
"""

import cv2
import numpy as np
import imutils
from functions import matchTemplate
import glob, os
# t1, t1_2,t1_3,t1_4,5,6 failed
#
import glob, os
template = cv2.imread('./proj1_cse573/task3_bonus/t1.jpg')
template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
for file in glob.glob("./proj1_cse573/task3_bonus/t1_*.jpg"):
    img = cv2.imread(file)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    (val,(temph,tempw),(x,y)) = matchTemplate(gray,template)
    if(val > 0.5):
        cv2.rectangle(img,(x, y),(x+temph, y+tempw),(255,0,0),2)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


(val,(temph,tempw),(x,y)) = matchTemplate(gray,template)
print(val)
cv2.rectangle(img,(x, y),(x+temph, y+tempw),(255,0,0),2)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# t2 works
template = cv2.imread('./proj1_cse573/task3_bonus/t2.jpg')
template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
for file in glob.glob("./proj1_cse573/task3_bonus/t2_*.jpg"):
    img = cv2.imread(file)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    (val,(temph,tempw),(x,y)) = matchTemplate(gray,template)
    if(val > 0.6):
        cv2.rectangle(img,(x, y),(x+temph, y+tempw),(255,0,0),2)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# t3 needs improvements
template = cv2.imread('./proj1_cse573/task3_bonus/t3_v2.jpg')
template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
for file in glob.glob("./proj1_cse573/task3_bonus/t3_*.jpg"):
    img = cv2.imread(file)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    (val,(temph,tempw),(x,y)) = matchTemplate(gray,template)
    if(val > 0.6):
        cv2.rectangle(img,(x, y),(x+temph, y+tempw),(255,0,0),2)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

(val,(temph,tempw),(x,y)) = matchTemplate(gray,template)
print(val)
cv2.rectangle(img,(x, y),(x+temph, y+tempw),(255,0,0),2)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()