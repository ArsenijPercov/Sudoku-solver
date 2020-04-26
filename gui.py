import tkinter as tk
import sudoku_solver

class SudokuGui(tk.Frame):
    def __init__(self,*args,**kwargs):
        tk.Frame.__init__(self,*args,**kwargs)
        
        self.board = [[0 for x in range(9)] for y in range(9)] 
        self.solvedboard = [[0 for x in range(9)] for y in range(9)]
        self.current = (0,0)
        self.cellsize = 50 
        
        self.canvas = tk.Canvas(self,height = 9*self.cellsize+self.cellsize, width = 9*self.cellsize)
        self.boxes = [[None for x in range(9)] for y in range(9)]
        self.texts = [[None for x in range(9)] for y in range(9)]
        self.canvas.pack(expand=0)

        for i in range(3):
            for j in range(3):
                self.canvas.create_rectangle(3*i*self.cellsize,3*j*self.cellsize,3*(i+1)*self.cellsize,3*(j+1)*self.cellsize,width=3,outline="purple")
        for i in range(9):
            for j in range(9):
                self.boxes[i][j] = self.canvas.create_rectangle(i*self.cellsize,j*self.cellsize,(i+1)*self.cellsize,(j+1)*self.cellsize,width=1,outline="purple")
                self.texts[i][j] = self.canvas.create_text(i*self.cellsize+self.cellsize/2,j*self.cellsize+self.cellsize/2)
        
    def updatecell(self, coord,val):
        self.canvas.itemconfig(self.texts[coord[0]][coord[1]],font=("Purisa", 20), text=str(val))
        self.board[coord[0]][coord[1]]=val
    
    def getorigin(self,eventorigin):
        x = eventorigin.x
        y = eventorigin.y
        xcell = x//self.cellsize
        ycell = y//self.cellsize
        self.current = (xcell,ycell)
        print(xcell,ycell)

    def handleinp(self,event):
        d = int(event.char)
        self.updatecell(self.current,d)

    def loadboard(self,board):
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != 0:
                    self.canvas.itemconfig(self.texts[i][j],font=("Purisa", 20), text=str(board[i][j]))
    
    #def solve(self):
    #    self.solvedboard = sudoku_solver.solve(board)
     #   print(self.solvedboard)
      #  self.loadboard(self.solvedboard)

    # def checkandfinish(self):
    #     if board == solvedboard:
    #         var = self.StringVar()
    #         label = self.Message( self, textvariable=var)
    #         var.set("Won")
    #         label.pack()

if __name__ == "__main__":
    mainwindow = tk.Tk()
    board = [[0,4,0,0,0,0,0,0,7],
               [0,0,6,0,0,0,8,0,0],
               [0,0,0,3,0,4,1,0,0],
               [8,0,0,7,1,0,0,0,0],
               [7,0,0,9,0,0,0,0,0],
               [5,6,2,0,0,0,0,0,0],
               [0,0,0,0,0,7,0,5,2],
               [0,0,0,0,2,0,0,0,0],
               [0,8,0,0,5,0,0,6,0]]
    sudoku = SudokuGui(mainwindow)
    sudoku.loadboard(board)
    #sudoku.solve()
    mainwindow.bind("<Button 1>",sudoku.getorigin)
    #mainwindow.bind("s",sudoku.solve)

    for i in range(9):
        mainwindow.bind(str(i+1),sudoku.handleinp)
    sudoku.pack(expand=False)
    mainwindow.mainloop()