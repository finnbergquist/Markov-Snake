import random

class MarkovBoard:
    def __init__(self):
        ''' A two dimentional enviornment with squares. Each square stores a number for how many visits
        the snake has made. That number will determine the color of the square.

        '''

        #Will hold how many times a position has been visited->determining that position's color
        self.visits = [0] * 100
        
        self.transitionMatrix = self.buildTransitionMatrix()

        self.states = list(self.transitionMatrix.keys())

        self.currentState = 0


    def buildTransitionMatrix(self):
        '''Called in the initializer. Creates the transition matrix. Transition probabilties are equal probability
        up, right, down, left. Except for edge cases, they still have equal chance of all possible moves.

        Args: self
        Return: Python Dictionary of Python Dictionaries
        '''
        transitionMatrix = {}
        for i in range(0, 99):
            probDistribution = {}
            for j in range(0,99):
                if j == i-1 or j == i+1 or j == i + 10 or j == i-10:
                    probDistribution[j] = 0.5
                else:
                    probDistribution[j] = 0
                    
            transitionMatrix[i] = probDistribution

        return transitionMatrix

    def transition(self, state):
        '''Returns the next state that the snake goes to
        Args: int previous state
        Return: int next state
        '''
        return random.choices(self.states, weights=list(self.transitionMatrix[state].values()))[0]


    

board = MarkovBoard()
print(board.transition(15))
