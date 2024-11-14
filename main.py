import pygame
import csv
import random
from visual import WHITE, BLACK, BLUE, WIDTH, HEIGHT, GRID_SIZE, CELL_SIZE
from grids import Wall,Grid,Cursor
from player import Player


# Initialize Pygame
pygame.init()

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game variables
grid = Grid(GRID_SIZE, CELL_SIZE)   # Game grid
cursor = Cursor(1, 1)               # Starting in the center of the grid
clock = pygame.time.Clock()

# Fonts
menu_font = pygame.font.Font("pixelmax\Pixelmax-Regular.otf", 72)
select_font = pygame.font.Font("pixelmax\Pixelmax-Regular.otf", 42)
font = pygame.font.Font("pixelmax\Pixelmax-Regular.otf", 24)
score_font = pygame.font.SysFont(None, 36)

# Menu methods
def render_menu(title, options, selected):
    screen.fill(BLACK)
    menu_title = menu_font.render(title, True, WHITE)
    screen.blit(menu_title, (WIDTH // 2 - menu_title.get_width() // 2, HEIGHT // 8))
    for i, option in enumerate(options):
        color = BLUE if i == selected else WHITE
        option_text = select_font.render(option, True, color)
        screen.blit(option_text, (WIDTH // 2 - option_text.get_width() // 2, HEIGHT // 3 + i * 50))
    pygame.display.flip()

def navigate_menu(options, selected):
    return

# Menus
# Menu function to handle selections
def main_menu():
    menu_options = ["Levels", "Endless", "Leaderboards", "Quit"]
    selected_option = 0
    menu_running = True
    while menu_running:
        render_menu("Wall Crusher",menu_options, selected_option)

        # Handle events for menu navigation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Levels
                        levels_menu()
                    elif selected_option == 1:  # Endless
                        menu_running = False
                        endless_game()
                    elif selected_option == 2:  # Leaderboards
                        show_leaderboards()
                    elif selected_option == 3: # Quit
                        pygame.quit()

# Levels menu function
def levels_menu():
    level_options = ["Level ONE", "Level TWO", "Level THREE"]
    selected_level = 0
    levels_running = True
    while levels_running:
        render_menu("Level Select",level_options, selected_level)

        # Handle events for levels menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                levels_running = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    levels_running = False
                elif event.key == pygame.K_UP:
                    selected_level = (selected_level - 1) % len(level_options)
                elif event.key == pygame.K_DOWN:
                    selected_level = (selected_level + 1) % len(level_options)
                elif event.key == pygame.K_RETURN:
                    # Add functionality to load levels or return to the main menu
                    return

# Leaderboards function (placeholder for future implementation)
def show_leaderboards():
    leaderboard_running = True
    while leaderboard_running:
        screen.fill(BLACK)
        leaderboard_text = menu_font.render("Leaderboards", True, WHITE)
        screen.blit(leaderboard_text, (WIDTH // 2 - leaderboard_text.get_width() // 2, HEIGHT // 10))

        # Example placeholder leaderboard content
        with open('data/players.csv', 'r', encoding="utf-8", newline='') as file:
            readr = csv.reader(file)
            next(readr)
            leaderboard_data = sorted([row for row in readr], key=lambda x: int(x[4]), reverse=True)
        
        text = font.render(f"Name | Punch | Broken | Walls | Miss", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))
        offset = 30
        for entry in leaderboard_data[:10]:
            text = score_font.render(f"{entry[1]}: {entry[2]},  {entry[3]},  {entry[4]},  {entry[5]}", True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4 + offset))
            offset += 30
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leaderboard_running = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:  # Return to main menu
                    leaderboard_running = False

# Player name input screen
def get_player_name():
    input_active = True
    player_name = ""
    while input_active:
        screen.fill(BLACK)
        prompt_text = menu_font.render("Enter Name:", True, WHITE)
        name_display = select_font.render(player_name, True, WHITE)
        
        # Center the text
        screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, HEIGHT // 3))
        screen.blit(name_display, (WIDTH // 2 - name_display.get_width() // 2, HEIGHT // 2))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(player_name) > 0:  # Ensure the name isn't empty
                        input_active = False  # Confirm input and exit loop
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]  # Remove last character
                elif len(player_name) < 5 and event.unicode.isprintable():
                    player_name += event.unicode  # Add typed character
    return player_name

# Game Methods
def game_event(player):
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
                grid.walls[cursor.y][cursor.x].punch(player)

def game_HUD(player, timer):
    hp_text = score_font.render(f"HP: {player.HP}", True, BLUE)
    timer_text = score_font.render(f"Time: {max(timer // 1000, 0)}s", True, BLUE)
    screen.blit(hp_text, (10, 10))
    screen.blit(timer_text, (WIDTH - 150, 10))  

def game_over(player):
    if player.HP <= 0:
        print("Game Over!")
        player.save()
        running = False

# Endless game loop
def endless_game(): 
    player = Player()                   # New player
    time_limit = 3000  # Timer in milliseconds
    timer = time_limit
    running = True

    player.NAME = get_player_name()
    while running:
        screen.fill(BLACK)

        game_event(player)
        
        # Draw the game
        grid.draw(screen, cursor)

        # Round
        timer -= clock.get_time()
        if timer <= 0:
            if grid.is_crushed() != True:  # Check if the wall isn't crushed
                player.HP -= 1
            else:
                player.WALLS_PASSED += 1
        
            # Generate a new grid and reset timer
            grid.random_walls()
            timer = time_limit
            player.TIME += time_limit

        # Game Over condition
        game_over(player)

        # Display HP and timer
        game_HUD(player, timer)

        # Update the display and tick the clock
        pygame.display.flip()
        clock.tick(30)

main_menu()