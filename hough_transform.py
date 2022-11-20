import cv2
import numpy as np
#Steps of Hough transform
#Edge detection, e.g. using the canny edge detector
#Mapping of edge points to the hough space 
#Interpretation of the accumulator to yield lines of infinite length
#Conversion of infinite line to finite line

#Hough line transform algorithm types
# 1. The standard Hough transform
# 2. Probabilistic Hough line transform

img=cv2.imread("sudoku.png")
ImgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(ImgGray,50,150,apertureSize=3)
cv2.imshow("Edge",edges)
lines=cv2.HoughLines(edges,1,np.pi/180,200)

for line in lines:
    rho,theta=line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho
    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))

    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow("Img",img)
cv2.waitKey(0)

cv2.destroyAllWindows()