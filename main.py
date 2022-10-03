# Rules: 
#   Any live cell with two or three live neighbours survives.
#   Any dead cell with three live neighbours becomes a live cell.
#   All other live cells die in the next generation. Similarly, all other dead cells stay dead.

import os
import time

def main():
    cols, rows = os.get_terminal_size()
    game = Game(rows, cols, "#")
    glider =[[0,2], [1,2], [2,2], [2,1], [1,0]]
    game.set_start(glider)
    game.run(100)

class Game:
    def __init__(self, rows, cols, fill) -> None:
        self.rows = rows - 1
        self.cols = cols
        self.fill = fill
        self.grid = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
    
    def __str__(self):
        grid_str = ""
        for row in self.grid:
            for item in row:
                grid_str += item
        return grid_str

    def set_start(self, start_list):
        for (x,y) in start_list:
            self.grid[y][x] = self.fill

    def run(self, num_steps):
        for i in range(num_steps):
            print(self)
            time.sleep(.05)
            self.update()

    def num_neighbors(self, i, j):
        count = 0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if x == 0 and y == 0:
                    continue
                if x + i < 0 or y + j < 0:
                    continue
                if x + i >= self.cols or y + j >= self.rows:
                    continue
                elif self.grid[j + y][i + x] == self.fill:
                    count += 1
        return count

    def update(self):
        new_grid = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
        for j in range(self.rows):
            for i in range(self.cols):
                count = self.num_neighbors(i, j)
                if self.grid[j][i] == self.fill:
                    if count == 2 or count == 3:
                        new_grid[j][i] = self.grid[j][i]
                elif count == 3:
                    new_grid[j][i] = self.fill
        self.grid = new_grid

if __name__ == "__main__":
    main()