import pygame
import Game_Logic
import os
from Pawns import *

def init_screen():
    Window_x = 300
    Window_y = 100
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (Window_x, Window_y)
    pygame.init()
    pygame.display.set_caption("English Checkers")
    screen = pygame.display.set_mode((600, 540))
    icon = pygame.image.load('checkers.png')
    pygame.display.set_icon(icon)
    return screen


def pawn_display(screen, pawn, center):
    red = (255, 0, 0)
    color_p = (255, 223, 24)
    white = (255, 255, 255)

    if pawn == 'C'or pawn =='[C]':
        pygame.draw.circle(screen, red, center, 25)
    elif pawn == 'B'or pawn == '[B]':
        pygame.draw.circle(screen, color_p, center, 25)
    elif pawn == 'Cd'or pawn =='[Cd]':
        pygame.draw.circle(screen, red, center, 25)
        pygame.draw.circle(screen, white, center, 27, 1)
    elif pawn == 'Bd' or pawn == '[Bd]':
        pygame.draw.circle(screen, color_p, center, 25)
        pygame.draw.circle(screen, white, center, 28, 1)


# todo tu zszytuje za kazdym razem stan boardu
def DisplayBoard(screen, grid):
    black = (0, 0, 0)
    white = (255, 255, 255)
    wood = (166, 128, 100)
    x, y = 15, 35
    size = 60
    screen.fill(wood)
    for row in range(8):
        for column in range(8):
            if (row % 2 == 0 and column % 2 == 0) or (row % 2 != 0 and column % 2 != 0):
                pygame.draw.rect(screen, white, (x + (row * size), y + (column * size), size, size))
            if row % 2 != 0 and column % 2 == 0 or (row % 2 == 0 and column % 2 != 0):
                block = pygame.draw.rect(screen, black, (x + (row * size), y + (column * size), size, size))
                pawn_display(screen,str(grid.board[column][row]), block.center)

def pick_pawn():
    pass

def main():
    screen = init_screen()
    grid = Game_Logic.Game_Logic()
    grid.test()
    running = True

    while running:

        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type==pygame.MOUSEBUTTONUP:
                if event.button==1:
                    x, y = pygame.mouse.get_pos()
                    x=(x-15)//60
                    y=(y-35)//60
                    if(isinstance(grid.board[y][x],pawn)):
                        print(grid.board[y][x])





        DisplayBoard(screen, grid)
        pygame.display.update()


if __name__ == "__main__":
    main()
