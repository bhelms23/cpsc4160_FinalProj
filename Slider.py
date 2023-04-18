import pygame
import random

pygame.init()

## Define Variables
size = (1000,800)
boardwidth = 1000
screen = pygame.display.set_mode(size)
timer = pygame.time.Clock()
mover = ""

## function variables
over = False
goHome = False
homeScreen = True
gamescreen = False
gameover = False

## boards
board = []
solvedBoard = []

## Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
## Define the main game color
GameColor = WHITE


## Creating the home screen
def goHome():

    global rect_level1,rect_level2,rect_level3
    title = TITLE.render("SliderPY", False, WHITE)

    Level1 = font.render("3x3", False, WHITE)
    rect_level1 = pygame.draw.rect(screen, GREEN, (boardwidth/2, 372,Level1.get_width(),Level1.get_height()))
    GameColor = GREEN

    Level2 = font.render("4x4", False, WHITE)
    rect_level2 = pygame.draw.rect(screen,(0,0,255),(boardwidth/2, 472,Level2.get_width(),Level2.get_height()))
    GameColor = BLUE

    Level3 = font.render("5x5", False, WHITE)
    rect_level3 = pygame.draw.rect(screen, RED, (boardwidth/2, 572, Level3.get_width(), Level3.get_height()))
    GameColor = RED

    screen.blit(title, (boardwidth/2.5, 272))
    screen.blit(Level1, (boardwidth/2, 372))
    screen.blit(Level2, (boardwidth/2, 472))
    screen.blit(Level3, (boardwidth/2, 572))

## Starting Board
def starting_board():
    x = 1
    for z in range(len(board)):
        for y in range(len(board)):
            r = random.randint(0, len(board)-1)
            c = random.randint(0, len(board)-1)
            while board[r][c] != 0:
                r = random.randint(0, len(board)-1)
                c = random.randint(0, len(board)-1)

            if x != len(board) **2:
                board[r][c] = x
            else:
                board[r][c] = 0
            x += 1

## Checks for solved board
def solved_board():
    a = 1
    for r in range(len(board)):
        for c in range(len(board)):
            if a != len(board)**2:
                board[r][c] = a
                a += 1
            else:
                board[r][c] = 0

## Sets board values to zero (restart etc)
def make_zero():
    for r in range(len(board)):
        for c in range(len(board)):
            board[r][c] = 0

## Finds empty spaces to guide the next move
def empty_space():
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                return (r,c)

## creates the grid move boundries
def boundaries(move):
    blankx, blanky = empty_space()
    tryMove = move
    if tryMove == "left":
        if blanky+1 < len(board[0]):
            return True
    elif tryMove == "right":
        if blanky-1 >= 0:
            return True

    elif tryMove == "up":
        if blankx+1 < len(board):
            return True
    elif tryMove == "down":
        if blankx-1 >= 0:
            return True
    else:
        return False
## acts as the move functionality
def function(move):
    click = move
    blankx, blanky = empty_space()

    if click == "right":
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
    if click == "left":
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
    if click == "up":
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]

    if click == "down":
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]


## Draws the game and all of the rects
def draw():
    global new_rect,solve_rect,Quit_rect
    screen.fill(BLACK)

    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] != 0:
                pygame.draw.rect(screen,(GameColor),(c*(700/int(len(board))),r*(700/int(len(board))),(700/int(len(board)))-1,(700/int(len(board)))-1))
                test = font.render(str(board[r][c]),False,(0,0,0))
                screen.blit(test,(c*(700/int(len(board))) + float((700/int(len(board)))/2) - 16,r*(700/int(len(board))) +float((700/int(len(board)))/2) - 16))
            else:
                pygame.draw.rect(screen, BLACK, (c * (700/int(len(board))), r * (700/int(len(board))), (700/int(len(board))), (700/int(len(board)))))

    newgame = font.render("New Game", False, WHITE)
    new_rect = pygame.draw.rect(screen, BLACK,
                                (720, 500, newgame.get_width(), newgame.get_height()))
    screen.blit(newgame, (720, 500))

    solve = font.render("Solve", False, WHITE)
    solve_rect = pygame.draw.rect(screen, BLACK,(720, 600, solve.get_width(), solve.get_height()))
    screen.blit(solve, (720, 600))

    Quit = font.render("Quit",False,(255,255,255))
    Quit_rect = pygame.draw.rect(screen, BLACK,(720, 400, Quit.get_width(), Quit.get_height()))
    screen.blit(Quit,(720, 400))


font = pygame.font.Font('freesansbold.ttf', 35)
TITLE = pygame.font.Font('freesansbold.ttf',50)
keydown = True
while not over:
    global rect_level1,rect_level2,rect_level3,solve_rect,new_rect,Quit_rect

    if homeScreen:
      screen.fill(BLACK)
      goHome()
      homeScreen = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
        if event.type == pygame.KEYDOWN and keydown:
            if event.key == pygame.K_RETURN and gameover:
                gameover = False
                homeScreen = True
            if event.key == pygame.K_UP and boundaries("up") and gamescreen:
                mover = "up"
            elif event.key == pygame.K_DOWN and boundaries("down") and gamescreen:
                mover = "down"
            elif event.key == pygame.K_LEFT and boundaries("left") and gamescreen:
                mover = "left"
            elif event.key == pygame.K_RIGHT and boundaries("right") and gamescreen:
                mover = "right"
            keydown = False

        if event.type == pygame.KEYUP:
            keydown = True


        if event.type == pygame.MOUSEBUTTONDOWN and homeScreen:

            if rect_level1.collidepoint(event.pos) and homeScreen:
                GameColor = GREEN
                board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                solvedBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
                starting_board()
                draw()
                homeScreen = False
                gamescreen = True

            if rect_level2.collidepoint(event.pos) and homeScreen:
                GameColor = BLUE
                board = [[0, 0, 0,0], [0, 0, 0,0], [0, 0, 0,0],[0, 0, 0,0]]
                solvedBoard = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 0]]
                starting_board()
                draw()
                homeScreen = False
                gamescreen = True

            if rect_level3.collidepoint(event.pos) and homeScreen:
                GameColor = RED
                board = [[0, 0, 0,0,0], [0, 0, 0,0,0], [0, 0, 0,0,0],[0, 0, 0,0,0],[0, 0, 0,0,0]]
                solvedBoard = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],[16, 17, 18, 19, 20],[21, 22, 23, 24, 0]]
                starting_board()
                draw()
                homeScreen = False
                gamescreen = True

        if event.type == pygame.MOUSEBUTTONDOWN and gamescreen:
            if solve_rect.collidepoint(event.pos) and gamescreen:
                solved_board()
                draw()

            if new_rect.collidepoint(event.pos) and gamescreen:
                make_zero()
                starting_board()
                draw()

            if Quit_rect.collidepoint(event.pos) and gamescreen:
                gamescreen = False
                screen.fill(BLACK)
                goHome()
                homeScreen = True

    if mover:
        function(mover)
        draw()
    mover = ""

    pygame.display.update()

    ##check for solved board
    if board == solvedBoard:
        gamescreen = False
        screen.fill(GREEN)
        gameover = font.render("WINNER",False,(0,0,0))
        enter_button = font.render("press enter",False,(0,0,0))
        screen.blit(gameover,(450-int(gameover.get_width()/2),700/2))
        screen.blit(enter_button,(450-int(enter_button.get_width()/2),550))
        gameover = True

pygame.quit()