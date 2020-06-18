import Pawns

#todo bicie

class Game_Logic(object):
    def __init__(self):
        self.column = 8
        self.row = 8
        self.board = [[' ' for _ in range(self.column)] for _ in range(self.row)]
        self.player_red = []
        self.player_black = []
        self.init_player_red()
        self.init_player_black()

    def test(self):
        for x in self.board:
            print(x)

    def init_player_black(self):
        for row in range(3):
            for column in range(8):
                if row % 2 != 0 and column % 2 == 0 or row % 2 == 0 and column % 2 != 0:
                    add_pawn = Pawns.pawn(row, column,"B")
                    self.player_black.append(add_pawn)
        count=0
        for pawn in self.player_black:
            self.board[pawn.x][pawn.y] =pawn.type_piece


    def init_player_red(self):
        for row in range(5, 8):
            for column in range(8):
                if row % 2 != 0 and column % 2 == 0 or row % 2 == 0 and column % 2 != 0:
                    add_pawn = Pawns.pawn(row, column, "C")
                    self.player_red.append(add_pawn)

        for pawn in self.player_red:
            self.board[pawn.x][pawn.y] = pawn.type_piece
       #todo ta funkcja w chwili obecnej nie ma sensu
    def createQuin(self,pawn):
        if pawn.type_piece=='B':
            if pawn.y==7:
                pawn.type_piece='Bd'
        if pawn.type_piece=='C':
            if pawn.y==0:
                pawn.type_piece='Cd'

    # todo: duze zmiany inncoming
    def ismovepossible(self, x, y, pawn):
        #jezeli ruch po skosie i na obszarze planszy
        if self.board[x][y] == ' ' and x <= (self.column - 1) and y <= (self.row - 1) and (y - pawn.y == 1 or y - pawn.y == -1) :
                if pawn.type_piece == 'B' and x - pawn.x == 1:
                    return True
                elif pawn.type_piece == 'Bd' and (x - pawn.x == 1 or x - pawn.x == -1):
                    return True
                elif pawn.type_piece == 'C' and  x - pawn.x == -1:
                    return True
                elif pawn.type_piece == 'Cd' and  (x - pawn.x == 1 or x - pawn.x == -1):
                    return True
                else:
                    return False
        else:
            return False
    def valid_jump(self,pawn):
        if pawn.type_piece=='C' and (self.board[pawn.x-1][pawn.y-1]=='B' or self.board[pawn.x-1][pawn.y-1]=='dB' or self.board[pawn.x-1][pawn.y+1]=='B'
         or self.board[pawn.x-1][pawn.y+1]=='dB'):
            if self.board[pawn.x-2][pawn-2]==' ' or self.board[pawn.x-2][pawn+2]==' ':
                return True
            else:
                return False
         #do pawns dodac możliwy ruch






    def valid_move(self, x, y, pawn):
        #przesuniecie o 1
        if self.ismovepossible(x, y, pawn):
            self.board[pawn.x][pawn.y] = ' '
            pawn.x = x
            pawn.y = y
            self.board[pawn.x][pawn.y] = pawn.type_piece
            print('wykonano ruch')
        else:
            print('ruch nie mozliwy')
            return
        self.createQuin(pawn)

# B=czarny
# C=czerwony

#logika becie całkowicie zmieniona :(