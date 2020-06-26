import Pawns


class Game_Logic(object):
    def __init__(self):
        self.column = 8
        self.row = 8
        self.board = [[' ' for _ in range(self.column)] for _ in range(self.row)]
        self.player_red = []
        self.player_yellow = []
        self.init_player_red()
        self.init_player_yellow()

    def print_matrix(self):
        for x in self.board:
            print(x)

    def init_player_yellow(self):
        for row in range(3):
            for column in range(8):
                if row % 2 != 0 and column % 2 == 0 or row % 2 == 0 and column % 2 != 0:
                    add_pawn = Pawns.pawn(row, column, "B")
                    self.player_yellow.append(add_pawn)

        for pawn in self.player_yellow:
            self.board[pawn.x][pawn.y] = pawn

    def init_player_red(self):
        for row in range(5, 8):
            for column in range(8):
                if row % 2 != 0 and column % 2 == 0 or row % 2 == 0 and column % 2 != 0:
                    add_pawn = Pawns.pawn(row, column, "C")
                    self.player_red.append(add_pawn)

        for pawn in self.player_red:
            self.board[pawn.x][pawn.y] = pawn

    def Check_move(self, pawn, x, y):
        for move in pawn.list_of_moves():
            if move[0] == x and move[1] == y and self.board[x][y] == ' ':
                return True
        return False

    def beating(self, pawn, x, y):
        # wykonanie bicia
        for jump in pawn.list_of_jumps():
            if jump[0] == x and jump[1] == y and self.board[x][y] == ' ' and self.board[jump[2]][jump[3]] != ' ' and \
                    self.board[jump[2]][jump[3]].type_piece != pawn.type_piece:
                self.board[jump[2]][jump[3]] = ' '
                return True
        return False

    def cant_beat(self, pawn):
        #sprawdzenie czy mozna dalej bez podawania współrzednych myszki
        for posible_jump in pawn.list_of_jumps():
            if self.board[posible_jump[0]][posible_jump[1]] == ' ' and \
                    self.board[posible_jump[2]][posible_jump[3]] != ' ' and self.board[posible_jump[2]][posible_jump[3]].type_piece != pawn.type_piece:
                return False
        return True

    def move(self, pawn, x, y):
        self.board[pawn.x][pawn.y] = ' '
        pawn.x = x
        pawn.y = y
        self.board[pawn.x][pawn.y] = pawn

    def makeQuin(self, player1, player2):
        for y in range(8):
            if (isinstance(self.board[7][y], Pawns.pawn) and self.board[7][y].type_piece == 'B'):
                player2.list_Pawns.remove(self.board[7][y])
                self.board[7][y] = ' '
                createQuin = Pawns.Quin(7, y, 'Bd')
                self.board[7][y] = createQuin
                player2.list_Pawns.append(self.board[7][y])

            if (isinstance(self.board[0][y], Pawns.pawn) and self.board[0][y].type_piece == 'C'):
                player1.list_Pawns.remove(self.board[0][y])
                self.board[0][y] = ' '
                createQuin = Pawns.Quin(0, y, 'Cd')
                self.board[0][y] = createQuin
                player1.list_Pawns.append(self.board[0][y])



#w klasie Player zawiera metody i zmienne służą do
#określenia tury i sprawdzania czy pionek nalezy do gracza
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

    def __str__(self):
        return ' {}'.format(self.player)

