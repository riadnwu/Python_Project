import numpy as np
import cv2
detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
id=raw_input("Enter Your Id: ")
count=0
while(True):
    ret,image=cam.read()
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face=detector.detectMultiScale(gray,1.3,5)  ##How Many face
    for(x,y,w,h) in face:                     ## Run the loop number of face
        count=count+1
        cv2.rectangle(image,(x+10,y+10),(x+w+10,y+h+10),(0,0,255),2)
        cv2.imwrite("Image/Student."+id+"."+str(count)+".jpg",gray[y:y+h,x:x+w])
        cv2.waitKey(500)
    cv2.imshow("Face Detect",image)
    cv2.waitKey(1)
    if count>5:
        break
cam.release()
cv2.destroyAllWindows()


