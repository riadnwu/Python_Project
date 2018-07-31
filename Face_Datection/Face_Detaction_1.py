import numpy as np
import cv2

image=cv2.imread('show.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('iamge',image)
cv2.waitKey(0)
cv2.destroyAllWindows()