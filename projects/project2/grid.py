from projects.project2.gamearray2d import Array2D
from projects.project2.cell import Cell
import random

class Grid:

    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        cells: list[list[Cell]] = []
        self.history = []
        self.generation_count = 0

        # initializing the grid
        for row in range(rows):
            cells.append([])
            for col in range(columns):
                alive = random.choice((True, False))
                cells[row].append(Cell((row, col), alive=alive))
        
        self.current_grid: Array2D = Array2D(starting_sequence=cells, data_type=Cell)

    def get_cell(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.columns:
            raise IndexError("Index out of range.")
        return self.current_grid[row][col]

    def num_alive(self):
        count = 0
        for row in range(self.rows):
            for col in range(self.columns):
                if self.get_cell(row, col).alive:
                    count += 1
        print(f"Cells alive = {count}")
        return count

    def produce_next_gen(self):
        next_gen = []

        for row in range(self.rows):
            new_row = []
            for col in range(self.columns):
                cell = self.get_cell(row, col)
                next_state = cell.alive_next_gen(self) # calls Cell.alive_next_gen
                new_row.append(Cell(location=(row, col), alive=next_state)) 
            next_gen.append(new_row)

        # All checks that could cease the game
        if self.checks(next_gen) == False:
            self.current_grid = Array2D(starting_sequence=next_gen, data_type=Cell)
            self.generation_count += 1
            self.display()
            return False
    
        self.current_grid = Array2D(starting_sequence=next_gen, data_type=Cell)
        self.add_to_history(next_gen)
        self.generation_count += 1

        return True

    def stable(self, next_gen):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.current_grid[row][col].alive != next_gen[row][col].alive:
                    return False
        return True

    def repeating(self, next_gen):
        for gen in self.history:
            if gen == next_gen:
                return True
        return False
    
    def colony_dead(self, next_gen):
        if all(cell.alive == False for row in next_gen for cell in row):
            return True
        return False
    
    def add_to_history(self, current_grid):
        self.history.append(current_grid)

    def checks(self, next_gen):
        # Stable
        if self.stable(next_gen):
            print("Colony stablilized.")
            print("Next generation:")
            print()
            return False
        #print("Colony unstable.")

        # Repeating
        if self.repeating(next_gen):
            print("Repeating pattern detected.")
            print("Next generation:")
            print()
            return False
        #print("Colony not repeating.")

        # Colony dead
        if self.colony_dead(next_gen):
            print("Colony dead.")
            print()
            return False
        
        return True
    
    def display(self) -> None:
        print(f"Generation: {self.generation_count}")
        for row in range(self.rows):
            row_str = " ".join(f"{'■' if self.get_cell(row, col).alive else '□'}" for col in range(self.columns))
            print(row_str)
        print()