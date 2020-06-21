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

    if pawn == 'C' or pawn == '[C]':
        pygame.draw.circle(screen, red, center, 25)
    elif pawn == 'B' or pawn == '[B]':
        pygame.draw.circle(screen, color_p, center, 25)
    elif pawn == 'Cd' or pawn == '[Cd]':
        pygame.draw.circle(screen, red, center, 25)
        pygame.draw.circle(screen, white, center, 27, 1)
    elif pawn == 'Bd' or pawn == '[Bd]':
        pygame.draw.circle(screen, color_p, center, 25)
        pygame.draw.circle(screen, white, center, 28, 1)



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
                pawn_display(screen, str(grid.board[column][row]), block.center)


#todo: ogarnac graczy
#todo: tura gracza + dodaj napis kogo tura
#todo: zamiana w krolowa
#todo: dodanie zmiany nazwy pionka
#todo: oczyszczenie kodu

#todo: dodac wyjatki
#todo nwm co z gui zrobic
#todo: dodac przycisk resetu
#todo: testy
#todo: podpisac w gitchabie
#todo: dodac komentarze

def main():
    screen = init_screen()
    grid = Game_Logic.Game_Logic()
    grid.test()
    running = True
    Player1=Game_Logic.Player("Player 1",grid.player_red)
    Player2 = Game_Logic.Player("Player 2", grid.player_black)
    #jeśli True to tura gracza
    Player1.Turn=True

    while running:
        if Player1.Turn==True:
            current_player = Player1
        else:
            current_player =Player2
        screen.fill((0, 0, 0))
        print(current_player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    old_x, old_y = pygame.mouse.get_pos()
                    old_x = (old_x - 15) // 60
                    old_y = (old_y - 35) // 60
                    ######################################
                    if (isinstance(grid.board[old_y][old_x], pawn)and current_player.itismypawn(grid.board,old_y,old_x)):
                        second_click = True
                        count_moves=0
                        while second_click:
                            event = pygame.event.wait()
                            if event.type == pygame.QUIT:
                                second_click = False
                                running = False
                            elif event.type == pygame.MOUSEBUTTONUP:
                                if event.button == 1:
                                    x, y = pygame.mouse.get_pos()
                                    x = (x - 15) // 60
                                    y = (y - 35) // 60
                                    print('lista ruchow {}'.format(grid.board[old_y][old_x].list_of_moves()))
                                    if grid.ismovepossible(grid.board[old_y][old_x], y, x) and count_moves==0 :
                                        grid.move(grid.board[old_y][old_x], y, x)
                                        print('ruch poprawny {} {}'.format(y,x))
                                        count_moves+=1
                                        second_click = False
                                    elif grid.isjumppossible(grid.board[old_y][old_x], y, x):
                                        grid.move(grid.board[old_y][old_x], y, x)
                                        print('ruch poprawny {} {}'.format(y,x))
                                        old_y=y
                                        old_x=x
                                        count_moves += 1

                                    else:
                                        print('ruch niemozliwy')
                                        second_click = False
                            DisplayBoard(screen, grid)
                            pygame.display.update()

                        if count_moves>0:
                            Player1.endmyturn(Player1.Turn)
                            Player2.endmyturn(Player2.Turn)


        running=Player1.isgameover()
        running=Player2.isgameover()
        DisplayBoard(screen, grid)
        pygame.display.update()


if __name__ == "__main__":
    main()
