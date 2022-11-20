import cv2
import numpy as np

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

def process(img):
    print(img.shape)
    height=img.shape[0]
    width=img.shape[1]

    region_of_interest_vertices=[
        (20,height),
        (width/2,height/2),
        (width,height)
    ]

    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    canny=cv2.Canny(gray,100,200)
    cv2.imshow("canny",canny)


    cropped_images=region_of_interest(canny,np.array([region_of_interest_vertices],np.int32))
    lines=cv2.HoughLinesP(cropped_images,rho=6,theta=np.pi/60,
    threshold=160,lines=np.array([]),minLineLength=40,maxLineGap=25)


    draw_image=draw_line(img,lines)
    return(draw_image)

cap=cv2.VideoCapture("test.mp4")

while(cap.isOpened):
    _,frame=cap.read()
    frame=process(frame)
    cv2.imshow("Lane",frame)
    if cv2.waitKey(1) & 0xff==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()