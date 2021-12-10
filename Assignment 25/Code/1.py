import cv2
import numpy as np

img = cv2.imread('flower_input.jpg')
img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

result = np.zeros(img.shape)

rows, cols = img.shape

mask = np.ones((35,35)) / 1225

for i in range (17 , rows-17):
    for j in range(17 , cols-17):          
        part_of_img = img[i-17:i+18,j-17:j+18]
        result[i,j] = np.sum(part_of_img * mask)

for i in range(rows):
    for j in range(cols):
        if img[i,j] <= 200: 
            img[i,j] = result[i,j]
        
cv2.imshow('blurred background' , img)
cv2.imwrite('blurred background.jpg' , img)
cv2.waitKey()

