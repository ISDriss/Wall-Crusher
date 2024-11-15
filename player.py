import os
import csv
import pygame
class Player:
    ID: int
    NAME: str
    HP: int
    NB_OF_PUNCHES: int
    BRICKS_BROKEN: int
    WALLS_PASSED: int
    MISS: int
    TIME: int

    def __init__(self, name = None):
        last_id = 0
        if not os.path.exists('data/players.csv'):
            with open('data/players.csv', 'w', encoding="utf-8", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "NAME", "HP", "NB_OF_PUNCHES", "BRICKS_BROKEN", "WALLS_PASSED", "MISS", "TIME", "LEVEL"])
        
        try:
            with open('data/players.csv', 'r', encoding="utf-8", newline='') as file:
                read = file.readlines()
                if len(read) == 1:
                    last_id = 0
                else:
                    last_id = int(read[-1].split(',')[0])
    
        except (FileNotFoundError, IOError) as e:
            print("Error reading the CSV file:", e)
            pygame.quit()
            exit()
        except Exception as e:
            print("An unexpected error occurred:", e)
            pygame.quit()
            exit()

        self.ID = last_id + 1
        self.NAME = name
        self.HP = 3
        self.NB_OF_PUNCHES = 0
        self.BRICKS_BROKEN = 0
        self.WALLS_PASSED = 0
        self.MISS = 0
        self.TIME = 0
    
    def set(self, hp, punches, broken, walls, miss, time):
        self.HP = hp
        self.NB_OF_PUNCHES = punches
        self.BRICKS_BROKEN = broken
        self.WALLS_PASSED = walls
        self.MISS = miss
        self.TIME = time
    
    def reset(self):
        self.HP = 3
        self.NB_OF_PUNCHES = 0
        self.BRICKS_BROKEN = 0
        self.WALLS_PASSED = 0
        self.MISS = 0
        self.TIME = 0

    def save(self, level  = "unknown"):
        # Writing data to a CSV file
        data =[   
            self.ID,
            self.NAME,
            self.NB_OF_PUNCHES,
            self.BRICKS_BROKEN,
            self.WALLS_PASSED,
            self.MISS,
            self.TIME,
            level]
    
        with open('data/players.csv', 'a', encoding="utf-8", newline='') as file:
            writr = csv.writer(file)
            writr.writerow(data)

        print("Data saved to output csv")