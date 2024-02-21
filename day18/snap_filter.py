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
                # Draw 5 dots on the right side of the face
                if id in [12, 133, 4, 15, 106]:  # Right side landmarks
                    cv2.circle(frame, (x, y), 4, (255, 217, 4), -1)
                # Draw 5 dots on the left side of the face
                if id in [100, 101, 142, 123, 104]:  # Left side landmarks
                    cv2.circle(frame, (x, y), 4, (255, 217, 4), -1)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(frame, "FPS:-"+str(int(fps)), (18, 78), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('web camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
