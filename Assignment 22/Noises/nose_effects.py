import random
import cv2
import numpy as np

img = cv2.imread("chess pieces.jpg" , 0)

rows,cols = img.shape

for i in range(12000):
    noise = random.randint(100,220)
    random_position1 = random.randint(0 , rows-1)
    random_position2 = random.randint(0 , cols-1)
    img[random_position1,random_position2] = noise

cv2.imwrite('noisey_effect.jpg' , img)

cv2.imshow('Highway' , img)

cv2.waitKey()