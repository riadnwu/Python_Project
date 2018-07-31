import cv2
import numpy as np

image=cv2.imread("5.jpg")
cv2.imshow("6 cm distance",image)
cv2.waitKey(0)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

detacting=cv2.imread("detacting.jpg",0)
result=cv2.matchTemplate(gray,detacting,cv2.TM_CCOEFF)
minValue,maxValue,minLoc,Maxloc=cv2.minMaxLoc(result)

topLeft=Maxloc
bottomRight=(topLeft[0]+120,topLeft[1]+200)
cv2.rectangle(image,topLeft,bottomRight,(0,0,255),2)

cv2.imshow("Find 6 cm distance",image)
cv2.waitKey(0)
cv2.destroyAllWindows()