import cv2
import mediapipe as mp
import serial
import time
import math
import os

# Global variables
COM_PORT = 'COM8'  # Update with your correct port
MAX_RETRIES = 5  # Maximum number of retries
RETRY_DELAY = 2  # Delay between retries in seconds

# Connect to Arduino with retry mechanism
def connect_to_uno():
    retries = 0
    while retries < MAX_RETRIES:
        if os.path.exists(f'\\\\.\\{COM_PORT}'):  # Check if the port exists
            try:
                arduino = serial.Serial(COM_PORT, 115200, timeout=1)  # Open COM port
                time.sleep(2)  # Allow time for Arduino to initialize
                print("Successfully connected to Uno")
                return arduino
            except serial.SerialException as e:
                print(f"Error: Could not connect to Uno. {e}")
                retries += 1
                time.sleep(RETRY_DELAY)
        else:
            print(f"Error: COM port {COM_PORT} not found.")
            retries += 1
            time.sleep(RETRY_DELAY)
    print("Failed to connect to Uno after several attempts.")
    return None

# Initialize the connection
arduino = connect_to_uno()

# Mediapipe setup for hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)
mp_draw = mp.solutions.drawing_utils

# OpenCV setup for video capture (use cv2.VideoCapture(1) to access second webcam)
WIDTH, HEIGHT = 640, 480
cap = cv2.VideoCapture(1)  # Use the second webcam (if available)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Mapping function
def map_value(value, from_min, from_max, to_min, to_max):
    return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min

# Send data to Arduino
def send_to_uno(x, y):
    global arduino
    if arduino is None or not arduino.is_open:
        print("Error: Arduino connection not available.")
        return

    try:
        # BASE ROTATION – X axis (left/right hand motion)
        angle_base = int(map_value(x, 0, WIDTH, 0, 180))  # Left to right hand maps to 0–180

        # SHOULDER – Y axis (up/down hand motion)
        angle_shoulder = int(map_value(y, 0, HEIGHT, 180, 0))  # Upwards hand movement = shoulder goes up, down goes down

        # ELBOW – based on how far your hand is from the center
        center_x, center_y = WIDTH // 2, HEIGHT // 2
        dist = math.hypot(x - center_x, y - center_y)
        angle_elbow = int(map_value(dist, 0, math.hypot(WIDTH // 2, HEIGHT // 2), 90, 0))  # Fold in as hand moves away

        # Clamp angles to valid servo range
        angle_base = max(0, min(180, angle_base))
        angle_shoulder = max(0, min(180, angle_shoulder))  # Should be between 0-180, adjust as needed
        angle_elbow = max(0, min(90, angle_elbow))

        # Send angles to Arduino
        command = f"{angle_base},{angle_shoulder},{angle_elbow}\n"
        arduino.write(command.encode())
        print(f"[TX] Sent: {command.strip()}")

    except (serial.SerialException, serial.SerialTimeoutException) as e:
        print(f"[ERROR] Serial write failed: {e}")
        arduino.close()
        arduino = connect_to_uno()
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")

# Main loop
try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from webcam.")
            break

        frame = cv2.flip(frame, 1)  # Flip the frame horizontally
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                index = hand_landmarks.landmark[8]  # Index finger tip
                x = int(index.x * WIDTH)
                y = int(index.y * HEIGHT)

                send_to_uno(x, y)

                # Draw circle at index finger and display coordinates
                cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)
                cv2.putText(frame, f"X: {x}, Y: {y}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        frame = cv2.resize(frame, (960, 720))  # Resize for display
        cv2.imshow("Hand Tracking", frame)  # Display the frame

        # Limit frame rate (ESC to quit)
        if cv2.waitKey(1) & 0xFF == 27:  
            break

        time.sleep(0.01)  # Light delay to reduce CPU usage

except KeyboardInterrupt:
    print("\nProgram terminated by user")

finally:
    print("Cleaning up...")
    cap.release()  # Release the webcam
    cv2.destroyAllWindows()  # Close the OpenCV window
    if arduino:
        arduino.close()  # Close the serial connection
