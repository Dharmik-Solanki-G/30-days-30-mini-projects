import cv2
import mediapipe as mp
import time
import math 
import screen_brightness_control as sbc


wCam, hCam = 1280,1280

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

mpHands = mp.solutions.hands 
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

ctime = 0
ptime = 0

while True:
    ret, frame = cap.read()
    
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id==4 or id==8:
                    if(id==4):
                        x1,y1=cx,cy
                        print(id, cx, cy,end='  ')
                    else:
                        x2,y2=cx,cy
                        print(id, cx, cy)
                    cv2.circle(frame, (cx, cy), 12, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
            
            if 'x1' in locals() and 'y1' in locals() and 'x2' in locals() and 'y2' in locals():
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

                centX = (x1 + x2) // 2
                centY = (y1 + y2) // 2
                
                cv2.circle(frame, (centX, centY), 8, (0, 255, 0), cv2.FILLED)
                length = math.hypot(x2-x1,y2-y1) 
                print(length)
                if length<25:
                    sbc.set_brightness(0)
                    cv2.circle(frame, (centX, centY), 8, (0, 0, 255), cv2.FILLED)
                elif length<50:
                    sbc.set_brightness(16)
                elif length<100:
                    sbc.set_brightness(32)
                elif length<150:
                    sbc.set_brightness(48)
                elif length<200:
                    sbc.set_brightness(64)
                elif length<250:
                    sbc.set_brightness(80)
                elif length<300:
                    sbc.set_brightness(96)
                else:
                    sbc.set_brightness(100)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(frame,"FPS:-"+str(int(fps)), (18, 78), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)

    cv2.imshow('web camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()