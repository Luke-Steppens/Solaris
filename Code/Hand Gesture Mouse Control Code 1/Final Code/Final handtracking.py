import cv2
import mediapipe as mp
import serial
import time
import os

# Serial configuration
COM_PORT = 'COM4'
BAUD_RATE = 115200
WIDTH, HEIGHT = 640, 480

# Connect to Arduino
def connect_to_uno():
    for _ in range(5):
        try:
            if os.path.exists(f'\\\\.\\{COM_PORT}'):
                arduino = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
                time.sleep(2)  # Allow time to establish connection
                print("Connected to Arduino Uno")
                return arduino
        except Exception as e:
            print(f"[ERROR] {e}")
            time.sleep(2)
    print("Failed to connect to Arduino.")
    return None

arduino = connect_to_uno()

# Setup MediaPipe Hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)
mp_draw = mp.solutions.drawing_utils

# OpenCV camera setup
cap = cv2.VideoCapture(0)
cap.set(3, WIDTH)
cap.set(4, HEIGHT)

# Map function for angles
def map_value(val, in_min, in_max, out_min, out_max):
    return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Send angles to Arduino for base, shoulder, and elbow
def send_angles(x, y):
    global arduino
    if not arduino or not arduino.is_open:
        print("[ERROR] Arduino not connected")
        return

    flipped_x = WIDTH - x  # Flip X for natural hand movement

    # Map X coordinate to base rotation (left/right)
    angle_base = int(map_value(flipped_x, 0, WIDTH, 0, 180))

    # Map Y coordinate to shoulder movement (up/down)
    angle_shoulder = int(map_value(y, 0, HEIGHT, 30, 150))  # Adjust range for smooth control

    # Fixed elbow position to stabilize movement
    angle_elbow = 90  # Adjust this if needed

    # Clamp values
    angle_base = max(0, min(180, angle_base))
    angle_shoulder = max(0, min(180, angle_shoulder))

    try:
        cmd = f"{angle_base},{angle_shoulder},{angle_elbow}\n"
        arduino.write(cmd.encode())
        print(f"[TX] Base: {angle_base}, Shoulder: {angle_shoulder}, Elbow: {angle_elbow}")
    except Exception as e:
        print(f"[ERROR] Serial write failed: {e}")
        arduino.close()
        arduino = connect_to_uno()

# Main loop
try:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Camera read failed.")
            err = f"[ERROR]"
            arduino.write(err.encode())
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Use index finger tip for tracking
                index_finger = hand_landmarks.landmark[8]
                x = int(index_finger.x * WIDTH)
                y = int(index_finger.y * HEIGHT)

                # Send angles to Arduino
                send_angles(x, y)

                # Visualize the tracked point
                cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)
                cv2.putText(frame, f"X:{x} Y:{y}", (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Hand Tracking - Full X & Y Control", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key to break
            break

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    print("Cleaning up...")
    cap.release()
    cv2.destroyAllWindows()
    if arduino:
        arduino.close()
