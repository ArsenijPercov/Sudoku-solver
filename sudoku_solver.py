import numpy as np

sudoku_grid = [[0,4,0,0,0,0,0,0,7],
               [0,0,6,0,0,0,8,0,0],
               [0,0,0,3,0,4,1,0,0],
               [8,0,0,7,1,0,0,0,0],
               [7,0,0,9,0,0,0,0,0],
               [5,6,2,0,0,0,0,0,0],
               [0,0,0,0,0,7,0,5,2],
               [0,0,0,0,2,0,0,0,0],
               [0,8,0,0,5,0,0,6,0]]

def possible(x,y,n,grid):
    #if (grid != sudoku_grid):
    #print(np.matrix(grid))
    for i in range(9):
        if grid[x][i] == n:
            return False
    for j in range(9):
        if grid[j][y] == n:
            return False
    x_zone = (x//3)*3
    y_zone = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[x_zone+i][y_zone+j] == n:
                return False
    return True

def solve(grid):
    #global sudoku_grid
    #print(np.matrix(sudoku_grid))
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for r in range(1,10):
                    if possible(i,j,r,grid):
                        grid[i][j] = r
                        #print(np.matrix(grid))
                        solve(grid)
                        #print("=========")
                        grid[i][j] = 0
                return
    print(np.matrix(grid))
    return

solve(sudoku_grid)