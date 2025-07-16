import cv2
import mediapipe as mp
import pygame  # NEW: Import Pygame for the dot movement

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# Initialize Pygame Window
pygame.init()

# Set Pygame Screen Dimensions 
WIDTH, HEIGHT = 640, 480  # Increased screen size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hand Controlled Dot")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set up Pygame font
font = pygame.font.Font(None, 24)
text_surface = font.render("Please click 'Escape' if you have to exit the code.", True, WHITE)
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Display message before starting the game
screen.fill(BLACK)
screen.blit(text_surface, text_rect)
pygame.display.update()
pygame.time.delay(2000)  # Display message for 2 seconds

# Initial Position of the Dot in the Center
dot_x = WIDTH // 2
dot_y = HEIGHT // 2
dot_radius = 10  # Increased dot size for better visibility

# Open Camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read Frame from Camera
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for mirror effect
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the Frame
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get Index Finger Tip (Landmark ID 8)
            index_finger_tip = hand_landmarks.landmark[8]
            x = int(index_finger_tip.x * w)  # Convert normalized hand coordinates to pixel values
            y = int(index_finger_tip.y * h)

            # Convert hand coordinates to match Pygame screen size
            dot_x = int(index_finger_tip.x * WIDTH)
            dot_y = int(index_finger_tip.y * HEIGHT) 

            # Draw Circle on Index Finger Tip for Reference
            cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)

    # Display Hand Tracking Window
    cv2.imshow("Hand Tracking", frame)

    # Quit with ESC (27)
    if cv2.waitKey(1) & 0xFF == 27:
        break

    # Update Pygame Window with the Moving Dot
    screen.fill(BLACK)  # Clear screen
    pygame.draw.circle(screen, GREEN, (dot_x, dot_y), dot_radius)  # Draw the dot
    pygame.display.update()  # Refresh the screen

# Release Resources
cap.release()
cv2.destroyAllWindows()
pygame.quit()
