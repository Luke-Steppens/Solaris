import cv2
import mediapipe as mp
import pygame
import serial
import time

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection()

# Initialize Pygame Window
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Face Controlled Ball")
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

dot_x, dot_y = WIDTH // 2, HEIGHT // 2
dot_radius = 10

# Open Camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Setup Serial Communication with Arduino
try:
    arduino = serial.Serial('COM3', 9600)
    time.sleep(2)
    print("Connected to Arduino.")
except serial.SerialException:
    print("Error: Could not connect to Arduino.")
    arduino = None

# Main loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_detection.process(rgb_frame)

    if result.detections:
        print(f"Detected {len(result.detections)} face(s)")
        for detection in result.detections:
            bbox = detection.location_data.relative_bounding_box
            dot_x = int(bbox.xmin * WIDTH + bbox.width * WIDTH / 2)
            dot_y = int(bbox.ymin * HEIGHT + bbox.height * HEIGHT / 2)
            print(f"Face Position: {dot_x}, {dot_y}")
            if arduino:
                arduino.write(f"{dot_x},{dot_y}\n".encode())

    cv2.imshow("Face Tracking", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

    screen.fill(BLACK)
    pygame.draw.circle(screen, GREEN, (dot_x, dot_y), dot_radius)
    pygame.display.update()

cap.release()
cv2.destroyAllWindows()
pygame.quit()
if arduino:
    arduino.close()
