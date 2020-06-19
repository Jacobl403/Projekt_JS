import Game_Logic
import Pawns

grid=Game_Logic.Game_Logic()
print(grid.pick(1,2))
grid.change(1,2)
print(grid.pick(1,2))