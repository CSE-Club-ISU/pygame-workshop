# pygame-workshop
An interactive, simple tutorial to make a game with Python using pygame

## Table of Contents
- [Environment Setup](#environment-setup)
- [Basic Pygame Setup](#basic-pygame-setup)
- [Useful Pygame Functions](#useful-pygame-functions)

## Environment Setup

### Install Python

- [Official Download](https://www.python.org/downloads/)

- If you are unfamiliar Python, don't worry! Here are some great quickstart guides for your reference:
    - [Python Cheatsheet](https://quickref.me/python)
    - [Learn X in Y Minutes (Python Edition)](https://learnxinyminutes.com/python/)

### Setup your development environment

1. Open a new project in your IDE (like VSCode)

2. Open a terminal in your project directory

3. Setup a virtual environment
    1. In your terminal, while in the project directroy, run `python -m venv venv`.
        - This will create a new folder called `venv` in your project directory
        - This folder will contain the python packages, like `pygame`, you install for the project

        >If you get an error, try running `python3 -m venv venv`

    2. Then, activate the virtual environment by running the activation script
        - MacOS: `source venv/bin/activate`
        - Windows: `venv\Scripts\activate`

4. Install pygame by running `pip install pygame`
    - `pip` is a package manager for python; use it to install packages you need for your project

5. Create the python file for the game!

## Basic Pygame Setup
1. First, in your main `.py` file, import the pygame library

    ```python
    import pygame
    ```

2. After pygame is imported, initialize pygame by calling the pygame's `init` function

    ```python
    import pygame

    pygame.init()
    ```

3. Now, we can setup the window and the 'clock' (games internal timer)

    ```python
    # ...

    # variables for the window size
    WIDTH, HEIGHT = 800, 600
    # init a pygame window. the set_mode function takes in a tuple (similar to a list, but immutable) for the window size
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # initialize the clock
    clock = pygame.time.Clock()
    ```

4. Now, we can setup the game loop

    ```python
    # ...

    game_over = False

    # game loop. when you run this python file, the program will spend most of its time in this loop
    while not game_over:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if the user closes the window, exit the game loop
                pygame.quit()
                sys.exit()

            # game logic will go here!

            # draw logic will go here!
            ## clear the screen every frame before re-drawing
            screen.fill((0, 0, 0))
            ## custom drawing logic goes here
            ## ...
            ## update the display with the newly drawn frame
            pygame.display.update()

            # update the clock. `clock.tick()` takes one argument, framerate
            clock.tick(60)
    ```

## Useful Pygame Functions

### Drawing

```python
# draw a rectangle
# PARAMS:
# screen is the window
# color is the color of the rectangle. simplest is to pass a tuple of RGB values, e.g. (255, 0, 0)
# rect is the rectangle, a tuple of (x, y, width, height)
    # x is left to right position of top left corner of the rectangle
    # y is top to bottom position of top left corner of the rectangle
    # width is the width of the rectangle (left to right)
    # height is the height of the rectangle (top to bottom)
pygame.draw.rect(screen, color, rect)

# draw a circle
# PARAMS:
# center is a point (a tuple of (x, y) coordinates)
pygame.draw.circle(screen, color, center, radius)

# draw a line
# PARAMS:
# start and end are points
pygame.draw.line(screen, color, start, end)
```

### Input Events

```python
# get the current state of the keys
keys = pygame.key.get_pressed()
# if 'a' key is pressed
if keys[pygame.K_a]:
    # do something
```

The official pygame documentation can be found [here](https://www.pygame.org/docs/), including basic examples. 

Your IDE (more specifically, the language server which your IDE manages) can also be very helpful when navigating external libraries.

Don't forget the [Python Cheatsheet](https://quickref.me/python) and [Learn X in Y Minutes (Python Edition)](https://learnxinyminutes.com/python/) for Python things too.
