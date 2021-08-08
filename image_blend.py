import cv2
import numpy as np

img1=cv2.imread("f4.jpg")
img1=cv2.resize(img1,(600,500))

img2=cv2.imread("f5.jpg")
img2=cv2.resize(img2,(600,500))

res1=cv2.addWeighted(img1,0.5,img2,0.5,0)

#cv2.imshow("img1",img1)
#cv2.imshow("img2",img2)

def fu(x):
    pass

img=np.zeros((400,400,3),np.uint8)
cv2.namedWindow("blend")

cv2.createTrackbar("alpha","blend",1,100,fu)

while True:
    a=cv2.getTrackbarPos("alpha","blend")
    n=float(a/100)
    dst=cv2.addWeighted(img1,1-n,img2,n,0)
    img[:]=a
    cv2.putText(dst,str(a),(50,50),cv2.FONT_HERSHEY_PLAIN,2,(250,0,0),2)
    cv2.imshow("blend",dst)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

