import cv2
import mediapipe
import pyautogui
capture_hands = mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
# Code for the camera to turn on when run 
camera = cv2.VideoCapture(0)
x1 = y1 = x2 = y2 = 0
while True:
    _,image = camera.read()
    image_height, image_width, _ = image.shape
    #converting / fliping the captured image to be the right side and making it and rgb image
    image = cv2.flip(image,1)
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output_hands = capture_hands.process(rgb_image)
    all_hands = output_hands.multi_hand_landmarks
    # when hand is seen it will create landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image, hand)
            one_hand_landmarks = hand.landmark
            for id, lm in enumerate(one_hand_landmarks):
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)
                print(x, y)
                # finding the index finger and thumb and trying to draw a circle over it, since we want to find the index and the thumb.
                if id == 8:
                    mouse_x = int(screen_width / image_width * x)
                    mouse_y = int(screen_height / image_height * y)
                    pyautogui.moveTo(mouse_x,mouse_y)
                    x1 = x
                    y1 = y
                    cv2.circle(image,(x,y),15,(0,255,255)) # setting the circle radius, and rgb value
                if id == 4:
                    x2 = x
                    y2 = y
                    cv2.circle(image,(x,y),15,(0,255,255))
        dist = y2 - y1
        print(dist)
        if(dist<20):
            pyautogui.click()
            print("clicked")
    cv2.imshow("Hand movement video capture",image)
    key = cv2.waitKey(100)
    #value of an escape key is 27 hence to check if the key intered is to leave the progeam verifying value
    if key == 27:
        break
camera.release()
cv2.destroyAllWindows()