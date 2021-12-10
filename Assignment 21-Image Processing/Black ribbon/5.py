import cv2

img = cv2.imread('5.jpg' , 0)

for i in range(100):
        if i <= 70:
            for j in range(70-i , 100-i):
                if(j >= 0):
                    img[i,j] = 0

        else:
            for j in range(0 , 100-i):
                if(j >= 0):
                    img[i,j] = 0

cv2.imshow('marhoom Xxxtentation' , img)

cv2.imwrite('xxxtentation has pass away.jpg' , img)

cv2.waitKey()