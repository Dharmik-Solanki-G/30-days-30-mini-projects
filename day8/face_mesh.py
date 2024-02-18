import cv2
import mediapipe as mp 
import time

cap = cv2.VideoCapture(0)

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)

ctime = 0
ptime = 0

while True:
    ret, frame = cap.read()
    
    results = faceMesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            for id, lm in enumerate(faceLms.landmark):
                ih, iw, _ = frame.shape
                x, y = int(lm.x * iw), int(lm.y * ih)
                cv2.circle(frame, (x, y), 2, (255, 217, 4), -1)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(frame, "FPS:-"+str(int(fps)), (18, 78), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('web camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
