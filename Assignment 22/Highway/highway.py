import cv2
import numpy as np

images = []

for i in range(15):
    img = cv2.imread(f'h{i}.jpg' , 0)
    images.append(img)
    rows,cols = img.shape

result = np.zeros((rows , cols) , dtype='uint8')

for image in images:
    result += image//15


cv2.imwrite('clear_streets.jpg' , result)

cv2.imshow('Highway' , result)

cv2.waitKey()