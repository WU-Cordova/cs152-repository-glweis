from projects.project2.gamecontroller import GameController
from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit

def main():

    kbhit = KBHit()
    grid = Grid(10, 10)
    game = GameController(grid)
    game.run()


if __name__ == '__main__':
    main()
