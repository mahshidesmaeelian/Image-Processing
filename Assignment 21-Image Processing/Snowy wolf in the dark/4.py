import cv2

img = cv2.imread('4.jpg' , 0)
print(img)


height , width = img.shape


for i in range(height):

    for j in range(width):

        if img[i , j] <= 160:
            img[i , j] = 0

    

cv2.imshow('snowy wolf in the darkness' , img)

cv2.imwrite('snowy wolf.jpg' , img)

cv2.waitKey()