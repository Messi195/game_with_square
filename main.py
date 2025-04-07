import pygame
import random

# Initialize pygame
pygame.init()

# --- Window settings ---
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# --- Player parameters ---
player_width, player_height = 50, 50
player_speed = 10

# --- Enemy parameters ---
enemy_width, enemy_height = 50, 50

# --- Function to draw text ---
def draw_text(text: str, x: int, y: int, color: tuple[int, int, int], size: int = 36) -> None:
    """
    Draws text on the screen at the specified position with the specified color.

    Args:
        text (str): The text to display.
        x (int): The x-coordinate of the text.
        y (int): The y-coordinate of the text.
        color (tuple[int, int, int]): The color of the text in RGB format.
        size (int): The font size of the text. Default is 36.
    """
    font = pygame.font.Font(None, size)
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# --- Finish screen function ---
def finish_screen(score: int) -> None:
    """
    Displays the finish screen with the final score and restart instructions.

    Args:
        score (int): The player's final score.
    """
    screen.fill(BLACK)
    draw_text("GAME OVER!", 220, 200, WHITE, size=50)
    draw_text(f"Your score: {score}", 310, 300, WHITE, size=40)
    draw_text("Press [ESC] to exit", 245, 400, WHITE, size=30)
    draw_text("Press [R] to restart", 220, 450, WHITE, size=30)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_r:
                    return

# --- Main game function ---
def main_game() -> None:
    """
    Runs the main game loop, handling player movement, enemy interactions, and game progression.

    The player controls a blue rectangle, trying to collide with red enemies that randomly appear.
    The game has a timer, and the player earns points by touching the enemies.
    """
    global score
    player_x, player_y = 100, 300
    enemy_x = random.randint(0, 750)
    enemy_y = random.randint(0, 550)

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    score = 0
    start_ticks = pygame.time.get_ticks()
    game_duration = 10

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        remaining_time = max(0, int(game_duration - elapsed_time))

        if remaining_time == 0:
            break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < window_size[0] - player_width:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < window_size[1] - player_height:
            player_y += player_speed

        player_rect.topleft = (player_x, player_y)

        if player_rect.colliderect(enemy_rect):
            score += 1
            enemy_x = random.randint(0, 750)
            enemy_y = random.randint(0, 550)
            enemy_rect.topleft = (enemy_x, enemy_y)

        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, player_rect)
        pygame.draw.rect(screen, RED, enemy_rect)
        draw_text(f"Score: {score}", 10, 10, WHITE)
        draw_text(f"Time: {remaining_time} sec", 10, 40, WHITE)

        pygame.display.flip()
        clock.tick(60)

    finish_screen(score)

# --- Main program loop ---
while True:
    main_game()
