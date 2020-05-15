import pygame
import Board
import os
import Pawns as p

def createpyboard(screen, white, black, wood):
    startX=200
    startY=100
    distance=55
    triangle_size=55
    pygame.draw.rect(screen, wood, (startX - 10, startY - 10, 460, 460))

    for x in range(8):
        for y in range(8):
            if x%2==0 and y%2==0:
                pygame.draw.rect(screen, black, (startX + (x * distance), startY + (y * distance), triangle_size, triangle_size))
            if x % 2 != 0 and y % 2 == 0:
                pygame.draw.rect(screen, white, (startX + (x * distance), startY + (y * distance), triangle_size,triangle_size))
            if x % 2 == 0 and y % 2 != 0:
                pygame.draw.rect(screen, white, (startX + (x * distance), startY + (y * distance), triangle_size, triangle_size))
            if x % 2 != 0 and y % 2 != 0:
                pygame.draw.rect(screen, black, (startX + (x * distance), startY + (y * distance), triangle_size, triangle_size))
    pygame.display.update()



def main():
    # colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    wood = (166, 128, 100)
    # init pygame
    Window_x = 300
    Window_y = 100
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (Window_x, Window_y)
    pygame.init()
    pygame.display.set_caption("English Checkers")
    screen = pygame.display.set_mode((960, 640))
    icon = pygame.image.load('game.png')
    pygame.display.set_icon(icon)
    # init board
    Playground = Board.Board()
    Playground.initboard()
    # Playground.init_number()

    # initalize players
    player_1 = []
    for i in range(3):
        for j in range(8):
            if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
                createpawn = p.pawn(i, j, "P1")
                player_1.append(createpawn)
     #====================================================================
    player_2 = []
    for i in range(5, 8):
        for j in range(8):
            if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
                createpawn = p.pawn(i, j, "P2")
                player_2.append(createpawn)
    #=======================================================================
    Playground.put_pawns(player_1)
    Playground.put_pawns(player_2)
    menu_rect = pygame.Rect(0, 0, 100, 320)
    running = True
    createpyboard(screen,white,black,wood)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()

