import pygame
import random
from var import WHITE, BLACK, WIDTH, HEIGHT, GRID_SIZE, CELL_SIZE
from grids import Wall,Grid,Cursor

# Initialize Pygame
pygame.init()

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wall Crusher")

# Game variables
grid = Grid(GRID_SIZE, CELL_SIZE)   # Game grid
cursor = Cursor(1, 1)               # Starting in the center of the grid
hp = 3
round_time_limit = 3000  # Timer in milliseconds
timer = round_time_limit
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Movement
            if event.key == pygame.K_LEFT and cursor.x > 0:
                cursor.x -= 1
            elif event.key == pygame.K_RIGHT and cursor.x < GRID_SIZE - 1:
                cursor.x += 1
            elif event.key == pygame.K_UP and cursor.y > 0:
                cursor.y -= 1
            elif event.key == pygame.K_DOWN and cursor.y < GRID_SIZE - 1:
                cursor.y += 1
            
            # Punching mechanic
            elif event.key == pygame.K_SPACE: 
                grid.walls[cursor.y][cursor.x].punch()

    # Draw the game
    grid.draw(screen, cursor)

    # Round
    timer -= clock.get_time()
    if timer <= 0:
        if grid.is_crushed() != True:  # Check if the wall is crushed
            hp -= 1
        
        # Generate a new grid and reset timer
        grid.random_walls()
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