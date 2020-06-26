import unittest
from Game_Logic import *
class Test(unittest.TestCase):

    def test_2(self):
        # ruch skrajnym pionkiem czerwonym do przodu a nie po skosie
        grid=Game_Logic()
        result=grid.Check_move(grid.board[5][0],4,0)
        self.assertFalse(result)

    def test_3(self):
        #bicie pojedynczego pionka
        grid = Game_Logic()
        grid.move(grid.board[5][4],4,5)
        grid.move(grid.board[2][7],3,6)
        result=grid.beating(grid.board[4][5],2,7)
        self.assertEqual(result,True)
        grid.print_matrix()

    def test_5(self):
        #zamiana w damke
        grid = Game_Logic()
        grid.board[0][1]=' '






if __name__=='__main__':
    unittest.main()

