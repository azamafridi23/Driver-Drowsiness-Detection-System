from tkinter import *
from tensorflow.keras.models import load_model
from PIL import Image,ImageTk
import cv2
from tkinter import Toplevel
import numpy as np
import datetime
from tkinter import ttk
import os
import final_testing
from final_testing import make_pred
mymodel=load_model('final_model.h5')


to_check_if_b1_ran=0

path='to_predict' #//home//jawad//to_jawad//to_predict

root = Tk()  # create root window
root.title("Mohtat driving system")  # title of the GUI window
root.maxsize(900, 600)  # specify the max size the window can expand to
root.config(bg="skyblue")  # specify background color
imgno=1

def capture():
    global imgno
    global to_check_if_b1_ran
    to_check_if_b1_ran=1
    #print("b1 pressed")

    image=Image.fromarray(img1)
    pic='//image'+str(imgno)+'.jpg'
    image.save(path+pic)
 
    imgno+=1
    if imgno==19:
        imgno=int(imgno/19)
        print("Im ....",imgno)
    
    
def qt():
    #mixer.music.stop()
    cap.release() 
#    plt.show()
    root.destroy()

    


# Create left and right frames
left_frame = Frame(root, width=650, height=400, bg='black',highlightbackground="red")
left_frame.grid(row=0, column=0, padx=10, pady=5)



right_frame = Frame(root, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Create frames and labels in left_frame
Label(left_frame, text="Alert",font=("times new roman",20,"bold"),bg="grey",fg="green").grid(row=0, column=0, padx=5, pady=5)

# load image to be "edited"


f1=LabelFrame(right_frame,bg="green")
f1.grid(row=0,column=0, padx=5, pady=5)
L1=Label(f1,bg="green")
L1.grid(row=0,column=0, padx=5, pady=5)
cap= cv2.VideoCapture(0)




# Create tool bar frame
tool_bar = Frame(left_frame, width=180, height=200,bg="black",highlightbackground="blue")
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Example labels that serve as placeholders for other widgets


# Example labels that could be displayed under the "Tool" menu
#s_button=Button(left_frame,text="START",font=("times new roman",20,"bold"),bg="grey",fg="green",command=capture).grid(row=2, column=0, padx=5, pady=5)
Button(left_frame,text="Quit",font=("times new roman",17,"bold"),bg="grey",fg="green",command=(root.destroy and qt)).grid(row=3, column=0, padx=5, pady=15)

from tkinter import ttk
#win=Tk()
#win.geometry("700x350")
style=ttk.Style()
style.theme_use('alt')
style.configure('TButton',background='grey',font=('times new roman',15),foreground='green',width=12,padding=3,borewidth=1,focuscolor='none')
style.map('TButton',background=[('active','white')])
b1=ttk.Button(left_frame,text='Start',command=capture)
b1.grid(row=2, column=0, pady=15)
import time
first_time_run=0
count=0
while True:
    
    img = cap.read()[1]
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    
    img = ImageTk.PhotoImage(Image.fromarray(img1))
    L1['image']=img
    
    #print('button = ',s_button)
    #print('b1 = ',b1)
    if(b1!=None):
        #print(f'entered first cond and to_check = {to_check_if_b1_ran} and first_time = {first_time_run}')
        if(to_check_if_b1_ran==1 and first_time_run==0):
            start=time.time()
            first_time_run+=1
            #print('2nd cond ran')
        end=time.time()
        if(to_check_if_b1_ran==1 and first_time_run==1):
            #print('3rd cond ran')
            if(end-start>3):
                #print('yess!!')
                b1.invoke()
                print(end-start)
                start=time.time()
                count+=1
            if(count>=18):

                print("18 pic captured..")
                make_pred(mymodel)

                time.sleep(5)
                count=0
    root.update()

cap.release() 
plt.show()