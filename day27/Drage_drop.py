import cv2
import mediapipe as mp
import time
import math 

cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

mpHands = mp.solutions.hands 
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

ctime = 0
ptime = 0

colourR = (255, 0, 255)

crx,cry,w,h=50,50,100,100

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break
    
    frame = cv2.flip(frame, 1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList=[id, cx, cy]
                if id==4 or id==8:
                    if(id==4):
                        x1,y1=cx,cy
                    else:
                        x2,y2=cx,cy
                    cv2.circle(frame, (cx, cy), 12, (255, 0, 255), cv2.FILLED)
            
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

            if 'x1' in locals() and 'y1' in locals() and 'x2' in locals() and 'y2' in locals():
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

                centX = (x1 + x2) // 2
                centY = (y1 + y2) // 2
                
                cv2.circle(frame, (centX, centY), 8, (0, 255, 0), cv2.FILLED)
                length = math.hypot(x2-x1,y2-y1) 

                if length<40:
                    cv2.circle(frame, (centX, centY), 8, (0, 0, 255), cv2.FILLED)
                    if crx-w//8 < x1 < crx+w//8 and cry-h//8 < y1 < cry+h//8:
                        colourR = (0, 255, 0)
                        crx,cry=x2,y2  
                else:
                    colourR = (255, 0, 255)

    cv2.rectangle(frame, (crx-w//8,cry-h//8), (crx+w//8,cry+h//8), colourR, cv2.FILLED)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(frame, str(int(fps)), (18, 78), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 1)

    cv2.imshow('web camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
