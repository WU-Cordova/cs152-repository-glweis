from __future__ import annotations
class Cell:

    def __init__(self, location: tuple[int, int], alive: bool = False) -> None:
        self.location = location
        self.alive = alive #?

    def num_of_neighbors(self, grid: 'Grid'):
        from projects.project2.grid import Grid

        directions = [(-1, -1), (0, -1), (1, -1),
                      (-1, 0), (1, 0), (-1, 1),
                      (0, 1), (1, 1)]
        
        # Check directions
        count = 0
        for dx, dy in directions:
            nx, ny = self.location[0] + dx, self.location[1] + dy
            if 0 <= nx < grid.rows and 0 <= ny < grid.columns:
                if grid.current_grid[nx][ny].alive: #???
                    count += 1
        return count
    
    def alive_next_gen(self, grid: Grid):
        neighbors = self.num_of_neighbors(grid)
        if self.alive:
            if neighbors < 2 or neighbors > 3:
                return False
            else:
                return True
        elif neighbors == 3:
            return True  # Cell is born
        return False

    def __eq__(self, other: object):
        if not isinstance(other, Cell):
            return False
        #?
        return self.location == other.location and self.alive == other.alive
        