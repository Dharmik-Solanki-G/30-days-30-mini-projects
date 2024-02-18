import cv2
import mediapipe as mp 
import time

cap = cv2.VideoCapture(0)

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)

mpHands = mp.solutions.hands 
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

myPose = mp.solutions.pose 
pose = myPose.Pose()

ctime = 0
ptime = 0

# Set the initial window size
cv2.namedWindow('web camera', cv2.WINDOW_NORMAL)
# Resize the window
cv2.resizeWindow('web camera', 1000, 750)  # Set your desired width and height

while True:
    ret, frame = cap.read()
    
    results = faceMesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            for id, lm in enumerate(faceLms.landmark):
                ih, iw, _ = frame.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                cv2.circle(frame, (x, y), 2, (255, 217, 4), -1)

    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (cx, cy), 8, (255, 217, 4), cv2.FILLED)

            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

    results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))


    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            if id==0 or id==1 or id==2 or id==3 or id==4 or id==5 or id==6 or id==7 or id==8 or id==9 or id==10 or id==15 or id==17 or id==19 or id==21 or id==22 or id==16 or id==18 or id==20 :
                pass
            else:
                cv2.circle(frame, (cx, cy), 12, (255, 217, 4), cv2.FILLED)
        mpDraw.draw_landmarks(frame, results.pose_landmarks, myPose.POSE_CONNECTIONS)


    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(frame, "FPS:-"+str(int(fps)), (18, 78), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('web camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
