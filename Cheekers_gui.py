import pygame
from Game_Logic import *
from Pawns import *


class Checkers_gui(object):
    def __init__(self):
        self.screen = self.init_screen()
        self.grid = Game_Logic()
        self.running = True
        self.Player1 = Player("Player 1", self.grid.player_red)
        self.Player2 = Player("Player 2", self.grid.player_yellow)
        self.Player1.Turn = True
        self.clock = pygame.time.Clock()

    def init_screen(self):
        pygame.init()
        pygame.display.set_caption("English Checkers")
        screen = pygame.display.set_mode((600, 540))
        icon = pygame.image.load('checkers.png')
        pygame.display.set_icon(icon)
        return screen

    def turn_drawn(self, msg):
        color = (69, 252, 3)
        font = pygame.font.Font(None, 50)
        text = font.render(f"Tura gracza : {msg}", True, color)
        return text

    def res_Button(self):
        color2 = (233, 252, 211)
        color = (69, 252, 3)
        pygame.draw.rect(self.screen, color, (500, 150, 80, 80))
        font = pygame.font.Font(None, 30)
        text = font.render("RESET", True, color2)
        self.screen.blit(text, (510, 180))

    def DisplayBoard(self, current_player):
        black = (0, 0, 0)
        white = (255, 255, 255)
        wood = (166, 128, 100)
        x, y = 15, 35
        size = 60
        self.screen.fill(wood)
        text = self.turn_drawn(current_player.player)
        self.screen.blit(text, (100, 1))
        self.res_Button()
        for row in range(8):
            for column in range(8):
                if (row % 2 == 0 and column % 2 == 0) or (row % 2 != 0 and column % 2 != 0):
                    pygame.draw.rect(self.screen, white, (x + (row * size), y + (column * size), size, size))
                if row % 2 != 0 and column % 2 == 0 or (row % 2 == 0 and column % 2 != 0):
                    block = pygame.draw.rect(self.screen, black, (x + (row * size), y + (column * size), size, size))
                    self.pawn_display(str(self.grid.board[column][row]), block.center)

    def pawn_display(self, pawn, center):
        red = (255, 0, 0)
        yellow = (255, 223, 24)
        white = (255, 255, 255)

        if pawn == 'C' or pawn == '[C]':
            pygame.draw.circle(self.screen, red, center, 25)
        elif pawn == 'B' or pawn == '[B]':
            pygame.draw.circle(self.screen, yellow, center, 25)
        elif pawn == 'Cd' or pawn == '[Cd]':
            pygame.draw.circle(self.screen, red, center, 25)
            pygame.draw.circle(self.screen, white, center, 27, 1)
        elif pawn == 'Bd' or pawn == '[Bd]':
            pygame.draw.circle(self.screen, yellow, center, 25)
            pygame.draw.circle(self.screen, white, center, 28, 1)

    def mainloop(self):
        while self.running:
            try:
                if self.Player1.Turn:
                    current_player = self.Player1
                else:
                    current_player = self.Player2

                self.screen.fill((0, 0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return 0
                    # Wybieramy pionka nastepnie sprawdzamy czy nalezy do klasy pawn
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            old_x, old_y = pygame.mouse.get_pos()
                            if 500 <= old_x <= 580 and 150 <= old_y <= 230:
                                self.__init__()
                                self.mainloop()
                                return
                            old_x = (old_x - 15) // 60
                            old_y = (old_y - 35) // 60


                            #ruch po wybraniu pionka

                            if isinstance(self.grid.board[old_y][old_x], pawn) and current_player.Check_pawn(self.grid.board, old_y, old_x):
                                second_click = True
                                count_moves = 0

                                while second_click:
                                    event = pygame.event.wait()

                                    if event.type == pygame.QUIT:
                                        second_click = False
                                        running = False
                                    elif event.type == pygame.MOUSEBUTTONUP:
                                        if event.button == 1:
                                            x, y = pygame.mouse.get_pos()
                                            if 500 <= x <= 580 and 150 <= y <= 230:
                                                self.__init__()
                                                self.mainloop()
                                                return
                                            x = (x - 15) // 60
                                            y = (y - 35) // 60

                                            if self.grid.Check_move(self.grid.board[old_y][old_x], y, x) and count_moves == 0:
                                                self.grid.move(self.grid.board[old_y][old_x], y, x)
                                                count_moves += 1
                                                second_click = False

                                            elif self.grid.beating(self.grid.board[old_y][old_x], y, x):

                                                self.grid.move(self.grid.board[old_y][old_x], y, x)
                                                old_y = y
                                                old_x = x
                                                count_moves += 1

                                                if current_player.player == "Player 1":
                                                    self.Player2.number_of_pawns -= 1
                                                elif current_player.player == "Player 2":
                                                    self.Player1.number_of_pawns -= 1

                                                if self.grid.cant_beat(self.grid.board[old_y][old_x]):
                                                    second_click = False

                                            else:
                                                print('ruch niedozwolony')
                                                second_click = False

                                    self.grid.makeQuin(self.Player1, self.Player2)
                                    self.DisplayBoard(current_player)
                                    pygame.display.update()

                                if count_moves > 0:
                                    self.Player1.Turn_end(self.Player1.Turn)
                                    self.Player2.Turn_end(self.Player2.Turn)

                self.DisplayBoard(current_player)
                pygame.display.update()
                self.clock.tick(60)

                if self.Player2.number_of_pawns == 0:
                    print('wygrał Player1')
                    self.running = False
                if self.Player1.number_of_pawns == 0:
                    print('wygrał Player2')
                    self.running = False
            except Exception as e:
                continue


if __name__ == "__main__":
    game = Checkers_gui()
    game.mainloop()
