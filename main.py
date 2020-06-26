import unittest
from Game_Logic import *
class Test(unittest.TestCase):

    def test_wrong_move(self):
        # ruch skrajnym pionkiem czerwonym do przodu a nie po skosie
        grid=Game_Logic()
        result=grid.Check_move(grid.board[5][0],4,0)
        self.assertFalse(result)

    def test_beating(self):
        grid = Game_Logic()
        grid.move(grid.board[5][4],4,5)
        grid.move(grid.board[2][7],3,6)
        result=grid.beating(grid.board[4][5],2,7)
        grid.print_matrix()







if __name__=='__main__':
    unittest.main()

