import cv2
import numpy as np

def convolution(dimention ):
    img = cv2.imread('3.jpg')
    img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    result = np.zeros(img.shape)

    mask = np.ones((dimention,dimention)) / dimention**2

    rows, cols = img.shape

    s= dimention//2

    for i in range(s, rows-s):
        for j in range(s , cols-s):
            part_of_img = img[i-s:i+s+1 , j-s:j+s+1]
            result[i,j] = np.sum(part_of_img * mask)
            return img

#static input
result1 = convolution(3)
result2 = convolution(5)
result3 = convolution(7)
result4 = convolution(15)   

cv2.imwrite('result3.jpg' , result1)
cv2.imwrite('result3_2.jpg' , result2)
cv2.imwrite('result3_3.jpg' , result3)
cv2.imwrite('result3_4.jpg' , result4)

#dynamic input
#User can enter the dimention vvvv
answer= int(input('Enter the array dimension:'))
dynamic_res = convolution(answer)
cv2.imwrite('users_result.jpg' , dynamic_res)







