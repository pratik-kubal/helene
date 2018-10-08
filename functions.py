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
    for x_iter in range(0,getShape(matA)[0]):
        for y_iter in range(0,getShape(matA)[0]):
            if not len(matA) or not len(matB) == 0:
                matResult += matA[x_iter][y_iter] * matB[x_iter][y_iter]
    return matResult

def padMat(matA,sizeWindow):
    space = (int)(sizeWindow/2)
    skeleton=[[] for i in range(0,(getShape(matA)[0]+4))]
    for window_h in range(0,getShape(matA)[0]+4):
        for window_w in range(0,getShape(matA)[1]+4):
            if(window_h >= 0 and window_h <= (space-1)) or (window_h > getShape(matA)[0]):
                skeleton[window_h].append(0)
            else:
                if(window_w >= 0 and window_w < 3) or (window_w > getShape(matA)[1] ):
                    #print("wpad")
                    #print(window_w)
                    skeleton[window_h].append(0)
                else:
                        skeleton[window_h].append(matA[window_h-(3)][window_w-(3)])
    return skeleton

#def padMat(matA,sizeWindow):
#    #space = (int)(sizeWindow/2)
#    skeleton=[[] for i in range(0,(getShape(matA)[0]+6))]
#    for window_h in range(0,getShape(matA)[0]+6):
#        for window_w in range(0,getShape(matA)[1]+6):
#            if(window_h >= 0 and window_h <= 2) or (window_h >460 and window_h <= 463 ):
#                
#                skeleton[window_h].append(0)
#            else:
#                if(window_w >= 0 and window_w <= 2) or (window_w > 752 and window_w <= 756):
#                    #print("wpad")
#                    #print(window_w)
#                    skeleton[window_h].append(0)
#                else:
#                    skeleton[window_h].append(matA[window_h-(3)][window_w-(3)])
#    return skeleton

def sliceMat(matrix,window_h_start,window_h_stop,window_w_start,window_w_stop):
    retMat = matrix[window_h_start:window_h_stop]
    holdWindow = []
    for i in range(0,len(retMat)):
        holdWindow.append(retMat[i][window_w_start:window_w_stop])
    return holdWindow

def normImage(matA):
    from functions import getShape
    skeleton=[[] for i in range(0,getShape(matA)[0])]
    maxValue = 0
    absValue = 0
    for window_h in range(0,getShape(matA)[0]):
        for window_w in range(0,getShape(matA)[1]):
            absValue = abs(matA[window_h][window_w])
            skeleton[window_h].append(absValue)     
            if(maxValue < absValue) : maxValue = absValue
    returnMat=[[] for i in range(0,getShape(matA)[0])]
    for window_h in range(0,getShape(matA)[0]):
        for window_w in range(0,getShape(matA)[1]):
            returnMat[window_h].append(skeleton[window_h][window_w] / maxValue)
    return returnMat

def getShape(matA):
    height = len(matA)
    width = len(matA[1])
    for i in range(0,height):
        if(len(matA[i]) != width):
            return -i
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

def sobel(matA,sobel_op):
    matA = padMat(matA,3)
    resultImage = [[]for i in range(600)]
    for window_h in range(0,getShape(matA)[0]-2):
        for window_w in range(0,getShape(matA)[1]-2):
            window = sliceMat(matA,window_h,window_h+3,window_w,window_w+3)
            opResult = windowMult(sobel_op,window)
            resultImage[window_h].append(opResult)
    resultImage = normImage(resultImage)
    return resultImage

def combineEdges(matA,matB):
    from math import sqrt
    maxValue = 0
    skeleton = [[] for i in range(0,getShape(matA)[0])]
    for window_h in range(0,getShape(matA)[0]):
        for window_w in range(0,getShape(matA)[1]):
            skeleton[window_h].append(sqrt(matA[window_h][window_w]**2 + matB[window_h][window_w]**2))
    for window_h in range(0,getShape(skeleton)[0]):
        for window_w in range(0,getShape(skeleton)[1]):
            if(skeleton[window_h][window_w]>maxValue): maxValue = skeleton[window_h][window_w]
    for window_h in range(0,getShape(skeleton)[0]):
        for window_w in range(0,getShape(skeleton)[1]):
            skeleton[window_h][window_w] = skeleton[window_h][window_w]/maxValue
    return skeleton

def genOctave(matA):
    #print(getShape(matA));
    skeleton = [[] for i in range(0,(int)(getShape(matA)[0]/2))]
    for window_h in range(0,getShape(matA)[0]):
        for window_w in range(0,getShape(matA)[1]):
            if(window_h % 2 ==0 and window_w % 2 == 0):
                sampleIndex = (int)(window_h / 2)
                if(sampleIndex < (int)(getShape(matA)[0]/2)):
                    skeleton[sampleIndex].append(matA[window_h][window_w])
    return(skeleton)

def genGaussianVal(xval,yval,sigma):
    import math
    sigma = sigma**2
    return (1/(2*math.pi*sigma))*(math.exp(-((xval**2+yval**2)/(2*sigma))))

