import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("sudoku.png",cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.abs(lap))
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)

lap=np.uint8(np.abs(lap))
sobelX=np.uint8(np.abs(sobelX))
sobelY=np.uint8(np.abs(sobelY))

bitwise=cv2.bitwise_or(sobelX,sobelY)

image=[img,lap,sobelX,sobelY,bitwise]
title=["Original Image","Laplace","sobelX","solbelY","Bitwise"]

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(image[i],'gray'),plt.title(title[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.destroyAllWindows()