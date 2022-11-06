import cv2
from matplotlib import pyplot as plt
import numpy as np

img=cv2.imread("lena.jpg")#Reads images in BGR format
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Low pass filter(LPF) helps in removing noise and blurring of images, while High pass filter(LPF) is used to remove ages

#Guassian filter uses different weight kernel in both x and y direction
kernel=np.ones((5,5),np.uint8)/25
dst=cv2.filter2D(img,-1,kernel)#Blurring of Image
gblur=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5)# It is used to remove salt-and-pepper noise
bilateral=cv2.bilateralFilter(img,9,75,75)#This is used to remove noise when the edge of the image is needed to be preserved.

image=[img,dst,gblur,median,bilateral]
title=["Original image","2D Convolution","Guassian Blur","MedianBlur","Bilateral_filter"]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(image[i],'gray')#Reads images in RGB format
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.destroyAllWindows()