def summession2d(matA):
    summession = 0
    for window_h in range(0,getShape(matA)[0]):
        for window_w in range(0,getShape(matA)[1]):
            summession += matA[window_h][window_w]
    return summession

def genGaussianKernel(scales,octaveNumber,scalesNumber):
    from functions import genGaussianVal,summession2d
    gaussianKernel = [[] for i in range(0,7)]
    scalesStack = scales[octaveNumber-1]
    sigma = scalesStack[scalesNumber-1]
    i = 0
    for y in range(3,-4,-1):
        for x in range(-3,4,1):
            gaussianKernel[i].append(genGaussianVal(x,y,sigma))
        i+=1
    constant = summession2d(gaussianKernel)
    constant = 1/constant
    for y in range(0,7):
        for x in range(0,7):
            gaussianKernel[y][x] = constant*gaussianKernel[y][x] 
    return gaussianKernel

def convolve(windowFilter,matA):
    from functions import invertMat,getShape,sliceMat,padMat,windowMult
    windowFilter = invertMat(windowFilter)
    matA = padMat(matA,getShape(windowFilter)[0])
    #print(getShape(matA))
    resultImage = [[] for i in range(0,getShape(matA)[0] - int(getShape(windowFilter)[0] / 2) -1 )]
    for window_h in range(0,getShape(matA)[0]):
        for window_w in range(0,getShape(matA)[1]):
            if(window_h > 2 and window_h <= (getShape(matA)[0]) -4) and (window_w > 2 and window_w < (getShape(matA)[1]-3)):
                window = sliceMat(matA,window_h-3,window_h+4,window_w-3,window_w+4)
                #print(getShape(window))
                opResult = windowMult(windowFilter,window)
                resultImage[window_h-3].append(opResult)
    return resultImage

def convolveSSJ4(windowFilter,matA):
    from functions import invertMat,getShape,sliceMat,padMat,windowMult
    windowFilter = invertMat(windowFilter)
    matA = padMat(matA,getShape(windowFilter)[0])
    #print(getShape(matA))
    resultImage = [[] for i in range(0,(getShape(matA))[0] + 6)]
    for window_h in range(0,getShape(matA)[0]+6):
        for window_w in range(0,getShape(matA)[1]+6):
            window = sliceMat(matA,window_h,window_h+7,window_w,window_w+7)
            #print(getShape(window))
            opResult = windowMult(windowFilter,window)
            resultImage[window_h].append(opResult)
    return resultImage


def differenceGaussians(matA,matB):
    if(getShape(matA) == getShape(matB)):
        skeleton = [[] for i in range(0,getShape(matA)[0])]
        for window_h in range(0,getShape(matA)[0]):
            for window_w in range(0,getShape(matB)[1]):
                difference = matB[window_h][window_w] - matA[window_h][window_w]
                skeleton[window_h].append(difference)
        return skeleton
    else:
        return -1
    
def isMinima(dogslice,center,isMid):
    counter=0
    if(not isMid):
        for window_h in range(0,3):
            for window_w in range(0,3):
                if dogslice[window_h][window_w] > center:
                    counter +=1
        if(counter == 9):
            return True
        else:
            return False
    else:
        for window_h in range(0,3):
            for window_w in range(0,3):
                if(window_h != 1 or window_w != 1):
                    if (dogslice[window_h][window_w] > center):
                        counter +=1
        if(counter == 8):
            return True
        else:
            return False
        
def isMaxima(dogslice,center,isMid):
    counter = 0
    if(not isMid):
        for window_h in range(0,3):
            for window_w in range(0,3):
                if dogslice[window_h][window_w] < center:
                    counter += 1
        if(counter == 9):
            return True
        else:
            return False
    else:
        for window_h in range(0,3):
            for window_w in range(0,3):
                if window_h != 1 or window_w != 1 :
                    val = dogslice[window_h][window_w]
                    if val < center:
                        counter +=1
        if(counter == 8):
            return True
        else:
            return False

def findMinimaMaxima(dogstack,mainImage,octaveNumber,tracker):
    #mult = octaveNumber
    count=0
    for mid_window_h in range(0,(getShape(dogstack[1])[0] - 2)):
        for mid_window_w in range(0,(getShape(dogstack[1])[1] - 2)):
            middogslice = sliceMat(dogstack[1],mid_window_h,(mid_window_h+3),mid_window_w,(mid_window_w+3))
            upperdogslice = sliceMat(dogstack[0],mid_window_h,(mid_window_h+3),mid_window_w,(mid_window_w+3))
            lowerdogslice = sliceMat(dogstack[2],mid_window_h,(mid_window_h+3),mid_window_w,(mid_window_w+3))
            center = middogslice[1][1]
            h_coords = mid_window_h+1
            w_coords = mid_window_w+1
            #print(getShape(middogslice))
            if(getShape(upperdogslice)[0] == 3 and getShape(upperdogslice)[1] == 3):
                if(isMinima(middogslice,center,True) and isMinima(upperdogslice,center,False) and isMinima(lowerdogslice,center,False)):
                    print("Keypoint Minima!");
                    print(mid_window_h,mid_window_w)
                    mainImage[h_coords*octaveNumber][w_coords*octaveNumber] = 255
                    count+=1
                    tracker.append([h_coords*octaveNumber,w_coords*octaveNumber])
                elif(isMaxima(middogslice,center,True) and isMaxima(upperdogslice,center,False) and isMaxima(lowerdogslice,center,False)):
                    print("Keypoint Maxima!");
                    print(mid_window_h,mid_window_w)
                    mainImage[h_coords*octaveNumber][w_coords*octaveNumber] = 255
                    count+=1
                    tracker.append([h_coords*octaveNumber,w_coords*octaveNumber])             
    print(count)
    return mainImage

