import cv2
import numpy as np

img=cv2.imread("chessboard.png")
img=cv2.resize(img,(1000,600))
#cv2.imshow("Chessboard1",img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

dst=cv2.cornerHarris(gray,2,3,0.04)

dst=cv2.dilate(dst,None)
img[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow("Chessboard",img)
cv2.waitKey(0)
if cv2.waitKey(1) & 0xff==ord("q"):
    cv2.destroyAllWindows()