import cv2
import numpy as np
#Positve classifier: Face
#Negative Classifier: Other objects apart from the face
face_cascade=cv2.CascadeClassifier("data/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("data/haarcascades/haarcascade_eye_tree_eyeglasses.xml")
cam=cv2.VideoCapture("test.mp4")

while(cam.isOpened() and cam!=None):
    _,frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)

        

    cv2.imshow("Face",frame)
    if cv2.waitKey(1) & 0xff==ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
