import cv2
import mediapipe as mp
import numpy as np 
import time
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands 
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

ctime = 0
ptime = 0

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange= volume.GetVolumeRange()
minVol=volRange[0]
maxVol=volRange[1]

while True:
    ret, frame = cap.read()
    
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id==8:
                    y1=cy
                    x1=cx
                    cv2.circle(frame, (cx, cy), 12, (0, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
            
            if 'x1' in locals():
                vol = np.interp(x1,[50,300],[minVol,maxVol])
                volume.SetMasterVolumeLevel(vol,None)
    
                vol_percentage = np.interp(vol, [minVol, maxVol], [0, 100])
                cv2.putText(frame, f"Volume: {int(vol_percentage)}%", (18,108), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(frame,"FPS:-"+str(int(fps)), (18, 78), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)

    cv2.imshow('web camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()