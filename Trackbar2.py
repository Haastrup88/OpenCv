import cv2
import numpy as np

def num(x):
    print(x)
cv2.namedWindow("Image")
cv2.createTrackbar("CP","Image",15,255,num)
switch="0 for OFF \n 1 for ON"
cv2.createTrackbar(switch,"Image",0,1,num)

while True:
    img=cv2.imread("lena.jpg")
    pos=cv2.getTrackbarPos("CP","Image")
    s=cv2.getTrackbarPos(switch,"Image")
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(pos),(50,180),font,4,(255,0,0),3)
    if cv2.waitKey(1) & 0xff==ord("q"):
        break

    if s==0:
        pass
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    img=cv2.imshow("Image",img)
cv2.destroyAllWindows()
