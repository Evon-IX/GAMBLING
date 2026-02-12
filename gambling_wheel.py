import pygame
import random

# Constants and Settings
WIDTH, HEIGHT = 800, 600
FPS = 60
jackpot_base = 239
max_jackpot_probability = 1 / 25
start_money = 777
money = start_money

# State Management
state = "menu"
spin_result = None
spins = []
jackpot_thresholds = {}  # To track jackpot states

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gambling Wheel")
clock = pygame.time.Clock()

# UI setup
font = pygame.font.Font(None, 36)

# Function to calculate jackpot probability
def jackpot_probability(k):
    p_k = 1 / (jackpot_base - 8 * k)
    return min(p_k, max_jackpot_probability)

# Function to spin the wheel
def spin_wheel():
    global money, spins, spin_result
    if money <= 0:
        reset_game()
        return
    spin_result = random.randint(0, 36)  # Simulating a standard wheel
    spins.append(spin_result)
    money -= 10  # Cost to spin

    # Check for jackpot
    if random.random() < jackpot_probability(spin_result):
        money += 100  # Jackpot payout
        reset_game()

# Reset the game
def reset_game():
    global money, spins
    money = start_money
    spins = [] 

# Function to manage the game loop
def game_loop():
    global state
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    spin_wheel()  # Spin when space is pressed

        screen.fill((0, 128, 0))  # Green background
        draw_ui()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Function to draw UI
def draw_ui():
    money_text = font.render(f"Money: ${money}", True, (255, 255, 255))
    spins_text = font.render(f"Last Spins: {spins[-5:]}", True, (255, 255, 255))
    screen.blit(money_text, (20, 20))
    screen.blit(spins_text, (20, 60))

# Start the game
if __name__ == "__main__":
    game_loop()