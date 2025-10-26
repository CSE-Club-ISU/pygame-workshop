# pygame-workshop
An interactive, simple tutorial to make a game with Python using pygame

## Environment Setup

### Install Python

- [Official Download](https://www.python.org/downloads/)

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

    `import pygame`

2. After pygame is imported, initialize pygame by calling the pygame's `init` function

    `pygame.init()`

3. Now, we can setup the window and the 'clock' (games internal timer)

    ```python
        # variables for the window size
        WIDTH, HEIGHT = 800, 600
        # init a pygame window. the set_mode function takes in a tuple (similar to a list, but immutable) for the window size
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # initialize the clock
        clock = pygame.time.Clock()
    ```

4. Now, we can setup the game loop

    ```python

    game_over = False

    # game loop. when you run this python file, the program will spend most of its time in this loop
    while not game_over:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if the user closes the window, exit the game loop
                pygame.quit()
                sys.exit()

            # game code will go here!

            # update the clock. `clock.tick()` takes one argument, framerate
            clock.tick(60)
    ```
