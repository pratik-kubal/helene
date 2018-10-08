#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:08:19 2018

@author: pratik
"""
from functions import rgbToGrayscale,genOctave,convolve,genGaussianKernel,differenceGaussians,findMinimaMaxima,ecl_distance
import cv2
import numpy as np

a = cv2.imread("./proj1_cse573/task2.jpg")
b = rgbToGrayscale(a)

scales=[[0.70710678118,1,1.41421356237,2,2.82842712475],
        [1.41421356237,2,2.82842712475,4,5.65685424949],
        [2.82842712475,4,5.65685424949,8,11.313708499],
        [5.65685424949,8,11.313708499,16,22.627416998]]

# genGaussianKernel(scales,octaveNumber,scalesNumber)
octave1 = b.copy()
windowFilter = genGaussianKernel(scales,1,1)
octave1_1 = convolve(windowFilter,octave1)
octave1_1_norm = np.asarray(octave1_1)
cv2.imwrite("octave1_1_norm.jpg",octave1_1_norm)

windowFilter = genGaussianKernel(scales,1,2)
octave1_2 = convolve(windowFilter,octave1)
octave1_2_norm = np.asarray(octave1_2)
cv2.imwrite("octave1_2_norm.jpg",octave1_2_norm)

windowFilter = genGaussianKernel(scales,1,3)
octave1_3 = convolve(windowFilter,octave1)
octave1_3_norm = np.asarray(octave1_3)
cv2.imwrite("octave1_3_norm.jpg",octave1_3_norm)

windowFilter = genGaussianKernel(scales,1,4)
octave1_4 = convolve(windowFilter,octave1)
octave1_4_norm = np.asarray(octave1_4)
cv2.imwrite("octave1_4_norm.jpg",octave1_4_norm)

windowFilter = genGaussianKernel(scales,1,5)
octave1_5 = convolve(windowFilter,octave1)
octave1_5_norm = np.asarray(octave1_5)
cv2.imwrite("octave1_5_norm.jpg",octave1_5_norm)


octave2 = genOctave(octave1)
#octave2_norm = np.asarray(octave2)
#cv2.imwrite("octave2_norm.jpg",octave2_norm)
windowFilter = genGaussianKernel(scales,2,1)
octave2_1 = convolve(windowFilter,octave2)
octave2_1_norm = np.asarray(octave2_1)
cv2.imwrite("octave2_1_norm.jpg",octave2_1_norm)

windowFilter = genGaussianKernel(scales,2,2)
octave2_2 = convolve(windowFilter,octave2)
octave2_2_norm = np.asarray(octave2_2)
cv2.imwrite("octave2_2_norm.jpg",octave2_2_norm)

windowFilter = genGaussianKernel(scales,2,3)
octave2_3 = convolve(windowFilter,octave2)
octave2_3_norm = np.asarray(octave2_3)
cv2.imwrite("octave2_3_norm.jpg",octave2_3_norm)

windowFilter = genGaussianKernel(scales,2,4)
octave2_4 = convolve(windowFilter,octave2)
octave2_4_norm = np.asarray(octave2_4)
cv2.imwrite("octave2_4_norm.jpg",octave2_4_norm)

windowFilter = genGaussianKernel(scales,2,5)
octave2_5 = convolve(windowFilter,octave2)
octave2_5_norm = np.asarray(octave2_5)
cv2.imwrite("octave2_5_norm.jpg",octave2_5_norm)


octave3 = genOctave(octave2)
#octave3_norm = np.asarray(octave3)
#cv2.imwrite("octave3_norm.jpg",octave3_norm)
windowFilter = genGaussianKernel(scales,3,1)
octave3_1 = convolve(windowFilter,octave3)
octave3_1_norm = np.asarray(octave3_1)
cv2.imwrite("octave3_1_norm.jpg",octave3_1_norm)

windowFilter = genGaussianKernel(scales,3,2)
octave3_2 = convolve(windowFilter,octave3)
octave3_2_norm = np.asarray(octave3_2)
cv2.imwrite("octave3_2_norm.jpg",octave3_2_norm)

windowFilter = genGaussianKernel(scales,3,3)
octave3_3 = convolve(windowFilter,octave3)
octave3_3_norm = np.asarray(octave3_3)
cv2.imwrite("octave3_3_norm.jpg",octave3_3_norm)

windowFilter = genGaussianKernel(scales,3,4)
octave3_4 = convolve(windowFilter,octave3)
octave3_4_norm = np.asarray(octave3_4)
cv2.imwrite("octave3_4_norm.jpg",octave3_4_norm)

windowFilter = genGaussianKernel(scales,3,5)
octave3_5 = convolve(windowFilter,octave3)
octave3_5_norm = np.asarray(octave3_5)
cv2.imwrite("octave3_5_norm.jpg",octave3_5_norm)


octave4 = genOctave(octave3)
windowFilter = genGaussianKernel(scales,4,1)
octave4_1 = convolve(windowFilter,octave4)
octave4_1_norm = np.asarray(octave4_1)
cv2.imwrite("octave4_1_norm.jpg",octave4_1_norm)

windowFilter = genGaussianKernel(scales,4,2)
octave4_2 = convolve(windowFilter,octave4)
octave4_2_norm = np.asarray(octave4_2)
cv2.imwrite("octave4_2_norm.jpg",octave4_2_norm)

windowFilter = genGaussianKernel(scales,4,3)
octave4_3 = convolve(windowFilter,octave4)
octave4_3_norm = np.asarray(octave4_3)
cv2.imwrite("octave4_3_norm.jpg",octave4_3_norm)

windowFilter = genGaussianKernel(scales,4,4)
octave4_4 = convolve(windowFilter,octave4)
octave4_4_norm = np.asarray(octave4_4)
cv2.imwrite("octave4_4_norm.jpg",octave4_4_norm)

windowFilter = genGaussianKernel(scales,4,5)
octave4_5 = convolve(windowFilter,octave4)
octave4_5_norm = np.asarray(octave4_5)
cv2.imwrite("octave4_5_norm.jpg",octave4_5_norm)


# Difference of Gaussians
# 2nd arg - 1st arg
dog1_1 = differenceGaussians(octave1_1,octave1_2)
dog1_1_norm = np.asarray(dog1_1)
cv2.imwrite("dog1_1_norm.jpg",dog1_1_norm)

dog1_2 = differenceGaussians(octave1_2,octave1_3)
dog1_2_norm = np.asarray(dog1_2)
cv2.imwrite("dog1_2_norm.jpg",dog1_2_norm)

dog1_3 = differenceGaussians(octave1_3,octave1_4)
dog1_3_norm = np.asarray(dog1_3)
cv2.imwrite("dog1_3_norm.jpg",dog1_3_norm)

dog1_4 = differenceGaussians(octave1_4,octave1_5)
dog1_4_norm = np.asarray(dog1_4)
cv2.imwrite("dog1_4_norm.jpg",dog1_4_norm)

dog2_1 = differenceGaussians(octave2_1,octave2_2)
dog2_1_norm = np.asarray(dog2_1)
cv2.imwrite("dog2_1_norm.jpg",dog2_1_norm)

dog2_2 = differenceGaussians(octave2_2,octave2_3)
dog2_2_norm = np.asarray(dog2_2)
cv2.imwrite("dog2_2_norm.jpg",dog2_2_norm)

dog2_3 = differenceGaussians(octave2_3,octave2_4)
dog2_3_norm = np.asarray(dog2_3)
cv2.imwrite("dog2_3_norm.jpg",dog2_3_norm)

dog2_4 = differenceGaussians(octave2_4,octave2_5)
dog2_4_norm = np.asarray(dog2_4)
cv2.imwrite("dog2_4_norm.jpg",dog2_4_norm)

dog3_1 = differenceGaussians(octave3_1,octave3_2)
dog3_1_norm = np.asarray(dog3_1)
cv2.imwrite("dog3_1_norm.jpg",dog3_1_norm)

dog3_2 = differenceGaussians(octave3_2,octave3_3)
dog3_2_norm = np.asarray(dog3_2)
cv2.imwrite("dog3_2_norm.jpg",dog3_2_norm)

dog3_3 = differenceGaussians(octave3_3,octave3_4)
dog3_3_norm = np.asarray(dog3_3)
cv2.imwrite("dog3_3_norm.jpg",dog3_3_norm)

dog3_4 = differenceGaussians(octave3_4,octave3_5)
dog3_4_norm = np.asarray(dog3_4)
cv2.imwrite("dog3_4_norm.jpg",dog3_4_norm)

dog4_1 = differenceGaussians(octave4_1,octave4_2)
dog4_1_norm = np.asarray(dog4_1)
cv2.imwrite("dog4_1_norm.jpg",dog4_1_norm)

dog4_2 = differenceGaussians(octave4_2,octave4_3)
dog4_2_norm = np.asarray(dog4_2)
cv2.imwrite("dog4_2_norm.jpg",dog4_2_norm)

dog4_3 = differenceGaussians(octave4_3,octave4_4)
dog4_3_norm = np.asarray(dog4_3)
cv2.imwrite("dog4_3_norm.jpg",dog4_3_norm)

dog4_4 = differenceGaussians(octave4_4,octave4_5)
dog4_4_norm = np.asarray(dog4_3)
cv2.imwrite("dog4_4_norm.jpg",dog4_4_norm)


# Key Points detection
outputImage = a.copy()
tracker = [];
stack1_1 = [dog1_3,dog1_2,dog1_1]
keypointsMat1_1 = findMinimaMaxima(stack1_1,outputImage,1,tracker)
stack1_2 = [dog1_2,dog1_3,dog1_4]
keypointsMat1_2 = findMinimaMaxima(stack1_2,outputImage,1,tracker)

stack2_1 = [dog2_1,dog2_2,dog2_3]
keypointsMat2_1 = findMinimaMaxima(stack2_1,outputImage,2,tracker)
stack2_2 = [dog2_2,dog2_3,dog2_4]
keypointsMat2_2 = findMinimaMaxima(stack2_2,outputImage,2,tracker)

stack3_1 = [dog3_1,dog3_2,dog3_3]
keypointsMat2_1 = findMinimaMaxima(stack3_1,outputImage,4,tracker)
stack3_2 = [dog3_2,dog3_3,dog3_4]
keypointsMat3_2 = findMinimaMaxima(stack3_2,outputImage,4,tracker)

stack4_1 = [dog4_1,dog4_2,dog4_3]
keypointsMat2_1 = findMinimaMaxima(stack4_1,outputImage,8,tracker)
stack4_2 = [dog4_2,dog4_3,dog4_4]
keypointsMat4_2 = findMinimaMaxima(stack4_2,outputImage,8,tracker)

cv2.imwrite("keypoints.jpg",outputImage)
ecl_distance_sort = sorted(tracker,key=ecl_distance)
print("Closest five points are:")
print("Format is (Height,Width) or (y,x)")
print(ecl_distance_sort[0:5])


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',np.asarray(normImage(dog2_2)))
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("dog2_2.jpg",np.asarray(normImage(dog2_2))*255)