import cv2 
import pandas as pd
img_path='pic2.jpg'
csv_path='colors.csv'

index=['colors','color_name','hex','R','G','B']
df=pd.read_csv(csv_path,names=index,header=None)
img=cv2.imread(img_path)
img=cv2.resize(img,(800,600))

clicked=False
r=g=b=xpos=ypos=0

def color_name(R,G,B):
    minimum=1000
    for i in range(len(df)):
        d=abs(R-int(df.loc[i,'R']))+abs(G-int(df.loc[i,'G']))+abs(B-int(df.loc[i,'B']))
        if d <=minimum:
            minimum=d
            cname=df.loc[i,'color_name']
    return cname
         
print(color_name(255,0,0))
def draw_function(event,x,y,flag,params):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global clicked,r,g,b,xpos,ypos
        clicked=True
        xpos=x
        ypos=y
        #print(x,y)
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)
        #print(b,g,r)
        #print(clicked,r,g,b,xpos,ypos)

cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_function)

while True:
    cv2.imshow("image",img)
    if clicked:
        cv2.rectangle(img,(20,20),(600,60),(b,g,r),-1)
        text=color_name(r,g,b)+' R='+str(r)+' G='+str(g)+' B='+str(b)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if r+g+b>=600:
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
    
    if cv2.waitKey(1) & 0xff==ord('q'):
        break



