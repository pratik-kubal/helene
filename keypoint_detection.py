#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:08:19 2018

@author: pratik
"""
from functions import rgbToGrayscale,getShape,normImage,genOctave,convolve,genGaussianKernel,invertMat,differenceGaussians,findMinimaMaxima
import cv2
import numpy as np

a = cv2.imread("./proj1_cse573/task2.jpg")
b = rgbToGrayscale(a)

scales=[[0.70710678118,1,1.41421356237,2,2.82842712475],
        [1.41421356237,2,2.82842712475,4,5.65685424949],
        [2.82842712475,4,5.65685424949,8,11.313708499],
        [5.65685424949,8,11.313708499,16,22.627416998]]

# genGaussianKernel(scales,octaveNumber,scalesNumber)
octave1 = b
windowFilter = genGaussianKernel(scales,1,1)
octave1_1 = convolve(windowFilter,octave1)
windowFilter = genGaussianKernel(scales,1,2)
octave1_2 = convolve(windowFilter,b)
windowFilter = genGaussianKernel(scales,1,3)
octave1_3 = convolve(windowFilter,b)
windowFilter = genGaussianKernel(scales,1,4)
octave1_4 = convolve(windowFilter,b)
windowFilter = genGaussianKernel(scales,1,5)
octave1_5 = convolve(windowFilter,b)

octave2 = genOctave(b)
windowFilter = genGaussianKernel(scales,2,1)
octave2_1 = convolve(windowFilter,octave2)
windowFilter = genGaussianKernel(scales,2,2)
octave2_2 = convolve(windowFilter,octave2)
windowFilter = genGaussianKernel(scales,2,3)
octave2_3 = convolve(windowFilter,octave2)
windowFilter = genGaussianKernel(scales,2,4)
octave2_4 = convolve(windowFilter,octave2)
windowFilter = genGaussianKernel(scales,2,5)
octave2_5 = convolve(windowFilter,octave2)

octave3 = genOctave(octave2)
windowFilter = genGaussianKernel(scales,3,1)
octave3_1 = convolve(windowFilter,octave3)
windowFilter = genGaussianKernel(scales,3,2)
octave3_2 = convolve(windowFilter,octave3)
windowFilter = genGaussianKernel(scales,3,3)
octave3_3 = convolve(windowFilter,octave3)
windowFilter = genGaussianKernel(scales,3,4)
octave3_4 = convolve(windowFilter,octave3)
windowFilter = genGaussianKernel(scales,3,5)
octave3_5 = convolve(windowFilter,octave3)

octave4 = genOctave(octave3)
windowFilter = genGaussianKernel(scales,4,1)
octave4_1 = convolve(windowFilter,octave4)
windowFilter = genGaussianKernel(scales,4,2)
octave4_2 = convolve(windowFilter,octave4)
windowFilter = genGaussianKernel(scales,4,3)
octave4_3 = convolve(windowFilter,octave4)
windowFilter = genGaussianKernel(scales,4,4)
octave4_4 = convolve(windowFilter,octave4)
windowFilter = genGaussianKernel(scales,4,5)
octave4_5 = convolve(windowFilter,octave4)

# Difference of Gaussians
# 2nd arg - 1st arg
dog1_1 = differenceGaussians(octave1_1,octave1_2)
dog1_2 = differenceGaussians(octave1_2,octave1_3)
dog1_3 = differenceGaussians(octave1_3,octave1_4)
dog1_4 = differenceGaussians(octave1_4,octave1_5)

dog2_1 = differenceGaussians(octave2_1,octave2_2)
dog2_2 = differenceGaussians(octave2_2,octave2_3)
dog2_3 = differenceGaussians(octave2_3,octave2_4)
dog2_4 = differenceGaussians(octave2_4,octave2_5)

dog3_1 = differenceGaussians(octave3_1,octave3_2)
dog3_2 = differenceGaussians(octave3_2,octave3_3)
dog3_3 = differenceGaussians(octave3_3,octave3_4)
dog3_4 = differenceGaussians(octave3_4,octave3_5)

dog4_1 = differenceGaussians(octave4_1,octave4_2)
dog4_2 = differenceGaussians(octave4_2,octave4_3)
dog4_3 = differenceGaussians(octave4_3,octave4_4)
dog4_4 = differenceGaussians(octave4_4,octave4_5)

# Key Points detection
stack1_1 = [dog1_1,dog1_2,dog1_3]
keypointsMat1_1 = findMinimaMaxima(stack1_1,octave1,1)
stack1_2 = [dog1_2,dog1_3,dog1_4]
keypointsMat1_2 = findMinimaMaxima(stack1_2,octave1,1)

stack2_1 = [dog2_1,dog2_2,dog2_3]
keypointsMat2_1 = findMinimaMaxima(stack2_1,octave2,2)
stack2_2 = [dog2_2,dog2_3,dog2_4]
keypointsMat2_2 = findMinimaMaxima(stack2_2,octave2,2)

stack3_1 = [dog3_1,dog3_2,dog3_3]
keypointsMat2_1 = findMinimaMaxima(stack3_1,octave3,2)
stack3_2 = [dog3_2,dog3_3,dog3_4]
keypointsMat3_2 = findMinimaMaxima(stack3_2,octave3,2)

stack4_1 = [dog4_1,dog4_2,dog4_3]
keypointsMat2_1 = findMinimaMaxima(stack4_1,octave4,2)
stack4_2 = [dog4_2,dog4_3,dog4_4]
keypointsMat4_2 = findMinimaMaxima(stack4_2,octave4,2)

normImg = normImage(keypointsMat1_1)
display = np.asarray(normImg)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', display)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("image.png",keypointsMat1_1)
display = np.asarray(normImage(b))
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', display)
cv2.waitKey(0)
cv2.destroyAllWindows()