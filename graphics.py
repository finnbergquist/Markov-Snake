import constants
import sys
import board
import numpy as np
import pygame


def intitialize():
    pygame.init()
    display = pygame.display.set_mode((constants.WIDTH,constants.HEIGHT))
    display.fill(constants.WHITE)

    #set caption?

    return display

def getColor(visits):
    '''Given number of visits, return what color the square should be
    
    '''
    color = constants.BLACK #default
    num = visits%10
    if num == 1:
        color = constants.GREY
    if num == 2:
        color = constants.RED
    if num == 3:
        color = constants.BLUE
    if num == 4:
        color = constants.GREEN
    if num == 5:
        color = constants.GOLD
    if num == 6:
        color = constants.DARKGREEN
    if num == 7:
        color = constants.DARKGREY
    if num == 8:
        color = constants.DARKORANGE
    if num == 9:
        color = constants.BROWN

    return color
        


def showBoard(display, numberBoard):
    '''
    '''

    for i, num in enumerate(numberBoard):
        #Square 23 is at (2,3)
        x = i % (constants.NUMBER_OF_SQUARES_HIGH)
        y = i //(constants.NUMBER_OF_SQUARES_HIGH)
        color = getColor(numberBoard[i]) #getColor

        #Rect(left, top, width, height)
        square = pygame.Rect(x*constants.SQUARE_WIDTH, y*constants.SQUARE_HEIGHT, constants.SQUARE_WIDTH, constants.SQUARE_HEIGHT)
        pygame.draw.rect(display, color, square)


def gameLoop(display, markovBoard):

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
            
        showBoard(display, markovBoard.visits)
        markovBoard.transition()
        pygame.display.update()
        pygame.time.wait(10)# wait 100 milliseconds




def main():
    display = intitialize()
    markovBoard = board.MarkovBoard()
    gameLoop(display, markovBoard)




if __name__=="__main__":
    main()
