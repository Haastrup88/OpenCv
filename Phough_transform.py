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
img=cv2.imread("road.jpg")
ImgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(ImgGray,50,150,apertureSize=3)
cv2.imshow("Edge",edges)
lines=cv2.HoughLinesP(edges,1,np.pi/180,300,minLineLength=100,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)


cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()