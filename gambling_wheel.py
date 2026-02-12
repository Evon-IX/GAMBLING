import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
JACKPOT_PROBABILITY = lambda k: 1/(239 - 8*k)
START_MONEY = 777
RESET_MONEY = 0
SPIN_TIME_MIN = 1.5
SPIN_TIME_MAX = 3.0

# Game State Variables
money = START_MONEY
k, e = 0, 0  # counters for odd/even

# Pygame settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gambling Wheel')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 74)

def draw_wheel(number):
    screen.fill((0, 0, 0))  # Clear the screen
    text = font.render(str(number), True, (255, 255, 255))
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    pygame.display.flip()

def spin_wheel():
    global money, k, e
    spin_time = random.uniform(SPIN_TIME_MIN, SPIN_TIME_MAX)
    result = random.randint(0, 9)
    draw_wheel(result)
    time.sleep(spin_time)
    return result

def update_game_state(result):
    global k, e, money
    if result % 2 == 0:
        e += 1
    else:
        k += 1
    if random.random() < JACKPOT_PROBABILITY(k):
        payout = 100  # example payout
        money += payout
        print(f'Jackpot! Payout: {payout}')
    if money <= 0:
        money = RESET_MONEY

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    result = spin_wheel()
    update_game_state(result)
    print(f'Money: {money}, Odds: {k}, Evens: {e}')
    clock.tick(60)  # 60 frames per second

pygame.quit()