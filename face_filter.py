import cv2
import numpy as np
from PIL import Image

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
maskpath="thugs.png"
mask=Image.open(maskpath)

def filter(image):
    
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,1.5)
    background=Image.fromarray(image)

    for (x,y,w,h) in face:
        resize_mask=mask.resize((w,h),Image.ANTIALIAS)
        offset=(x+5,y+5)
        background.paste(resize_mask,offset,mask=resize_mask)
    return np.asarray(background)

cap=cv2.VideoCapture(0)

while True:
    sucess,img=cap.read()
   
    cv2.imshow("img",filter(img))
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

