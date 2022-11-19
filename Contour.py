import cv2
import numpy as np
#Contour is is a python list of all contour in the image. Each individual contour is a numpy array of (x,y) coordinates of
#boundary point of the object
img=cv2.imread("opencv-logo.png")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgGray,127,255,0)
contour,hierarchy=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print("The numbers of contours are="+str(len(contour)))
print(contour[18])
cv2.drawContours(img,contour,18,(0,255,0),3)
cv2.imshow("Image",img)
cv2.imshow("GrayImage",imgGray)

cv2.waitKey(0)

cv2.destroyAllWindows()