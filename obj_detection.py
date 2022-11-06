import cv2
import numpy as np
def dummy(x):
    pass

cv2.namedWindow("Image")
cv2.createTrackbar("LH","Image",0,255,dummy)
cv2.createTrackbar("LS","Image",0,255,dummy)
cv2.createTrackbar("LV","Image",0,255,dummy)
cv2.createTrackbar("UH","Image",255,255,dummy)
cv2.createTrackbar("US","Image",255,255,dummy)
cv2.createTrackbar("UV","Image",255,255,dummy)

while True:
    img=cv2.imread('smarties.png')
    lh=cv2.getTrackbarPos("LH","Image")
    ls=cv2.getTrackbarPos("LS","Image")
    lv=cv2.getTrackbarPos("LV","Image")
    uh=cv2.getTrackbarPos("UH","Image")
    us=cv2.getTrackbarPos("US","Image")
    uv=cv2.getTrackbarPos("UV","Image")

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_b=np.array([lh,ls,lv])
    u_b=np.array([uh,us,uv])
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("smarties",img)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cv2.destroyAllWindows()
