import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('f4.jpg')
img=cv2.resize(img,(600,500))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("img",img)
cv2.waitKey(0)
