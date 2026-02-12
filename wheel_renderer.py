import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the drawing window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Wheel settings
wheel_color = (255, 223, 0)
wheel_radius = 250
center = (screen_width // 2, screen_height // 2)

# Game UI settings
font = pygame.font.Font(None, 36)

def draw_wheel():
    pygame.draw.circle(screen, wheel_color, center, wheel_radius)
    for i in range(10):  # Draw 10 segments
        angle = (360 / 10) * i
        x_start = center[0] + wheel_radius * 0.8 * pygame.math.cos(pygame.math.radians(angle))
        y_start = center[1] + wheel_radius * 0.8 * pygame.math.sin(pygame.math.radians(angle))
        x_end = center[0] + wheel_radius * pygame.math.cos(pygame.math.radians(angle))
        y_end = center[1] + wheel_radius * pygame.math.sin(pygame.math.radians(angle))
        pygame.draw.line(screen, (0, 0, 0), (x_start, y_start), (x_end, y_end), 2)  

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Fill the background with white
        draw_wheel()
        pygame.display.flip()  # Update the display

    pygame.quit()

if __name__ == '__main__':
    main()