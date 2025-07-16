import time
import keyboard  #For keyboard input simulation
import os  #To clear the terminal screen
import pygame


# Initialize Pygame
pygame.init()

# Screen dimensions (same as your LCD screen: 128x160)
WIDTH, HEIGHT = 128, 160
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Dot Movement Simulation")  

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initial Dot Position
dot_x = WIDTH // 2
dot_y = HEIGHT // 2
dot_radius = 5

# Movement speed
step = 3

# Game loop
running = True
while running:
    pygame.time.delay(100)  # Delay to control speed (similar to time.sleep(0.1))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        dot_y = max(0, dot_y - step)
    if keys[pygame.K_DOWN]:
        dot_y = min(HEIGHT, dot_y + step)
    if keys[pygame.K_LEFT]:
        dot_x = max(0, dot_x - step)
    if keys[pygame.K_RIGHT]:
        dot_x = min(WIDTH, dot_x + step)

    # Update display
    screen.fill(BLACK)  # Clear screen
    pygame.draw.circle(screen, GREEN, (dot_x, dot_y), dot_radius)  # Draw dot
    pygame.display.update()  # Refresh screen

# Quit Pygame when loop exits
pygame.quit()