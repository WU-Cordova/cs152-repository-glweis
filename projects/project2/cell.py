

class Cell:

    def __init__(self, location: tuple[int, int], alive: bool, neighbors: int) -> None:
        self.location = location
        self.neighbors = neighbors
        self.alive = False

    def num_of_neighs(self):
        pass
    
    def alive_next_gen(self):
        pass

    def __eq__(self, other):
        pass
        