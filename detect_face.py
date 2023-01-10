import cv2
import sys

imagePath = 'pic2.jpg'

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

print("[INFO] Found {0} Faces.".format(len(faces)))

for (x, y, w, h) in faces:
    #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = image[y-15:y + h+15, x-15:x + w+15]
    #print("[INFO] Object found. Saving locally.")
    cv2.imwrite('detected_face.jpg', roi_color)


# doesn't work when person is wearing sunglasses probably