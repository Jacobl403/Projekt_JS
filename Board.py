import pygame



class Board(object):
    def initboard(self):
        initboard = [[' ' for _ in range(8)] for _ in range(8)]
        self.board = initboard

    def put_pawns(self, pawnlist:list):
        for cls in pawnlist:
            Xpos = cls.x
            Ypos = cls.y
            self.board[Xpos][Ypos] = cls.player_piece

    def printlist(self):
        for x in self.board:
            print(x)

    def init_number(self):
        for x in range(8):
            for y in range(8):
                self.board[x][y] = '{} {}'.format(x, y)


"""
text function 

update position of player piece
"""
