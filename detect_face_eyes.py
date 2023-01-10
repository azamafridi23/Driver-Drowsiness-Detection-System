import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
#save the image(i) in the same directory
img = cv2.imread("pic2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

ran=0
ran2=0


print('len of faces = ',len(faces))
if(len(faces)>0):
    for (x,y,w,h) in faces:
        #img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # detects face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y + h, x :x + w ]
        try:
            roi_color2 = img[y:y+h+25, x-25:x+w+25]
        except:
            roi_color2 = img[y:y + h , x :x + w ]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        cv2.imwrite('detected_face.jpg', roi_color2)
        ran+=1
    if(ran>0):
        for (ex,ey,ew,eh) in eyes:
            #eye=cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            try:
                eye_pic=roi_color[ey-15:ey+eh+15,ex-15:ex+ew+15]
            except:
                eye_pic = roi_color[ey:ey + eh , ex :ex + ew ]
            cv2.imwrite(f'detected_eye{ran2+1}.jpg', eye_pic)
            ran2+=1

if(len(faces)==0):
    cv2.imwrite('detected_face.jpg',img)
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()