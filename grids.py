import pygame
import random

#a wall is 1 cell of the grid, the wall type determines if the wall is 
# indestructible (-1), destroyed (0), or destructible (1 to inf)
class Wall:
    level: int 
    rect: pygame.Rect

    def __init__(self, type, rect):
        self.level = type
        self.rect = rect
    
    def punch(self):
        if(self.level >0):
            self.level -= 1

class Grid:
    size: int
    cell_size: int
    walls: list[list[Wall]]

    def __init__(self, size, cell_size):
        self.size = size
        self.cell_size = cell_size
        
        # Create a 2D list of Wall objects using list comprehension
        self.walls = [
            [
                Wall(0, pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
                for col in range(size)
            ]
            for row in range(size)
        ]

    #TO DO: add difficulty scalar to change the probabilities and slowly add higher level walls
    def new_walls(self): 
        # Update the level of each wall in the existing grid
        for row in self.walls:
            for wall in row:
                wall.level = random.choice([-1, 0, 1])  # Change the level to a new value (can adjust logic as needed)

class Cursor:
    def __init__(self, x, y):
        self.x = x
        self.y = y