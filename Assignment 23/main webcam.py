import cv2

# from python_utils import image_resize

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyes_cascade = cv2.CascadeClassifier("frontalEyes35x16.xml")
lips_cascade = cv2.CascadeClassifier("mouth.xml")
video_cap = cv2.VideoCapture(0)

emoji = cv2.imread("emoji2.png")
eyes_sticker = cv2.imread("eyes.png" , -1)
lips_sticker = cv2.imread("lips.png" , -1)


blur_effect = False
flip_effect = False
emoji_effect = False
face_effect = False

while True:
    ret , frame = video_cap.read()

    if ret == False:
        break

    gray_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame , 1.1 , minNeighbors=5) 
    frame = cv2.cvtColor(frame , cv2.COLOR_BGRA2BGR)


    for (x,y,w,h) in faces:
        roi_gray = gray_frame[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        img = cv2.rectangle(frame , (x,y) , (x+w , y+h) , (0 , 255 , 0) , 3)
        
        eyes = eyes_cascade.detectMultiScale(roi_gray , 1.1 , minNeighbors=5) 
        # for (ex , ey ,ew , eh) in eyes:
        #     cv2.rectangle(roi_color , (ex,ey) , (ex+ew , ey+eh) , (255 , 255 , 255) , 3)
        #     roi_eyes = roi_gray[ey:ey+eh , ex:ex+ew]
        #     eyes_sticker_resized = cv2.resize(eyes_sticker,(w,h))


        if face_effect == True:
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color , (ex,ey) , (ex+ew , ey+eh) , (255 , 255 , 255) , 3)
                # roi_eyes = roi_gray[ey:ey+eh , ex:ex+ew]

                eyes_sticker_resized = cv2.resize(eyes_sticker, (ew,eh))
                eyes2gray = cv2.cvtColor(eyes_sticker_resized,cv2.COLOR_BGR2GRAY)

                _,mask= cv2.threshold(eyes2gray,10,255,cv2.THRESH_BINARY)
                mask_inv = cv2.bitwise_not(mask)

                roi_color = cv2.bitwise_and(roi_color[ey:ey+eh, ex:ex+ew],roi_color[ey:ey+eh, ex:ex+ew],mask = mask)
                mask_eyes = cv2.bitwise_and(eyes_sticker_resized, eyes_sticker_resized, mask=mask_inv)

                eyes_sticker_final =cv2.add(mask_eyes ,roi_color)
                roi_color[ey:ey+eh, ex:ex+ew] = eyes_sticker_final


        lips = lips_cascade.detectMultiScale(roi_gray , 1.1 , minNeighbors=5) 
        for (lx , ly ,lw , lh) in lips:
            cv2.rectangle(roi_color , (lx,ly) , (lx+lw , ly+lh) , (255 , 0 , 0 ) , 3)
            roi_lips = roi_gray[ly:ly+lh , lx:lx+lw]
        
        
        if emoji_effect == True:
            resized_emoji = cv2.resize(emoji ,(ew,eh))
            img[y:y+h,x:x+w] = resized_emoji

        if flip_effect == True:
            img[y:y+h,x:x+w] = cv2.flip(img[y:y+h , x:x+w],35)
        
    
    cv2.imshow('output' , frame)
    

    k = cv2.waitKey(1)
    if k == ord("1"):
        blur_effect = not blur_effect
        print('pressed 1')

    elif k == ord("2"):
        eyes_effect = not eyes_effect

    elif k == ord("4"):
        flip_effect = not flip_effect
        

    # if k == ord('1'):
    #     if emoji_effect:
    #         emoji_effect = False
    #     else:
    #         emoji_effect = True

# video_cap.release()
# cv2.destroyAllWindows()