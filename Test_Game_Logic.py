import unittest
import Game_Logic
import Pawns

class Test(unittest.TestCase):
    def setUp(self):
        self.grid=Game_Logic.Game_Logic()

    def test_1(self):
        #wykonanie po 2 ruchy przez graczy
        #sprawdzamy(result) czy mozliwy ruch nastepnie go wykonujemy

        #Player1(5, 4)----> (4, 5)
        result= self.grid.Check_move(self.grid.board[5][4],4,5)
        self.grid.move(self.grid.board[5][4],4,5)
        self.assertEqual(result,True)

        #Player2(2, 5)----> (3, 4)
        result= self.grid.Check_move(self.grid.board[2][5],3,4)
        self.grid.move(self.grid.board[2][5],3,4)
        self.assertEqual(result, True)

        #Player1(5, 2)----> (4, 3)
        result= self.grid.Check_move(self.grid.board[5][2],4,3)
        self.grid.move(self.grid.board[5][2],4,3)
        self.assertEqual(result, True)

        #Player2(1, 4)----> (2, 5)
        result= self.grid.Check_move(self.grid.board[1][4],2,5)
        self.grid.move(self.grid.board[1][4],2,5)
        self.assertEqual(result, True)

    def test_2(self):
        # ruch skrajnym pionkiem czerwonym do przodu a nie po skosie
        result=self.grid.Check_move(self.grid.board[5][0],4,0)
        self.assertFalse(result)

    def test_3(self):
        #bicie pojedynczego pionka
        self.grid.move(self.grid.board[5][4],4,5)
        self.grid.move(self.grid.board[2][7],3,6)
        result=self.grid.beating(self.grid.board[4][5],2,7)
        self.assertEqual(result,True)

    def test_4(self):
        #wykonanie podwójnego bicia
        #musimy odpowiednio ustawic plansze do tego zagrania
        self.grid.move(self.grid.board[5][6], 4, 5)
        self.grid.move(self.grid.board[2][5], 3, 4)
        self.grid.board[7][4]=' '
        result=self.grid.beating(self.grid.board[3][4],5,6)
        self.grid.move(self.grid.board[3][4],5,6)
        self.assertEqual(result,True)
        #sprawdzenie kolejnego bicia jeśli false to można bic
        result=self.grid.cant_beat(self.grid.board[5][6])
        self.assertFalse(result)
    def test_5(self):
        #zamiana w damke
        #musimy zmienic wspołrzedne pionka znajdujacego sie w liscie gracza a nastepnie wstawic go
        #w odpowiednie miejsce na planszy nastepnie funkcja makeQuin usunie pionka i stworzy damke
        #po czym sprawdzamy czy dane pole należy do klasy Quin
        Player1 =Game_Logic.Player("Player 1", self.grid.player_red)
        Player2 =Game_Logic.Player("Player 2", self.grid.player_yellow)
        Player1.list_Pawns[0].x=0
        Player1.list_Pawns[0].y=1
        Player2.list_Pawns[1].x=7
        Player2.list_Pawns[1].y=0
        self.grid.board[0][1]=Player1.list_Pawns[0]
        self.grid.board[7][0]=Player2.list_Pawns[1]
        self.grid.makeQuin(Player1,Player2)
        result=isinstance(self.grid.board[0][1],Pawns.Quin)
        self.assertEqual(result, True)
        result=isinstance(self.grid.board[7][0],Pawns.Quin)
        self.assertEqual(result, True)


    def test_6(self):
        #bicie damą
        Player1 =Game_Logic.Player("Player 1", self.grid.player_red)
        Player2 =Game_Logic.Player("Player 2", self.grid.player_yellow)
        Player1.list_Pawns[0].x=0
        Player1.list_Pawns[0].y=1
        Player2.list_Pawns[1].x=7
        Player2.list_Pawns[1].y=0
        self.grid.board[0][1]=Player1.list_Pawns[0]
        self.grid.board[7][0]=Player2.list_Pawns[1]
        self.grid.makeQuin(Player1,Player2)
        #po stworzeniu damek nalezy umozliwic im bicie:
        #żółty
        self.grid.board[5][2]=' '
        result=self.grid.beating(self.grid.board[7][0],5,2)
        self.grid.move(self.grid.board[7][0],5,2)
        self.assertEqual(result, True)
        #czerwony
        self.grid.board[2][3] =' '
        result=self.grid.beating(self.grid.board[0][1],2,3)
        self.grid.move(self.grid.board[0][1], 2, 3)
        self.assertEqual(result, True)

    def test_7(self):
        #wygrana gracza yellow
        Player1 =Game_Logic.Player("Player 1", self.grid.player_red)
        Player2 =Game_Logic.Player("Player 2", self.grid.player_yellow)
        Player1.number_of_pawns=0
        red_win = False
        yellow_win = False
        if Player2.number_of_pawns == 0:
            red_win = True
        if Player1.number_of_pawns == 0:
            yellow_win = True
        self.assertEqual(yellow_win,True)
        self.assertFalse(red_win)





if __name__=='__main__':
    unittest.main()

