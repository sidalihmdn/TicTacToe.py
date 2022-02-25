from matplotlib.pyplot import draw
import pygame, sys

from sqlalchemy import false
from source import TicTacToe

tictac = TicTacToe()
tictac.createBoard()
#tictac.board = [['X' for element in range(3)] for element in range(3)]


class board :
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
            pygame.draw.line(screen, BLACK, [i, 0], [i, 600], 5)
            pygame.draw.line(screen, BLACK, [0, i], [600, i], 5)
    # draws the X's
    def drawX(self , x , y):
        pygame.draw.line(screen, BLACK, [x+20, y+20], [x+160, y+160], 5)
        pygame.draw.line(screen, BLACK, [x+160, y+20], [x+20, y+160], 5)
    # draws the O's
    def drawO(self,x,y):
        pygame.draw.circle(screen, BLACK, (x+100, y+100) , 80 , 5)

    def putMark(self, mark , x , y) :
        i = int(x/200)
        j = int(y/200)

        tictac.placeMark(i,j,mark)
        

        

pygame.init()

#define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)

#open a new window
size    = (600,600)
screen  = pygame.display.set_mode(size)
pygame.display.set_caption("TIC TAC TOE !")


#init font
pygame.font.init()
myfont = pygame.font.SysFont('Minecrafter', 60)
  

carryOn = True
clock   = pygame.time.Clock()
b = board()
win = False

# main loop
while carryOn:
    #events that could break the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONUP:
            x , y = pygame.mouse.get_pos()
            b.putMark(tictac.mark , x , y)
            win = tictac.chekWinner(tictac.mark)
            winner = tictac.mark
            tictac.mark = tictac.switchPlayer()
            
    
    #game logic goes here 

    #drawing code 
    #clear the screen 
    screen.fill(WHITE)

    # draw the tic tac toe grid
    b.drawGrid()
    b.drawBoard()

    if win :
        textsurface = myfont.render(f'THE {winner} WINS !', False, (0, 255, 0))  
        screen.blit(textsurface,(170,300))
   
    
    # displaying shapes
    pygame.display.flip()

    #refreshiing rate
    clock.tick(60)

pygame.quit()


