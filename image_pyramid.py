import cv2
import numpy as np
img=cv2.imread("lena.jpg")
layer=img.copy()
gp=[layer]

#pyrdown_1=cv2.pyrDown(img)
#pyrdown_2=cv2.pyrDown(pyrdown_1)
#pyrUp=cv2.pyrUp(pyrdown_2)

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)

cv2.imshow("Original Image",img)
#cv2.imshow("pyrdown 1",pyrdown_1)
#cv2.imshow("pyrdown 2",pyrdown_2)
#cv2.imshow("pyrUp",pyrUp)
cv2.waitKey(0)
cv2.destroyAllWindows()