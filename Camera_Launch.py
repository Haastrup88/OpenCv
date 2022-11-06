import cv2
import numpy as np
height=720
width=1280
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*"MJPG"))

while True:
    _,frame=cam.read()
    frame=np.zeros((300,512,3),np.uint8)
    cv2.imshow("Window",frame)
    if cv2.waitKey(1) & 0xff==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()