import cv2
import mediapipe as mp
import pyautogui
import time
import webbrowser
from collections import deque

# Open game in browser
webbrowser.open("https://poki.com/en/g/temple-run-2")
time.sleep(5)

# Setup MediaPipe FaceMesh
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(
    max_num_faces=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Start camera
cap = cv2.VideoCapture(0)

# Extended eye landmarks
LEFT_EYE = [33, 133, 160, 159, 158, 157, 173]
RIGHT_EYE = [362, 263, 387, 386, 385, 384, 398]

# Eye smoothing history
eye_history = deque(maxlen=5)

# Cooldown settings
cooldown = 1.5
last_command_time = time.time()

def get_eye_center(landmarks, eye_points, w, h):
    x = [landmarks[i].x for i in eye_points]
    y = [landmarks[i].y for i in eye_points]
    center_x = int(sum(x) / len(x) * w)
    center_y = int(sum(y) / len(y) * h)
    return center_x, center_y

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w, _ = frame.shape
    mid_x, mid_y = w // 2, h // 2

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        face = results.multi_face_landmarks[0]

        left_eye_center = get_eye_center(face.landmark, LEFT_EYE, w, h)
        right_eye_center = get_eye_center(face.landmark, RIGHT_EYE, w, h)

        # Average of both eyes
        eye_x = (left_eye_center[0] + right_eye_center[0]) // 2
        eye_y = (left_eye_center[1] + right_eye_center[1]) // 2

        # Smoothing with moving average
        eye_history.append((eye_x, eye_y))
        avg_x = int(sum(p[0] for p in eye_history) / len(eye_history))
        avg_y = int(sum(p[1] for p in eye_history) / len(eye_history))

        # Dynamic thresholds
        threshold_x = int(w * 0.08)
        threshold_y = int(h * 0.08)

        now = time.time()
        if now - last_command_time > cooldown:
            if avg_x < mid_x - threshold_x:
                pyautogui.press("left")
                print("LEFT")
                last_command_time = now
            elif avg_x > mid_x + threshold_x:
                pyautogui.press("right")
                print("RIGHT")
                last_command_time = now
            elif avg_y < mid_y - threshold_y:
                pyautogui.press("up")
                print("UP")
                last_command_time = now
            elif avg_y > mid_y + threshold_y:
                pyautogui.press("down")
                print("DOWN")
                last_command_time = now

        # Optional: draw the eye centers
        cv2.circle(frame, left_eye_center, 5, (0, 255, 0), -1)
        cv2.circle(frame, right_eye_center, 5, (0, 255, 0), -1)
        cv2.circle(frame, (avg_x, avg_y), 5, (255, 0, 0), -1)

    # UI Overlay
    cv2.putText(frame, "Eye Control Active - Press 'Q' to Quit",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    cv2.imshow("Eye Game Control", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
