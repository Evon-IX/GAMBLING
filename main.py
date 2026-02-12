import pygame
import time
import random
from game_manager import GameManager

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gambling Wheel")
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
font_large = pygame.font.Font(None, 72)
font_medium = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)
game = GameManager()

class WheelRenderer:
    def __init__(self):
        self.center_x = WIDTH // 2
        self.center_y = HEIGHT // 2
        self.radius = 150
        self.rotation = 0

    def draw(self, surface, current_number=None):
        pygame.draw.circle(surface, GOLD, (self.center_x, self.center_y), self.radius)
        pygame.draw.circle(surface, BLACK, (self.center_x, self.center_y), self.radius, 3)
        for i in range(10):
            angle = (360 / 10) * i + self.rotation
            start_angle = angle - 18
            end_angle = angle + 18
            pygame.draw.wedge(surface, WHITE, (self.center_x, self.center_y), self.radius, start_angle, end_angle, 2)
            rad = (angle * 3.14159) / 180
            text_x = self.center_x + (self.radius - 40) * pygame.math.cos(pygame.math.radians(angle))
            text_y = self.center_y + (self.radius - 40) * pygame.math.sin(pygame.math.radians(angle))
            number_text = font_medium.render(str(i), True, BLACK)
            surface.blit(number_text, (text_x - number_text.get_width()//2, text_y - number_text.get_height()//2))
        pygame.draw.polygon(surface, RED, [(self.center_x, self.center_y - self.radius - 20), (self.center_x - 10, self.center_y - self.radius), (self.center_x + 10, self.center_y - self.radius)])

    def spin(self, duration=2.0):
        start_time = time.time()
        start_rotation = self.rotation
        spin_amount = 360 * random.randint(3, 8)
        while time.time() - start_time < duration:
            elapsed = time.time() - start_time
            progress = elapsed / duration
            self.rotation = start_rotation + (spin_amount * progress)


def draw_ui():
    state = game.get_game_state()
    money_text = font_medium.render(f"Money: ${state['money']}", True, WHITE)
    screen.blit(money_text, (20, 20))
    jp_text = font_small.render(f"Jackpot: 1/{{int(1/state['jackpot_probability'])}}", True, WHITE)
    screen.blit(jp_text, (20, 60))
    st_text = font_small.render(f"Spin Time: {{state['spin_time']:.1f}}s", True, WHITE)
    screen.blit(st_text, (20, 90))
    oe_text = font_small.render(f"Odds: {{state['odd_count']}} | Evens: {{state['even_count']}}", True, WHITE)
    screen.blit(oe_text, (20, 120))
    jp_won = font_small.render(f"Jackpots Won: {{state['jackpot_payouts']}}", True, GOLD)
    screen.blit(jp_won, (20, 150))
    inst_text = font_small.render("Press SPACE to spin | Press Q to quit", True, WHITE)
    screen.blit(inst_text, (WIDTH - 350, HEIGHT - 30))


def main():
    wheel = WheelRenderer()
    running = True
    spinning = False
    spin_cooldown = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not spinning and spin_cooldown <= 0:
                    spinning = True
                    spin_cooldown = game.get_spin_time() + 0.5
                elif event.key == pygame.K_q:
                    running = False

        if spinning:
            wheel.spin(game.get_spin_time())
            result = game.spin_wheel()
            game.process_spin_result(result)
            game.deduct_spin_cost()
            if game.check_jackpot():
                payout = game.trigger_jackpot()
                game.money += payout
                print(f"JACKPOT! Won ${payout}")
            spinning = False
        if spin_cooldown > 0:
            spin_cooldown -= 1/60

        screen.fill(GREEN)
        wheel.draw(screen)
        draw_ui()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()