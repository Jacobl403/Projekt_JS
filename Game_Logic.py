import Pawns

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

        for pawn in self.player_black:
            self.board[pawn.x][pawn.y] =pawn

    def init_player_red(self):
        for row in range(5, 8):
            for column in range(8):
                if row % 2 != 0 and column % 2 == 0 or row % 2 == 0 and column % 2 != 0:
                    add_pawn = Pawns.pawn(row, column, "C")
                    self.player_red.append(add_pawn)

        for pawn in self.player_red:
            self.board[pawn.x][pawn.y] = pawn

    def pick(self,x,y):
        return self.board[x][y]

    def change(self,x,y):
             prev=str(self.board[x][y])
             self.board[x][y]=f'[{prev}]'

    def ismovepossible(self,pawn,x,y):
        for move in pawn.list_of_moves():
            print(x,y)
            if move[0]==x and move[1]==y and self.board[x][y]==' ':
                return True
        return False

    def isjumppossible(self,pawn,x,y):
        for jump in pawn.list_of_jumps():

            if jump[0]==x and jump[1]==y and self.board[x][y]==' ' and self.board[jump[2]][jump[3]]!=' 'and \
                    self.board[jump[2]][jump[3]].type_piece!=pawn.type_piece:
                self.board[jump[2]][jump[3]]=' '
                return True
        return False

    def jump(self,pawn,x,y):
        self.move(pawn,x,y)

    def move(self,pawn,x,y):
        self.board[pawn.x][pawn.y] = ' '
        pawn.x = x
        pawn.y = y
        self.board[pawn.x][pawn.y] = pawn



class Player(object):
    def __init__(self,player,list_Pawns):
        self.player=player
        self.list_Pawns=list_Pawns
        self.number_of_pawns=len(list_Pawns)
        self.Turn=False
    def endmyturn(self,end_turn):
        if end_turn==True:
            self.Turn=False
        else:
            self.Turn=True

    def itismypawn(self,board,x,y):
        for pawn in self.list_Pawns:
            if str(board[x][y])==pawn.type_piece:
                return True
        print('pionek przeciwnika')
        return False
    def isgameover(self):
        if self.number_of_pawns==0:
            return False
        else:
            return True

    def __str__(self):
        return ' {}'.format(self.player)



