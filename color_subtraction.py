import cv2
import numpy as np

cap=cv2.VideoCapture("dance.mp4")

def fu(x):
    pass

cv2.namedWindow("color_track")

cv2.createTrackbar("lower_H","color_track",0,255,fu)
cv2.createTrackbar("lower_S","color_track",0,255,fu)
cv2.createTrackbar("lower_V","color_track",0,255,fu)

cv2.createTrackbar("upper_H","color_track",255,255,fu)
cv2.createTrackbar("upper_S","color_track",255,255,fu)
cv2.createTrackbar("upper_V","color_track",255,255,fu)

while True:
    sucess,img=cap.read()
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_H=cv2.getTrackbarPos("lower_H","color_track")
    l_S=cv2.getTrackbarPos("lower_S","color_track")
    l_V=cv2.getTrackbarPos("lower_V","color_track")

    U_H=cv2.getTrackbarPos("upper_H","color_track")
    U_S=cv2.getTrackbarPos("upper_S","color_track")
    U_V=cv2.getTrackbarPos("upper_V","color_track")

    lower=np.array([l_H,l_S,l_V])
    upper=np.array([U_H,U_S,U_V])

    mask=cv2.inRange(hsv,lower,upper)
    res=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("img",img)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    if cv2.waitKey(30) & 0xFF==ord('q'):
        break
