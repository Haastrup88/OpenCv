import cv2
import numpy as np

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
width=150
height=75
def out(x):
    print(x)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))

cv2.namedWindow("Image")
cv2.createTrackbar("LH","Image",0,255,out)
cv2.createTrackbar("LS","Image",0,255,out)
cv2.createTrackbar("LV","Image",0,255,out)
cv2.createTrackbar("UH","Image",255,255,out)
cv2.createTrackbar("US","Image",255,255,out)
cv2.createTrackbar("UV","Image",255,255,out)

while True:
    _,frame=cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh=cv2.getTrackbarPos("LH","Image")
    ls=cv2.getTrackbarPos("LS","Image")
    lv=cv2.getTrackbarPos("LV","Image")
    uh=cv2.getTrackbarPos("UH","Image")
    us=cv2.getTrackbarPos("US","Image")
    uv=cv2.getTrackbarPos("UV","Image")

    l_b=np.array([lh,ls,lv])
    u_b=np.array([uh,us,uv])

    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("reset",res)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()