import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("road.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

def region_of_interest(image,vertices):
    mask=np.zeros_like(image)
    #channel_count=image.shape[2]
    match_mask_color=255
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image=cv2.bitwise_and(image,mask)

    return(masked_image)

def draw_line(image,lines):
    cimage=np.copy(image)
    blank_img=np.zeros((cimage.shape[0],cimage.shape[1],3),dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_img,(x1,y1),(x2,y2),(0,255,0),5)

    Image=cv2.addWeighted(cimage,0.8,blank_img,1,0.0)
    return(Image)


print(img.shape)
height=img.shape[0]
width=img.shape[1]

region_of_interest_vertices=[
    (50,height),
    (width/2,height/2),
    (width,height)
]

gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
canny=cv2.Canny(gray,100,200)


cropped_images=region_of_interest(canny,np.array([region_of_interest_vertices],np.int32))
lines=cv2.HoughLinesP(cropped_images,rho=6,theta=np.pi/60,
threshold=160,lines=np.array([]),minLineLength=40,maxLineGap=25)


draw_image=draw_line(img,lines)
plt.imshow(draw_image)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()