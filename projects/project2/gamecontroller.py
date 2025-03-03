from projects.project2.array import Array
from projects.project2.kbhit import KBHit
from projects.project2.grid import Grid
from projects.project2.cell import Cell

class GameController:

    def __init__(self, grid: Grid) -> None:
        #debug print
        print("constructed")

        self.generations = Array()
        self.grid = grid #Grid()?

    def advance_gens(gens: int):
        pass

    def run(self) -> None:
        # main loop for the simulaton
        #self.grid.display()
        print(self.grid)