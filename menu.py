import pygame
import sys

# initialize Pygame
pygame.init()

# set the window size
window_width = 800
window_height = 600
window_color = (255, 255, 255)

# create the window
window = pygame.display.set_mode((window_width, window_height))

font = pygame.font.SysFont('Arial', 32)

#create buttons
level_6_button = pygame.Rect(100, 100, 200, 50)
level_9_button = pygame.Rect(100, 200, 200, 50)
level_12_button = pygame.Rect(100, 300, 200, 50)
time_30_sec_button = pygame.Rect(400, 100, 200, 50)
time_60_sec_button = pygame.Rect(400, 200, 200, 50)
time_90_sec_button = pygame.Rect(400, 300, 200, 50)

start_game_button = pygame.Rect(300, 400, 200, 50)

#variables
level = 6
time = 30

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if level_6_button.collidepoint(event.pos):
                level = 6
            elif level_9_button.collidepoint(event.pos):
                level = 9
            elif level_12_button.collidepoint(event.pos):
                level = 12
            elif time_30_sec_button.collidepoint(event.pos):
                time = 30
            elif time_60_sec_button.collidepoint(event.pos):
                time = 60
            elif time_90_sec_button.collidepoint(event.pos):
                time = 90
            elif start_game_button.collidepoint(event.pos):
                print(f"Starting game with level {level} and time {time} seconds")

    window.fill(window_color)

    # draw the buttons on the screen
    pygame.draw.rect(window, (255, 0, 0), level_6_button)
    pygame.draw.rect(window, (255, 0, 0), level_9_button)
    pygame.draw.rect(window, (255, 0, 0), level_12_button)
    pygame.draw.rect(window, (255, 0, 0), time_30_sec_button)
    pygame.draw.rect(window, (255, 0, 0), time_60_sec_button)
    pygame.draw.rect(window, (255, 0, 0), time_90_sec_button)
    pygame.draw.rect(window, (255, 0, 0), start_game_button)
    level_6_text = font.render("Level 6", True, (255, 255, 255))
    level_9_text = font.render("Level 9", True, (255, 255, 255))
    level_12_text = font.render("Level 12", True, (255, 255, 255))
    time_30_sec_text = font.render("30 sec", True, (255, 255, 255))
    time_60_sec_text = font.render("60 sec", True, (255, 255, 255))
    time_90_sec_text = font.render("90 sec", True, (255, 255, 255))
    start_game_text = font.render("Start Game", True, (255, 255, 255))

    window.blit(level_6_text, level_6_button)
    window.blit(level_9_text, level_9_button)
    window.blit(level_12_text, level_12_button)
    window.blit(time_30_sec_text, time_30_sec_button)
    window.blit(time_60_sec_text, time_60_sec_button)
    window.blit(time_90_sec_text, time_90_sec_button)
    window.blit(start_game_text, start_game_button)

    # update the display
    pygame.display.flip()

