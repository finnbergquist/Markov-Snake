import random
import constants

class MarkovBoard:
    def __init__(self, num_squares=(constants.NUMBER_OF_SQUARES_HIGH*constants.NUMBER_OF_SQUARES_WIDE)):
        ''' A two dimentional enviornment with squares. Each square stores a number for how many visits
        the snake has made. That number will determine the color of the square.

        Args:
            num_squares: board size, by default set to number of squares wide*high
        Return:
            none
        '''
        self.num_squares = num_squares

        #Will hold how many times a position has been visited->determining that position's color
        self.visits = [0] * num_squares
        
        self.transitionMatrix = self.buildTransitionMatrix()

        self.states = list(self.transitionMatrix.keys())

        self.currentState = 0 # default initial state set to 0


    def buildTransitionMatrix(self):
        '''Called in the initializer. Creates the transition matrix. Transition probabilties are equal probability
        up, right, down, left. Except for edge cases, they still have equal chance of all possible moves.

        Args: 
            none
        Return: 
            transitionMatrix: Python Dictionary of Python Dictionaries
        '''
        transitionMatrix = {}
        for i in range(0, self.num_squares-1):
            probDistribution = {}
            for j in range(0,self.num_squares-1):
                if j == i-1 or j == i+1 or j == i + (self.num_squares**(1/2)) or j == i-(self.num_squares**(1/2)):
                    probDistribution[j] = 0.5
                else:
                    probDistribution[j] = 0
                    
            transitionMatrix[i] = probDistribution

        return transitionMatrix

    def transition(self):
        '''Sets the next state that the snake goes to, and updates the visit count list
        Args: 
            none
        Return: 
            none
        '''
        nextState = random.choices(self.states, weights=list(self.transitionMatrix[self.currentState].values()))[0]
        self.visits[nextState] += 1
        self.currentState = nextState
        return


    
'''
board = MarkovBoard()
print(board.currentState)
board.transition()
print(board.currentState)
board.transition()
print(board.currentState)
board.transition()
print(board.currentState)
board.transition()
print(board.currentState)
board.transition()
print(board.currentState)
board.transition()
print(board.currentState)


print(board.visits)'''