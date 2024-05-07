"""Игра "Жизнь" Конвея.
Клеточный автомат для имитационного моделирования."""

import copy
import random
import sys
import time

WIDTH = 79
HEIGHT = 20

ALIVE = 'O'
DEAD = ' '

next_cells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            next_cells[(x, y)] = ALIVE
        else:
            next_cells[(x, y)] = DEAD

while True:
    cells = copy.deepcopy(next_cells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')
        print()
    print('Press Ctrl-C to quit.')

    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            number_neighbors = 0
            if cells[(left, above)] == ALIVE:
                number_neighbors += 1
            if cells[(x, above)] == ALIVE:
                number_neighbors += 1
            if cells[(right, above)] == ALIVE:
                number_neighbors += 1
            if cells[(right, y)] == ALIVE:
                number_neighbors += 1
            if cells[(right, below)] == ALIVE:
                number_neighbors += 1
            if cells[(x, below)] == ALIVE:
                number_neighbors += 1
            if cells[(x, below)] == ALIVE:
                number_neighbors += 1
            if cells[(left, below)] == ALIVE:
                number_neighbors += 1
            if cells[(left, y)] == ALIVE:
                number_neighbors += 1

            if cells[(x, y)] == ALIVE and (number_neighbors == 2
                                           or number_neighbors == 3):
                next_cells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and number_neighbors == 3:
                next_cells[(x, y)] = ALIVE
            else:
                next_cells[(x, y)] = DEAD
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print('Conway\'s Game of Life.')
        sys.exit()
