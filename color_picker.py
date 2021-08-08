import cv2
import numpy as np

img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow("color pick")


def fu(x):
    pass


cv2.createTrackbar("R","color pick",0,255,fu)
cv2.createTrackbar("G","color pick",0,255,fu)
cv2.createTrackbar("B","color pick",0,255,fu)

while True:
    cv2.imshow("color pick",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

    r=cv2.getTrackbarPos("R","color pick")
    g=cv2.getTrackbarPos("G","color pick")
    b=cv2.getTrackbarPos("B","color pick")
    img[:]=[r,g,b]

