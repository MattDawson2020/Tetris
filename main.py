import sys
import pygame
import random

pygame.init()

# screen dimensions
WIDTH = 800
HEIGHT = 600

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLOURS = [RED, BLUE, GREEN]

# Tetris shapes
SHAPES = [
    [
        ['.....',
         '.....',
         '.....',
         'OOOO.',
         '.....'],
        ['.....',
         '..O..',
         '..O..',
         '..O..',
         '..O..']
    ],
    [
        ['.....',
         '.....',
         '..O..',
         '.OOO.',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '..OO.',
         '..O..',
         '.....']
    ],
    [
        [
         '.....',
         '.....',
         '..OO.',
         '.OO..',
         '.....'],
        ['.....',
         '.....',
         '.OO..',
         '..OO.',
         '.....'],
        ['.....',
         '.O...',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '.O...',
         '.....']
    ],
    [
        ['.....',
         '..O..',
         '..O.',
         '..OO.',
         '.....'],
        ['.....',
         '...O.',
         '.OOO.',
         '.....',
         '.....'],
        ['.....',
         '.OO..',
         '..O..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '.O...',
         '.....']
    ],
]


def main():
    # initialise the game
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("LEFT")
                if event.key == pygame.K_RIGHT:
                    print("RIGHT")
                if event.key == pygame.K_DOWN:
                    print("DOWN")
                if event.key == pygame.K_UP:
                    print("UP")
                if event.key == pygame.K_SPACE:
                    print("SPACE")


if __name__ == "__main__":
    main()