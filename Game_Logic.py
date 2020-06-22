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
                    add_pawn = Pawns.pawn(row, column, "B")
                    self.player_black.append(add_pawn)

        for pawn in self.player_black:
            self.board[pawn.x][pawn.y] = pawn

    def init_player_red(self):
        for row in range(5, 8):
            for column in range(8):
                if row % 2 != 0 and column % 2 == 0 or row % 2 == 0 and column % 2 != 0:
                    add_pawn = Pawns.pawn(row, column, "C")
                    self.player_red.append(add_pawn)

        for pawn in self.player_red:
            self.board[pawn.x][pawn.y] = pawn

    def unpick(self, x, y):
        prev = str(self.board[x][y])
        self.board[x][y] = f'[{prev}]'

    def pick(self, x, y):
        prev = str(self.board[x][y])
        self.board[x][y] = f'[{prev}]'

    def Check_move(self, pawn, x, y):
        for move in pawn.list_of_moves():
            print(x, y)
            if move[0] == x and move[1] == y and self.board[x][y] == ' ':
                return True
        return False

    def beating(self, pawn, x, y):
        for jump in pawn.list_of_jumps():

            if jump[0] == x and jump[1] == y and self.board[x][y] == ' ' and self.board[jump[2]][jump[3]] != ' ' and \
                    self.board[jump[2]][jump[3]].type_piece != pawn.type_piece:
                self.board[jump[2]][jump[3]] = ' '
                return True
        return False

    def move(self, pawn, x, y):
        self.board[pawn.x][pawn.y] = ' '
        pawn.x = x
        pawn.y = y
        self.board[pawn.x][pawn.y] = pawn

    def makeQuin(self):
        for y in range(8):
            if(isinstance(self.board[7][y],Pawns.pawn)and self.board[7][y].type_piece=='B'):
                self.board[7][y]=' '
                createQuin = Pawns.Quin(7, y, 'Bd')
                self.board[7][y] = createQuin

            if (isinstance(self.board[0][y], Pawns.pawn) and self.board[0][y].type_piece == 'C'):
                self.board[0][y] = ' '
                createQuin = Pawns.Quin(0, y, 'Cd')
                self.board[0][y] =createQuin



class Player(object):
    def __init__(self, player, list_Pawns):
        self.player = player
        self.list_Pawns = list_Pawns
        self.number_of_pawns = len(list_Pawns)
        self.Turn = False

    def Turn_end(self, end_turn):
        if end_turn == True:
            self.Turn = False
        else:
            self.Turn = True

    def Check_pawn(self, board, x, y):
        for pawn in self.list_Pawns:
            if str(board[x][y]) == pawn.type_piece:
                return True
        print('pionek przeciwnika')
        return False

    def Game_Over(self):
        if self.number_of_pawns == 0:
            return False
        else:
            return True
    def check_numb_pawn(self, list_Pawns):
        self.number_of_pawns = len(list_Pawns)
    def __str__(self):
        return ' {}'.format(self.player)
