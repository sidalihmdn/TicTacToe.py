import pygame, sys
from time import sleep

from source import TicTacToe

tictac = TicTacToe()
tictac.createBoard()
#tictac.board = [['X' for element in range(3)] for element in range(3)]

#define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)

class board :
    def __init__(self) -> None:
        pygame.init()


        #open a new window
        size    = (600,600)
        self.screen  = pygame.display.set_mode(size)
        pygame.display.set_caption("TIC TAC TOE !")


        #init font
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Minecrafter', 60)
        

        self.carryOn = True
        self.clock   = pygame.time.Clock()
        self.win = False

    def play(self) :
        while self.carryOn:
            #events that could break the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    self.carryOn = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    x , y = pygame.mouse.get_pos()
                    self.putMark(tictac.mark , x , y)
                    self.win = tictac.chekWinner(tictac.mark)
                    winner = tictac.mark
                    tictac.mark = tictac.switchPlayer()
                    
            
            self.screen.fill(WHITE)

            # draw the tic tac toe grid
            self.drawGrid()
            self.drawBoard()

            if self.win :
                textsurface = self.myfont.render(f'THE {winner} WINS !', False, (0, 255, 0))  
                self.screen.blit(textsurface,(170,300))
                self.inititializeBoard()

                
        
            
            # displaying shapes
            pygame.display.flip()

            #refreshiing rate
            self.clock.tick(60)


    # this function draws the board and update it
    def drawBoard(self):
        """
        drawing coordinates :
        i = 0   ->  x = 0        j = 0 ->  y = 0   
        i = 1   ->  x = 200      j = 1 ->  y = 200
        i = 2   ->  x = 400      j = 2 ->  y = 400
        """
        for i in range(3):
            for j in range(3):
                if tictac.board[i][j] == 'X' :
                    # we multiply by 200 to switch from array index to graphic coordinates
                    self.drawX(i*200 , j*200)
                elif tictac.board[i][j] == 'O' :
                    self.drawO(i*200 , j*200)


    # this function draws the grid
    def drawGrid(self):
        for i in [200 , 400]:
            pygame.draw.line(self.screen, BLACK, [i, 0], [i, 600], 5)
            pygame.draw.line(self.screen, BLACK, [0, i], [600, i], 5)


    # draws the X's
    def drawX(self , x , y):
        pygame.draw.line(self.screen, BLACK, [x+20, y+20], [x+160, y+160], 5)
        pygame.draw.line(self.screen, BLACK, [x+160, y+20], [x+20, y+160], 5)
    # draws the O's
    def drawO(self,x,y):
        pygame.draw.circle(self.screen, BLACK, (x+100, y+100) , 80 , 5)

    def putMark(self, mark , x , y) :
        i = int(x/200)
        j = int(y/200)

        tictac.placeMark(i,j,mark)
    
    def inititializeBoard(self):
        tictac.createBoard()
        self.drawBoard
        sleep(1)
        

game  = board()
game.play()       





pygame.quit()


