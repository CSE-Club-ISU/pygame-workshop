import random
import sys

import pygame

pygame.init()

"""
GLOBAL VARIABLES
"""

# pygame stuff
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# player stuff
player_size = 50
player_color = (0, 128, 255)
player_speed = 5
## init player pos at the bottom-center of the screen
player_x = (WIDTH-player_size) // 2
player_y = HEIGHT - player_size
player_pos = [player_x, player_y]

# enemy stuff
enemy_list = []
enemy_size = 20
enemy_color = (255, 0, 0)
enemy_speed = 5
max_enemy = 30

# for the game loop
run = True

"""
GAME LOGIC
"""
# function which handles 4-directional player movement
def handle_player_movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_d] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_w] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_s] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed

# function which will attempt to spawn an enemy
def spawn_enemy():
    # check if there are less than the maximum number of blocks AND generate a random number (0-1) and see if its less than 0.3,
    # essentially creating a 30% chance of spawning a block
    if len(enemy_list) < max_enemy and random.random() < 0.3:
        # generate random x position
        x_pos = random.randint(0, WIDTH - enemy_size)
        # add the block's coordinates to the list
        # note that the coordinate pair is in a list [x, y]; we use a list instead of a tuple because tuples are immutable
        enemy_list.append([x_pos, -enemy_size])

# function which updates the enemy positions to make them fall
def update_enemy_positions():
    # update each enemy's y position
    for enemy in enemy_list:
        enemy[1] += enemy_speed

    # update the list in-place (aka, modifying the actual list that was given)
    # with all of the enemies whose height is still less than the height of the screen
    enemy_list[:] = [e for e in enemy_list if e[1] < HEIGHT]

# check for collisions by checking manually for overlap
def collision_check(enemy_list, player_pos):
    # player corners
    player_left = player_pos[0]
    player_right = player_pos[0] + player_size
    player_top = player_pos[1]
    player_bottom = player_pos[1] + player_size

    for enemy in enemy_list:
        # enemy corners
        enemy_left = enemy[0]
        enemy_right = enemy[0] + enemy_size
        enemy_top = enemy[1]
        enemy_bottom = enemy[1] + enemy_size

        # check for overlap
        x_overlap = (enemy_left < player_right) and (enemy_right > player_left)
        y_overlap = (enemy_top < player_bottom) and (enemy_bottom > player_top)

        if x_overlap and y_overlap:
            return True # Collision detected!

    return False

# check for collisions by using pygame built-in rectangle collision detection
def collision_check_lib(enemy_list, player_pos):
    # player boundaries
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)

    for enemy in enemy_list:
        # enemy boundaries
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
        if player_rect.colliderect(enemy_rect):
            return True

    return False

"""
DRAWING LOGIC
"""
# simple function which draws the player
def draw_player():
    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))

# function which draws every enemy
def draw_enemies():
    for enemy in enemy_list:
        pygame.draw.rect(screen, enemy_color, (enemy[0], enemy[1], enemy_size, enemy_size))

"""
GAME LOOP
"""
while run:
    # quit the game if the player closes the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # game logic
    handle_player_movement()
    spawn_enemy()
    update_enemy_positions()

    # draw logic
    ## clear the screen every frame before re-drawing
    screen.fill((0, 0, 0))
    draw_player()
    draw_enemies()
    ## update the display with the newly drawn frame
    pygame.display.update()

    # check for collisions
    if collision_check(enemy_list, player_pos):
        run = False

    # this needs to be called once per frame
    # if you are curious to how this works, look up pygame.time.Clock documentation,
    # then look for the tick() function
    clock.tick(60)

print("Game Over!")
