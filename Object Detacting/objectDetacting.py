import cv2
import numpy as np

def imageCompair(newImage,compairableImage):
    image1=cv2.cvtColor(newImage,cv2.COLOR_BGR2GRAY)
    objectDetector=cv2.ORB(1000,1.2)
    (kp1,des1)=objectDetector.detectAndCompute(image1,None)
    (kp2, des2) = objectDetector.detectAndCompute(compairableImage, None)
    bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    matches=bf.match(des1,des2)
    matches=sorted(matches,key=lambda val: val.distance)
    return len(matches)

cap=cv2.VideoCapture(1)
compairableImage=cv2.imread('detecting.jpg',0)

while True:
    ret,frame=cap.read()
    hight,width=frame.shape[:2]

    topLeftX=width/3
    topLeftY=(hight/2)+(hight/4)
    bottomRightX=(width/3)*2
    bottomRightY=(hight/2)-(hight/4)

    cv2.rectangle(frame,(topLeftX,topLeftY),(bottomRightX,bottomRightY),255,3)
    cropped=frame[bottomRightY:topLeftY,topLeftX:bottomRightX]

    frame=cv2.flip(frame,1)
    matcches=imageCompair(cropped,compairableImage)
    cv2.putText(frame,str(matcches),(450,450),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),1)
    threshold=350
    if matcches>threshold:
        cv2.rectangle(frame,(topLeftX,topLeftY),(bottomRightX,bottomRightY),(0,255,0),3)
        cv2.putText(frame,"Object Found",(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)

    cv2.imshow("Objec Detector",frame)
    if cv2.waitKey((1))== 13:
        break
cap.release()
cv2.destroyAllWindows()

