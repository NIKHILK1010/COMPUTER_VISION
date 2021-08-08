import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture("dance.mp4")


m_draw=mp.solutions.drawing_utils
m_pose=mp.solutions.pose
pose=m_pose.Pose()

ptime=0
while True:
    success, img=cap.read()
    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=pose.process(rgb)
    print(result.pose_landmarks)
    if result.pose_landmarks:
        m_draw.draw_landmarks(img,result.pose_landmarks,m_pose.POSE_CONNECTIONS)
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    
    cv2.putText(img,str(int(fps)),(50,50),cv2.FONT_HERSHEY_TRIPLEX,2,(255,0,0),2)
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
