import cv2
import requests

url = 'http://<ESP32-CAM_IP>/stream'  # Replace with your ESP32-CAM's IP address

# Open the stream using OpenCV
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Display the frame
    cv2.imshow("ESP32-CAM Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
