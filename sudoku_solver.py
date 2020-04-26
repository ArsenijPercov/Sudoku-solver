import numpy as np
import copy


class SudokuSolver:
    def __init__(self,board):
        self.board = board
        self.solved = [[]]
        self.solve()
        print(self.board)

    def possible(self,x,y,n):
        #if (self.board != sudoku_grid):
        #print(np.matrix(grid))
        for i in range(9):
            if self.board[x][i] == n:
                return False
        for j in range(9):
            if self.board[j][y] == n:
                return False
        x_zone = (x//3)*3
        y_zone = (y//3)*3
        for i in range(3):
            for j in range(3):
                if self.board[x_zone+i][y_zone+j] == n:
                    return False
        return True

    def solve(self):
        #global sudoku_grid
        #print(np.matrix(sudoku_grid))
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    for r in range(1,10):
                        if self.possible(i,j,r):
                            self.board[i][j] = r
                            #print(np.matrix(self.board))
                            self.solve()
                            #print("=========")
                            self.board[i][j] = 0
                    return
        self.solved = copy.deepcopy(self.board.copy())
        print(np.matrix(self.solved))
        return
