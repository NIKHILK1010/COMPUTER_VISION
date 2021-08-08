import cv2
import time
cap=cv2.VideoCapture(0)

ptime=0
while True:
    success, img1=cap.read()
    success, img2=cap.read()
    diff=cv2.absdiff(img1,img2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,threshold=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(threshold,None,iterations=3)
    contour,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    #cv2.drawContours(img1,contour,-1,(250,0,2),2)
    for c in contour:
        if cv2.contourArea(c)<5000:
            continue
        x,y,w,h=cv2.boundingRect(c)
        cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),2)
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    
    cv2.putText(img1,str(int(fps)),(50,50),cv2.FONT_HERSHEY_TRIPLEX,2,(255,0,0),2)
    cv2.imshow("video",img1)
    if cv2.waitKey(80) & 0xFF==ord('q'):
        break
    

