import random
import flask_restful

from sqlalchemy import true 

class TicTacToe:

    def __init__(self):
        self.board = []
        

    def createBoard(self):
        self.board = [['-' for element in range(3)] for element in range(3)]
    
    def getFirstPlayer():
        return random.randint(0, 1)
    
    def placeMark(self ,x , y , mark):
        self.board[x][y] = mark 
    

    #checking for a winner 
    def chekWinner(self,mark):
        win = True
        #checking rows
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != mark:
                    win = False
                    
                
            if win : return True
        
        #checking columns
        win = True
        for i in range(3):
            for j in range(3):
                if self.board[j][i] != mark:
                    win =  False
                    
            if win : return True
        
        #checking the diagonal
        win = True
        for i in range(3):
            if self.board[i][i] != mark :
                win = False
            
        if win : return True

        #checking the anti-diagonal
        win = True
        for i in range(3):
            if self.board[i][2-i] != mark : 
                win = False
        if win : return True
        
        return win
    

    #checks if the matrix is full
    def isBoardFilled(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-' :
                    return False
        
        return True


    def switchPlayer(self, mark):
        if mark == 'X' :
            return 'O'
        else:
            return 'X'

    
    def displayBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j],'|' , end=' ')
            print('\n')
    
    def play(self):
        self.createBoard()

        if (0 == 0):
            mark = 'X'
        else : 
            mark = 'O'
        
        while True:
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            
            print()
            

            #adding the mark to the board
            self.placeMark(row-1 , col-1 , mark)
            self.displayBoard()
            #checking for a winner
            if self.chekWinner(mark):
                print(f"the {mark} wins !")
                break
            

            #checks if the board is filled
            if self.isBoardFilled():
                print("draw !")
                break

            #swapping players
            mark = self.switchPlayer(mark)
           




tictac = TicTacToe()
tictac.play()