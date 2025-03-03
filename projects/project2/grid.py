from projects.project2.array2d import Array2D
# from projects.project2.gamecontroller import GameController
from projects.project2.cell import Cell
import random

#/u25a0 = white
#/u25a1 = black

class Grid:

    def __init__(self, rows: int, columns: int) -> None:
        #self.rows = rows
        #self.columns = columns
        cells: list[list[Cell]] = []

        # initializing the grid
        for row in range(rows):
            cells.append([])
            for col in range(columns):
                alive = random.choice((True, False))
                cells[row].append(Cell(alive=alive))
        
        self.current_grid: Array2D = Array2D(starting_sequence=[[]], data_type=Cell)
        
        #self.current_grid[row][col] = Cell(location=(row, col), alive=alive, neighbors=0)

    def get_cell(self, row, col):
        # extra method?
        return self.current_grid[row][col]

    def num_alive():
        pass

    def produce_next_gen():
        pass
        