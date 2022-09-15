# Markov-Snake

This visual graphic generator creates a colored grid with a color changing position moving around.
I am calling this moving position the "Snake".

## Description

The snake in this project has a specific location, it's probability of moving to each of the surrounding 
positions is determined by a markov transition matrix, which gives the snake an equal probability of moving
to all legal moves(up, right, and down), with edge cases accounted for. Some of the walls can be moved through
and the snake will appear on the other side. 


This would represent the probabilities of moving to the each of the neighboring spaces if the snake is located 
in the 1,1 location of this example grid:

<img width="125" alt="Screen Shot 2022-09-14 at 9 21 59 PM" src="https://user-images.githubusercontent.com/61434761/190291266-87cf935f-af58-49d4-aaa0-e08351f2d477.png">




The top cieling would have these probabilities:

<img width="129" alt="Screen Shot 2022-09-14 at 9 22 09 PM" src="https://user-images.githubusercontent.com/61434761/190291284-2701c926-4dab-4b78-af6b-c50f554b2994.png">



But the sides behave this way(the snake can move through one side to the other):

<img width="139" alt="Screen Shot 2022-09-14 at 9 22 16 PM" src="https://user-images.githubusercontent.com/61434761/190291292-f9fd5791-50b3-4f0e-8d8a-52a3029be5a9.png">



The color of the grid square represents the number of time that thesnake has visited that position. 
Also, if the user clicks a specific location, the snake will jumpto that location.

This project is personally meaningful for me because I always found the traditional game of snake oddly amusing.
I would sit and watch my roommate play for hourse, unbable to lift my gaze from his screen. I loved the geometric
aesthetic and the quickly changing colors. I decided to use that as insperation and add way more colors. It is not
necessarily a game in the same way that the original snake game is; however, it still has a user interaction where
the user can click to alter the patterns. A challenge in building this project was making a transition matrix that
is built dybamically based on the grid size entered at the command line. That was a major upgrade to the alternative:
hardcoding the transition matrix. 

A cool next upgrade would be finding ways to alter the transition probabiltites based on user behavior so that the snake
might follow the cursor or replicate pattenrns based on user input.

I do believe this system is capable of very elementary creativity because it is unpredictable while still using human input,
but it does not learn, which I believe is an important element of the creative process.

### Dependencies

* Python
* Pygame
* random


### Executing program

# How to clone the repo:
'''
gh repo clone finnbergquist/Markov-Snake
'''

* How to run the program with default grid size:
```
python graphics.py
```
* How to run the program with variable grid size:
```
python graphics.py int 
```

##Fun Game
Run with a grid size of 10 and try to get rid of all the black squares. This can be done by trying to click on the
black grid squares before the snake makes it back to them enough times to turn the squares back to black again.
It is surprisingly challenging!

## Authors

Finn Bergquist

