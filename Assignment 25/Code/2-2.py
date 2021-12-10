import cv2
import numpy as np

img = cv2.imread('building.tif')
img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

result = np.zeros(img.shape)

mask = np.array([[-1 , -1 , -1],
                [0 , 0 , 0],
                [1 , 1 , 1]])

rows, cols = img.shape


for i in range(1, rows-1):
    for j in range(1 , cols-1):
        part_of_img = img[i-1:i+2 , j-1:j+2]
        result[i,j] = np.sum(part_of_img * mask)

cv2.imwrite('result2_2.jpg' , result)


