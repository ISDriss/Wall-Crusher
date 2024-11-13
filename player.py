import csv

class Player:
    ID: int
    NAME: str
    HP: int
    NB_OF_PUNCHES: int
    BRICKS_BROKEN: int
    WALLS_PASSED: int
    MISS: int
    TIME: int

    global_id = 1

    def __init__(self, name = None):

        with open('data/players.csv', 'r', encoding="utf-8", newline='') as file:
            last_id = int(file.readlines()[-1].split(',')[0])
        
        global_id = last_id + 1
        self.ID = global_id
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
    
    def save(self):
        # Writing data to a CSV file
        data =[   
            self.ID,
            self.NAME,
            self.NB_OF_PUNCHES,
            self.BRICKS_BROKEN,
            self.WALLS_PASSED,
            self.MISS,
            self.TIME]
    
        with open('data/players.csv', 'a', encoding="utf-8", newline='') as file:
            writr = csv.writer(file)
            writr.writerow(data)

        print("Data saved to output csv")