# Markov-Snake

This visual graphic generator creates a colored grid with a color changing position moving around.
I am calling this moving position the "Snake".

## Description

The snake in this project has a specific location, it's probability of moving to each of the surrounding 
positions is determined by a markov transition matrix, which gives the snake an equal probability of moving
to all legal moves(up, right, and down), with edge cases accounted for. Some of the walls can be moved through
and the snake will appear on the other side. The color of the grid square represents the number of time that the
snake has visited that position.  Also, if the user clicks a specific location, the snake will jump
to that location.

### Dependencies

* Python
* Pygame
* random


### Executing program

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

