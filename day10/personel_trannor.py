import cv2
import mediapipe as mp 
import numpy as np 
import time 
import math

mpDraw = mp.solutions.drawing_utils
myPose = mp.solutions.pose 
pose = myPose.Pose()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

pTime = 0
cTime = 0

count=0
dir=0

lmlist = []  # Initialize the list to store landmarks

while True:
    success, img = cap.read()

    if not success:
        print("Error: Could not read frame from camera.")
        break
       
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    
    if results.pose_landmarks:
        #mpDraw.draw_landmarks(img, results.pose_landmarks, myPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            
            if id == 12 or id == 14 or id == 22:
                lmlist.append([id, cx, cy])

        if len(lmlist) == 3:
            x1, y1 = lmlist[0][1:]
            x2, y2 = lmlist[1][1:]
            x3, y3 = lmlist[2][1:]

            angle=math.degrees(math.atan2(y3-y2,x3-x2)-
                                math.atan2(y1-y2,x1-x2))
            if angle<0:
                angle+=360
            per=np.interp(angle,(200,340),(0,100))
            if angle<180:
                per=np.interp(angle,(20,150),(0,100))

            if per==100:
                if dir==0:
                    count+=0.5
                    dir=1
            if per == 0:
                if dir==1:
                    count+=0.5
                    dir=0
                            
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)
            cv2.line(img,(x3,y3),(x2,y2),(0,255,0),3)
            cv2.circle(img,(x1,y1),10,(0,0,255),cv2.FILLED)
            cv2.circle(img,(x1,y1),15,(0,0,255),2)
            cv2.circle(img,(x2,y2),10,(0,0,255),cv2.FILLED)
            cv2.circle(img,(x2,y2),15,(0,0,255),2)
            cv2.circle(img,(x3,y3),10,(0,0,255),cv2.FILLED)
            cv2.circle(img,(x3,y3),15,(0,0,255),2)
            cv2.putText(img,'Angle:'+str(int(angle)),(18,108), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
            cv2.putText(img,'counter:'+str(int(count)),(18,138), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            lmlist = []  

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, 'FPS:'+str(int(fps)), (18, 78), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
 
    cv2.imshow('Image', img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
