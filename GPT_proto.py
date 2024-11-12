import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wall Crusher")

# Game variables
cursor_pos = [1, 1]  # Starting in the center of the grid
hp = 3
round_time_limit = 3000  # Timer in milliseconds
timer = round_time_limit
clock = pygame.time.Clock()

# Function to generate a new wall grid
def generate_new_walls():
    return [['D' if random.random() > 0.3 else 'I' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)], \
           [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Initial wall setup
walls, holes = generate_new_walls()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and cursor_pos[0] > 0:
                cursor_pos[0] -= 1
            elif event.key == pygame.K_RIGHT and cursor_pos[0] < GRID_SIZE - 1:
                cursor_pos[0] += 1
            elif event.key == pygame.K_UP and cursor_pos[1] > 0:
                cursor_pos[1] -= 1
            elif event.key == pygame.K_DOWN and cursor_pos[1] < GRID_SIZE - 1:
                cursor_pos[1] += 1
            elif event.key == pygame.K_SPACE:
                # Punching mechanic
                x, y = cursor_pos
                if walls[y][x] == 'D':  # Only punch destructible walls
                    holes[y][x] = True
                    walls[y][x] = 'H'  # Change wall state to "Hole"

    # Draw the grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            if holes[row][col]:
                pygame.draw.rect(screen, GREEN, rect)  # Draw hole
            elif walls[row][col] == 'D':
                pygame.draw.rect(screen, BLUE, rect)  # Destructible wall
            elif walls[row][col] == 'I':
                pygame.draw.rect(screen, RED, rect)  # Indestructible wall

            # Draw cursor
            if cursor_pos == [col, row]:
                pygame.draw.rect(screen, BLACK, rect, 3)

    # Timer logic
    timer -= clock.get_time()
    if timer <= 0:
        if not holes[cursor_pos[1]][cursor_pos[0]]:  # Check if the cursor is over a hole
            hp -= 1
        # Generate a new grid and reset timer
        walls, holes = generate_new_walls()
        timer = round_time_limit

    # Game Over condition
    if hp <= 0:
        print("Game Over!")
        running = False

    # Display HP and timer
    font = pygame.font.SysFont(None, 36)
    hp_text = font.render(f"HP: {hp}", True, BLACK)
    timer_text = font.render(f"Time: {max(timer // 1000, 0)}s", True, BLACK)
    screen.blit(hp_text, (10, 10))
    screen.blit(timer_text, (WIDTH - 150, 10))

    # Update the display and tick the clock
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
