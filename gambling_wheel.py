import pygame
import random

# Initializing Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gambling Wheel')

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game variables
WHEEL_NUMBERS = list(range(0, 37))  # 0-36 numbers
JACKPOT_NUMBER = 7                  # Jackpot on number 7
SPINNING_SPEED = 5                   # Base spin speed

class GamblingWheel:
    def __init__(self):
        self.angle = 0
        self.spin_speed = SPINNING_SPEED
        self.jackpot_count = 0

    def spin_wheel(self):
        # Increase spin speed for odd numbers
        if random.choice(WHEEL_NUMBERS) % 2 != 0:
            self.spin_speed += 2
        self.angle += self.spin_speed
        self.angle = self.angle % 360  # Looping angle

        # Check jackpot condition
        landed_number = random.choice(WHEEL_NUMBERS)
        if landed_number == JACKPOT_NUMBER:
            self.jackpot_count += 1
            print('Jackpot! You hit the jackpot on number', landed_number)
        return landed_number

    def draw_wheel(self):
        # Drawing code here (wheel visuals - placeholder)
        pygame.draw.circle(screen, GREEN, (WIDTH // 2, HEIGHT // 2), 200)
        # More drawing logic...

    def reset_speed(self):
        self.spin_speed = SPINNING_SPEED

# Main game loop
if __name__ == '__main__':
    wheel = GamblingWheel()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        wheel.draw_wheel()
        landed_number = wheel.spin_wheel()  # Spin the wheel each frame
        print('Landed on:', landed_number)
        pygame.display.flip()
        pygame.time.delay(500)  # Delay for visual slowing

    pygame.quit()