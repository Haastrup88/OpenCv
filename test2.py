from matplotlib import pyplot as plt
import cv2
img=cv2.imread('sudoku.png',0)
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,200,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,200,255,cv2.THRESH_TOZERO)
_,th5=cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)

image=[img,th1,th2,th3,th4,th5]
title=["Original Image","Binary","Binary Inv","Trunc","Tozero","ToZero_inv"]
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(image[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
plt.show()