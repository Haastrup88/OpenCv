import cv2
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
kernel=np.ones((2,2),np.uint8)# This defined the size that would be applied in performing dilation
dilation=cv2.dilate(mask,kernel,iterations=2)# This filter the black pixels to white
erosion=cv2.erode(mask,kernel,iterations=6)# This filter the white pixels to black
open=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)#Erosion is performed first, follow by dilation
close=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)#Dilation is performed first, follow by Erosion
image=[img,mask,dilation,erosion,open,close]
title=["Original Image","Mask","Dilation","Erosion","Open","Close"]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(image[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.destroyAllWindows()