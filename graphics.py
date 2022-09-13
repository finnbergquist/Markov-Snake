import constants
import sys
import board
import numpy as np
import pygame


def intitialize():
    '''
    Creates pygame instance, and intializes the board size as specified with constants
    Args: 
        none
    Return: 
        none
    '''
    pygame.init()
    display = pygame.display.set_mode((constants.WIDTH,constants.HEIGHT))
    display.fill(constants.WHITE)
    return display

def getColor(visits):
    '''Given number of visits, return what color the square should be

    Args: 
        visits: int number of visits at a specific position
    Return: 
        color: (x,y,z) where x,y,z represent values of red green and blue in color vector
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
    ''' Given our display pygame instance and number of visits list, create visual representaiton
    of the board. Will create a pygame.Rect at each position

    Args:
        display: pygame.display object
        numberBoard: List of size the same as the number of squares
    Return: 
        none

    '''
    for i, num in enumerate(numberBoard):
        #ex. Square 23 is at (2,3)
        x = i % (constants.NUMBER_OF_SQUARES_HIGH)
        y = i //(constants.NUMBER_OF_SQUARES_HIGH)
        color = getColor(numberBoard[i]) 

        #Rect(left, top, width, height)
        square = pygame.Rect(x*constants.SQUARE_WIDTH, y*constants.SQUARE_HEIGHT, constants.SQUARE_WIDTH, constants.SQUARE_HEIGHT)
        pygame.draw.rect(display, color, square)


def gameLoop(display, markovBoard):
    ''' Infinite loop with time breaks in between each loop. The loop will first check
    for any quit events, and exit if there is one. Then it will create the rectangle objects
    for the board using thebuilt in pygame methods in the showBoard method. Then it transitions 
    the markovBoard which will change the visits list. Finally it updates the display with the 
    new colors for the board and then waits a few milliseconds.

    Args:
        display: pygame.display object
        markovBoard: markovBoard object with transition matrix and visit count
    Return:
        none
    
    '''
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
