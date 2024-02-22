import cv2
import mediapipe
import pyautogui
import math

# Define screen template size
template_width = 800
template_height = 600

# Initialize hand detection model
capture_hands = mediapipe.solutions.hands.Hands()
drawing_options = mediapipe.solutions.drawing_utils

# Get screen resolution
screen_width, screen_height = pyautogui.size()

# Initialize webcam capture
camera = cv2.VideoCapture(0)

x1 = y1 = x2 = y2 = 0
while True:  
    _, image = camera.read()
    image_height, image_width, _ = image.shape
    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process hand detection
    output_hands = capture_hands.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks
    
    if all_hands:
        for hand in all_hands:
            drawing_options.draw_landmarks(image, hand, mediapipe.solutions.hands.HAND_CONNECTIONS)
            one_hand_landmarks = hand.landmark
            for id, lm in enumerate(one_hand_landmarks):
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)
                if id == 8:
                    # Map hand coordinates to screen template
                    template_x = int(screen_width/image_width*x)
                    template_y = int(screen_height/image_height*y)
                    pyautogui.moveTo(template_x, template_y)
                    x1 = x
                    y1 = y
                if id == 4:
                    x2 = x
                    y2 = y

            dist = math.hypot(x2 - x1, y2 - y1)
            if dist < 25:
                pyautogui.click() 
                cv2.circle(image, (x1, y1), 10, (255, 217, 4), -1)
                cv2.circle(image, (x2, y2), 10, (255, 217, 4), -1)

    cv2.imshow("Hand movement video capture", image)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