def ecl_distance(tracker):
    import math
    [x,y] = tracker
    return math.sqrt((y-0)**2+(x-0)**2)

def matchTemplate(grayscaleImage,template):
    import cv2,imutils,numpy as np
    gaussianImage = cv2.GaussianBlur(grayscaleImage,(3,3),0)
    lap = cv2.Laplacian(gaussianImage,ddepth=32,ksize = 3)
    lapTemplate = cv2.Laplacian(template,ddepth=32,ksize=3)
    maxValFound = 0
    (storex,storey) = (0,0)
    (xcords,ycords) = (0,0)
    for downscale in np.linspace(1,0.5,20):
        if(int(lapTemplate.shape[1]*downscale) > 1):
            downscaledTemplate = imutils.resize(lapTemplate,int(lapTemplate.shape[1]*downscale))        
            a = cv2.matchTemplate(lap,downscaledTemplate,cv2.TM_CCOEFF_NORMED)
            (_,maxVal,_,(xval,yval)) = cv2.minMaxLoc(a)
            if maxVal > maxValFound:
                maxValFound = maxVal
                templateShape = np.shape(downscaledTemplate)
                (storexp,storeyp) =  (storex,storey)
                (storex,storey) = (xcords,ycords)
                (xcords,ycords) = (xval,yval)
    for upscale in np.linspace(2,1.02,20):
        if(int(lapTemplate.shape[1]*upscale) > 1):
            upscaledTemplate = imutils.resize(lapTemplate,int(lapTemplate.shape[1]*upscale))
            a = cv2.matchTemplate(lap,upscaledTemplate,cv2.TM_CCOEFF_NORMED)
            (_,maxVal,_,(xval,yval)) = cv2.minMaxLoc(a)
            if maxVal > maxValFound:
                maxValFound = maxVal
                templateShape = np.shape(downscaledTemplate)
                (storexp,storeyp) =  (storex,storey)
                (storex,storey) = (xcords,ycords)
                (xcords,ycords) = (xval,yval)
    # False Positive Run Assuming there are two cursors 
    #secondaryImage = grayscaleImage.copy()
    print((storexp,storeyp))
    print((storex,storey))
    print((xval,yval))
    #cv2.rectangle(secondaryImage,(xcords, ycords),(xcords+templateShape[0], ycords+templateShape[1]),(0,0,0),-1)
    return [maxValFound,templateShape,(xcords,ycords)]

def matchTemplateAdv(grayscaleImage,template):
    import cv2,imutils,numpy as np
    gaussianImage = cv2.GaussianBlur(grayscaleImage,(5,5),0)
    lap = cv2.Laplacian(gaussianImage,ddepth=32)
    lapTemplate = cv2.Laplacian(template,ddepth=32)
    maxValFoundArray=[]
    maxValFound =-1
    for downscale in np.linspace(1,0.5,20):
        if(int(lapTemplate.shape[1]*downscale) > 1):
            downscaledTemplate = imutils.resize(lapTemplate,int(lapTemplate.shape[1]*downscale))        
            a = cv2.matchTemplate(lap,downscaledTemplate,cv2.TM_CCORR_NORMED)
            (_,maxVal,_,(xval,yval)) = cv2.minMaxLoc(a)
            if maxVal > maxValFound:
                maxValFound = maxVal
                (xcords,ycords) = (xval,yval)
                maxValFoundArray.append([[maxVal],[(xcords,ycords)],[np.shape(downscaledTemplate)]])
    for upscale in np.linspace(2,1.02,20):
        if(int(lapTemplate.shape[1]*upscale) > 1):
            upscaledTemplate = imutils.resize(lapTemplate,int(lapTemplate.shape[1]*upscale))
            a = cv2.matchTemplate(lap,upscaledTemplate,cv2.TM_CCORR_NORMED)
            (_,maxVal,_,(xval,yval)) = cv2.minMaxLoc(a)
            if maxVal > maxValFound:
                maxValFound = maxVal
                (xcords,ycords) = (xval,yval)
                maxValFoundArray.append([[maxVal],[(xcords,ycords)],[np.shape(upscaledTemplate)]])
    # False Positive Run Assuming there are two cursors 
    #secondaryImage = grayscaleImage.copy()
    #cv2.rectangle(secondaryImage,(xcords, ycords),(xcords+templateShape[0], ycords+templateShape[1]),(0,0,0),-1)
    return maxValFoundArray
    