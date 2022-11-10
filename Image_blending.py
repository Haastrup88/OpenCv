import cv2
import numpy as np
#Load two images of the objects
#Find the guassian pyramid of the objects
#From the guassian pyramid, find the laplacian pyramid
#Join the left and right half of the objects
#From the joined objects, reconstruct original images.
orange_img=cv2.imread("apple.jpg")
apple_img=cv2.imread("orange.jpg")
apple_orange=np.hstack((orange_img[:,:256],apple_img[:,256:]))

print(orange_img.shape)
print(apple_img.shape)
#Generate guassian pyramid for apple
apple_copy=np.copy(apple_img)
gp_apple=[apple_copy]

for i in range(6):
    apple_copy=cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#Generate guassian pyramid for orange
orange_copy=np.copy(orange_img)
gp_orange=[orange_copy]

for i in range(6):
    orange_copy=cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#Generate Laplacian pyramid for apple
apple_copy=gp_apple[5]
lp_apple=[apple_copy]
for i in range(5,0,-1):
    guassian_extended=cv2.pyrUp(gp_apple[i])
    laplacian=cv2.subtract(gp_apple[i-1],guassian_extended)
    lp_apple.append(laplacian)

#Generate Laplacian pyramid for orange
orange_copy=gp_orange[5]
lp_orange=[orange_copy]
for i in range(5,0,-1):
    guassian_extended=cv2.pyrUp(gp_orange[i])
    laplacian=cv2.subtract(gp_orange[i-1],guassian_extended)
    lp_orange.append(laplacian)
#Stacking the two halves of the objects

apple_orange_lp=[]
n=0
for apple_lp,orange_lp in zip(lp_apple,lp_orange):
    n=n+1
    cols,rows,ch=apple_lp.shape
    laplacian=np.hstack((apple_lp[:,0:int(cols/2)],orange_lp[:,int(cols/2):]))
    apple_orange_lp.append(laplacian)

#Reconstructing the objects
apple_orange_reconstruct=apple_orange_lp[0]
for i in range(1,6):
    apple_orange_reconstruct=cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct=cv2.add(apple_orange_lp[i],apple_orange_reconstruct)
 
cv2.imshow("Orange",orange_img)
cv2.imshow("Apple",apple_img)
cv2.imshow("Apple_orange",apple_orange)
cv2.imshow("apple_orange_reconstruct",apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()