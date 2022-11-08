import cv2
import numpy as np
from matplotlib import pyplot as plt
#Canny edge detection algorithm is divided into three steps
#1. Noise Reduction
#2. Gradient calculation
#3. Non-maximum suppresion
#4. Double threshold
#5. Edge tracking by hysteresis 

img=cv2.imread("messi5.jpg",cv2.IMREAD_GRAYSCALE)
canny=cv2.Canny(img,100,200)
image=[img,canny]
title=["Original image","canny"]

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(image[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
plt.show()
