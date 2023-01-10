# code to resize images

import cv2
import glob
import os

#print(os.listdir('Open'))


input_folder='resized_to_predict'
folder_len=len(input_folder)
#os.mkdir('resized_to_predict')
for img in glob.glob(input_folder+"/*.*"):
    image=cv2.imread(img)
    imgResized=cv2.resize(image,(150,150))
    cv2.imwrite("resized_to_predict"+img[folder_len:],imgResized)


