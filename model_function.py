#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 23:00:16 2022

@author: jawad
"""

import numpy as np
import os
import cv2

import cv2
import glob
import os



def detect():

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    
    image_no=1
    input_folder='to_predict'
    folder_len=len(input_folder)
    for i in os.listdir(input_folder):
        print('i = ',i)
    #save the image(i) in the same directory
        img = cv2.imread('to_predict//'+i)
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
                    roi_color2 = img[y:y+h+5, x-5:x+w+5]
                except:
                    roi_color2 = img[y:y + h , x :x + w ]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                cv2.imwrite(f'resized_to_predict//_detected_face_{image_no}.jpg', roi_color2)
                print("detected face ran")
                ran+=1
            if(ran>0):
                print("ran>0 true")
                for (ex,ey,ew,eh) in eyes:
                    print("eyes for loop")
                    #eye=cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    try:
                        eye_pic=roi_color[ey-5:ey+eh+5,ex-5:ex+ew+5]
                    except:
                        eye_pic = roi_color[ey:ey + eh , ex :ex + ew ]

                    # or use eye_pic is None
                    if(eye_pic.any()!=None):
                        cv2.imwrite(f'resized_to_predict//detected_eye{ran2+1}_{image_no}.jpg', eye_pic)
                    print('eye ran')
                    ran2+=1
    
        if(len(faces)==0):
            cv2.imwrite(f'resized_to_predict//detected_face_{image_no}.jpg',img)
            #print('faces = 0')
        image_no+=1
        
def resize():

    input_folder='resized_to_predict'
    folder_len=len(input_folder)
    for img in glob.glob(input_folder+"/*.*"):
        image=cv2.imread(img)
        imgResized=cv2.resize(image,(150,150))
        cv2.imwrite("resized_to_predict"+img[folder_len:],imgResized)
        
