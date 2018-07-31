import numpy as np
import cv2
detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
while(True):
    ret,image=cam.read()
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face=detector.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in face:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Face Detect",image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


