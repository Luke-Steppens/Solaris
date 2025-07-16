import cv2

ESP32_CAM_URL = "http://172.20.10.10:81/stream"
cap = cv2.VideoCapture(ESP32_CAM_URL)

if not cap.isOpened():
    print("Error: Cannot connect to ESP32-CAM stream.")
    exit()

print("Connected. Press ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to receive frame.")
        break

    frame = cv2.resize(frame, (640, 480))
    cv2.imshow("ESP32-CAM Stream", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
