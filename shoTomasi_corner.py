import cv2
import numpy as np
#Shi tomasi algrithm is use when all the corners are not to be detected.
img=cv2.imread("pic1.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners=cv2.goodFeaturesToTrack(gray,20,0.01,10)
corners=np.int0(corners)
print(corners)
for i in corners:
    (x,y)=np.ravel(i)
    cv2.circle(img,(x,y),3,(0,0,255),-1)

cv2.imshow("Picture",img)
if cv2.waitKey(0) & 0xff==ord("q"):
    cv2.destroyAllWindows()
