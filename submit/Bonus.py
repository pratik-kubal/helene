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
# t1, t1_2,t1_3,t1_4,5,6 failed
img = cv2.imread('./proj1_cse573/task3_bonus/t1_6.jpg')
template = cv2.imread('./proj1_cse573/task3_bonus/t1_v2.jpg')
template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

(val,(temph,tempw),(x,y)) = matchTemplate(gray,template)
print(val)
cv2.rectangle(img,(x, y),(x+temph, y+tempw),(255,0,0),2)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# t2 works
img = cv2.imread('./proj1_cse573/task3_bonus/t2_6.jpg')
template = cv2.imread('./proj1_cse573/task3_bonus/t2.jpg')
template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

(val,(temph,tempw),(x,y)) = matchTemplate(gray,template)
print(val)
cv2.rectangle(img,(x, y),(x+temph, y+tempw),(255,0,0),2)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# t3 needs improvements
img = cv2.imread('./proj1_cse573/task3_bonus/t3_5.jpg')
template = cv2.imread('./proj1_cse573/task3_bonus/t3_v2.jpg')
template = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

(val,(temph,tempw),(x,y)) = matchTemplate(gray,template)
print(val)
cv2.rectangle(img,(x, y),(x+temph, y+tempw),(255,0,0),2)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()