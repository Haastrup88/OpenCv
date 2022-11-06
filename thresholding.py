import cv2
import numpy as np

img=cv2.imread("gradient.png")
#0 pixel is black
#255 pixel is white
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)#If the pixel of img is less than 127, convert to 0 pixel;If the pixel of img is greater than 127, convert to 255 pixel
_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)#If the pixel of img is less than 127, convert to 255 pixel;If the pixel of img is greater than 127, convert to 0 pixel
_,th3=cv2.threshold(img,200,255,cv2.THRESH_TRUNC)#If the pixel of img is less than 200, do nothing;If the pixel of img is greater than 200, convert to 200 pixel
_,th4=cv2.threshold(img,200,255,cv2.THRESH_TOZERO)#If the pixel of img is less than 200,convert pixel to 0;If the pixel of img is greater than 200, do nothing.
_,th5=cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)#If the pixel of img is less than 200, do nothing;If the pixel of img is greater than 200, convert to 0 pixel


cv2.imshow("Image",img)
cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)
cv2.imshow("th4",th4)
cv2.imshow("th5",th5)
cv2.waitKey(0)

cv2.destroyAllWindows()