import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("road.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


print(img.shape)
height=img.shape[0]
width=img.shape[1]

region_of_interest_vertices=[
    (0,height),
    (width/2,height/2),
    (width,height)
]
def region_of_interest(image,vertices):
    mask=np.zeros_like(image)
    channel_count=image.shape[2]
    match_mask_color=(255,)*channel_count
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image=cv2.bitwise_and(image,mask)

    return(masked_image)

cropped_images=region_of_interest(img,np.array([region_of_interest_vertices],np.int32))

plt.imshow(cropped_images)
plt.show()

cv2.destroyAllWindows()