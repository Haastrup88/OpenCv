import cv2
import numpy as np
img=cv2.imread("smarties.png")
output=img.copy()
imgG=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgG=cv2.medianBlur(imgG,5)
circles=cv2.HoughCircles(imgG,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0, maxRadius=0)
detected_circle=np.uint16(np.around(circles))
for (x,y,r) in detected_circle[0,:]:
    cv2.circle(output,(x,y),r,(0,255,0),3)
    cv2.circle(output,(x,y),2,(0,255,255),3)

cv2.imshow("Img",output)
cv2.waitKey(0)
cv2.destroyAllWindows()