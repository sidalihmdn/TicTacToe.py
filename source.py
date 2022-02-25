import random


class TicTacToe:

    def __init__(self):
        self.board = []
        self.player = self.getFirstPlayer()
        self.mark = self.getMark()
        

    def createBoard(self):
        self.board = [['-' for element in range(3)] for element in range(3)]
    
    def resetBoard(self):
        self.board = [['-' for element in range(3)] for element in range(3)]

    def getFirstPlayer(self):
        return random.randint(0, 1)
    
    def placeMark(self ,x , y , mark):
        self.board[x][y] = mark 
        #swapping playersx
    

    #checking for a winner 
    def chekWinner(self,mark):
        print(mark)
        
        #checking rows
        for i in range(3):
            win = True
            for j in range(3):
                if self.board[i][j] != mark:
                    win = False
                    
                
            if win : return True
        
        #checking columns
        
        for i in range(3):
            win = True
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


    def switchPlayer(self):
        if self.mark == 'X' :
            return 'O'
        else:
            return 'X'

    
    def displayBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j],'|' , end=' ')
            print('\n')

    def getMark(self):
        if (True):
            return 'X'
        else : 
            return 'O'


    def play(self):
        self.createBoard()
        mark = self.mark
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

           
           
