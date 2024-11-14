import pygame
import random
from var import WALL_COLOR, WALL_SPRITES, WHITE

#a wall is 1 cell of the grid, the wall type determines if the wall is 
#indestructible (-1), destroyed (0), or destructible (1 to inf)
class Wall:
    level: int 
    rect: pygame.Rect

    def __init__(self, type, rect):
        self.level = type
        self.rect = rect
    
    def draw(self, screen): 
        screen.blit(WALL_SPRITES[0][self.level], self.rect)
        #pygame.draw.rect(screen, WALL_COLOR[self.level + 1], self.rect)

    def punch(self, player):
        player.NB_OF_PUNCHES += 1

        if(self.level >0):
            self.level -= 1

            if(self.level == 0):
                player.BRICKS_BROKEN += 1
        
        else:
            if(self.level == 0):
                player.MISS += 1

class Grid:
    size: int
    cell_size: int
    walls: list[list[Wall]]

    def __init__(self, size, cell_size):
        self.size = size
        self.cell_size = cell_size
        
        # Create an empty wall
        self.walls = [
            [
                Wall(0, pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
                for col in range(size)
            ]
            for row in range(size)
        ]

    #Set a wall based on a template, if a template isn't provided set to a level 0 wall
    def set_walls(self, temp: list[list[int]] = None):    
        for row in range(self.size):
            for col in range(self.size):
                self.walls[row][col].level = temp[row][col] if temp else 0

    #TO DO: add difficulty scalar to change the probabilities and slowly add higher level walls
    def random_walls(self): 
        for row in self.walls:
            for wall in row:
                wall.level = random.choice([-1, 0, 1])  # Change the level to a new value
    
    # Draw the grid
    def draw(self, screen, cursor):
        for row in self.walls:
            for wall in row:
                wall.draw(screen)
        
        cursor.draw(screen, self.cell_size)
    
    #check if all the destructible wall are level 0
    def is_crushed(self):
        crushed = True
        for row in self.walls:
            for wall in row:
                if(wall.level > 0):
                    crushed = False
        return crushed
                
class Cursor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen, cell_size):
        pygame.draw.rect(screen, WHITE, pygame.Rect(self.x * cell_size, self.y * cell_size, cell_size, cell_size), 3)