import cv2
import math

path='1.jpg'
img=cv2.imread(path)

pointslist=[]

def mousepoint(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        size=len(pointslist)
        if size !=0 and size %3!=0:
            cv2.line(img,tuple(pointslist[round((size-1)/3)*3]),(x,y),(0,0,255),2)
        cv2.circle(img,(x,y),5,(0,0,255),2,cv2.FILLED)
        pointslist.append([x,y])
        print(pointslist)


def gradients(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def getangle(pointslist):
    pt1,pt2,pt3=pointslist[-3:]
    m1=gradients(pt1,pt2)
    m2=gradients(pt1,pt3)
    angR=math.atan((m1-m2)/(1+m1*m2))
    angD=round(math.degrees(angR))
    cv2.putText(img,str(angD),(pt1[0]-40,pt1[1]-20),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255),2)

while True:
    if len(pointslist)%3==0 and len(pointslist)!=0:
        getangle(pointslist)



    cv2.imshow("img",img)
    cv2.setMouseCallback("img",mousepoint)
    if cv2.waitKey(1) & 0xff==ord('q'):
        pointslist=[]
        img=cv2.imread(path)
    
    
