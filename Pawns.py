class pawn(object):
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
        if player == "P1":
            self.player_piece = "C"
            self.pawn_color=(162, 162, 162)
        if player=="P2":
            self.player_piece = "B"
            self.pawn_color=(255, 68, 68)

    def move(self):
        pass

    def __repr__(self):
        return 'x {} y {}'.format(self.x, self.y)


class Quin(pawn):
    pass


"""
position of pawn on board
move pawn
destroy enemy pawn
gracz 1 - przycisk z tekstem “C”. Pola z pionkami gracza
gracz 2 - przycisk z tekstem “B”. Damki oznaczane są dodatkową literą d (“Cd”, “Bd”).
○ Nad planszą wyświetlana jest informacja “Tura gracza 1” lub “Tura gracza 2”.
○ Gracz wybiera pionka (tekst pola zmienia się z “C” na “[C]” lub z “B” na “[B]”)
"""
