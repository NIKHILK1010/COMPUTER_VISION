import cv2
import time
car_cascade=cv2.CascadeClassifier('carx.xml')
cap=cv2.VideoCapture('carv.mp4')
ptime=0
while True:
    sucess,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    car=car_cascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in car:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
    
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    
    cv2.putText(img,"FPS:"+str(int(fps)),(150,50),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(100,00,200),3)
    cv2.imshow("img",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
