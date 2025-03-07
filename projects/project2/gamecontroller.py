from projects.project2.kbhit import KBHit
from projects.project2.grid import Grid
import time

class GameController:

    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self.kbhit = KBHit()

        self.is_running = True
        self.is_manual = False
        self.previous_gen = None

        self.time_superspeed = False
        self.time_fast = False
        self.time_med = True
        self.time_slow = False

    def advance_gens(self) -> None:
        if self.grid.produce_next_gen() == False:
                self.is_running = False
        
    def handle_input(self) -> None:
        if self.kbhit.kbhit():
            key = self.kbhit.getch()
            if key == 'q':
                self.is_running = False
                print("Quitting the game.")
            elif key == 'a':
                self.is_manual = False
                print("Switched to Automatic Mode.")
            elif key == 'm':
                self.is_manual = True
                print("Switched to Manual Mode.")

            elif self.time_med and key == "t":
                print("Simulation speed quickened.")
                self.time_med = False
                self.time_fast = True
            elif self.time_fast and key == "t":
                print("Simulation speed quickened.")
                self.time_fast = False
                self.time_superspeed = True
            elif self.time_superspeed and key == "t":
                print("Simulation speed slowed.")
                self.time_superspeed = False
                self.time_slow = True
            elif self.time_slow and key == "t":
                print("Simulation speed quickened.")
                self.time_slow = False
                self.time_med = True
            

    def run(self) -> None:
        while self.is_running:
            if not self.is_manual:
                self.grid.display()
                self.advance_gens()

                if self.time_slow:
                    time.sleep(3)
                if self.time_med:
                    time.sleep(1)
                if self.time_fast:
                    time.sleep(0.5)
                if self.time_superspeed:
                    time.sleep(0.1)

                self.handle_input()
            else:
                user_input = input("Press 's' to step to next generation, 'a' to return to Automatic Mode, or 'q' to quit: ").lower()

                if user_input == 's':
                    print("Stepping to next generation.")
                    self.grid.produce_next_gen()
                    self.grid.display()
                elif user_input == "a":
                    print("Switched to Automatic Mode.")
                    self.is_manual = False
                    self.grid.produce_next_gen()
                elif user_input == 'q':
                    self.is_running = False
                    print("Quitting the game.")