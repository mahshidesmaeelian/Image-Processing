import cv2
import numpy as np

img1 = cv2.imread("Reveal the mystery/a.tif" , 0)
img2 = cv2.imread("Reveal the mystery/b.tif" , 0)

result = img2 - img1


cv2.imwrite('Reveal the mystery/1.jpg' , result)

cv2.imshow('output' , result)

cv2.waitKey()