import pygame

# Screen dimensions and settings
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE

# Setup the screen
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wall Crusher")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

WALL_COLOR = (
    RED,
    BLACK,
    YELLOW,
    BLUE,
    GREEN
)

#wall Sprites
METAL = pygame.transform.scale( pygame.image.load("sprites/metal.png").convert_alpha(), (CELL_SIZE, CELL_SIZE))
WALL_SPRITES = (
    (
        pygame.transform.scale( pygame.image.load("sprites/wall1_4.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        pygame.transform.scale( pygame.image.load("sprites/wall1_2.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        pygame.transform.scale( pygame.image.load("sprites/wall1_1.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        pygame.transform.scale( pygame.image.load("sprites/wall1_0.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        METAL
    ),
    (
        pygame.transform.scale( pygame.image.load("sprites/wall2_4.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        pygame.transform.scale( pygame.image.load("sprites/wall2_2.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        pygame.transform.scale( pygame.image.load("sprites/wall2_1.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        pygame.transform.scale( pygame.image.load("sprites/wall2_0.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        METAL
    )
)