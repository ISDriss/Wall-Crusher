import pygame
import random
from grids import Wall,Grid,Cursor

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