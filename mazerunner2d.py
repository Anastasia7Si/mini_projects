"""Бегущий в лабиринте.
Перемещайтесь по лабиринту и попытайтесь выбраться из него.
Файлы лабиринтов можно найти по адрсу https://invpy.com/mazes/."""

import sys
import os


WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
PLAYER = '@'
BLOCK = chr(9617)


def display_maze(maze):
    """Отображаем лабиринт на экране."""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (player_x, player_y):
                print(PLAYER, end='')
            elif (x, y) == (exit_x, exit_y):
                print('X', end='')
            elif maze[(x, y)] == WALL:
                print(BLOCK, end='')
            else:
                print(maze[(x, y)], end='')
        print()


print('''Maze Runner 2D.''')

while True:
    print('Enter the file name of the maze (or LIST or QUIT):')
    filename = input('> ')
    if filename.upper() == 'LIST':
        print('Maze files found in ', os.getcwd())
        for file_in_current_folder in os.listdir():
            if (file_in_current_folder.startswith('maze') and
               file_in_current_folder.endswith('txt')):
                print('   ', file_in_current_folder)
        continue
    if filename.upper() == 'QUIT':
        sys.exit()
    if os.path.exists(filename):
        break
    print('There is no file named ', filename)

maze_file = open(filename)
maze = {}
lines = maze_file.readlines()
player_x = None
player_y = None
exit_x = None
exit_y = None
y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (WALL, EMPTY, START, EXIT), (f'Invalid character '
                                                         f'at column {x + 1},'
                                                         f'line {y + 1}.')
        if character in (WALL, EMPTY):
            maze[(x, y)] = character
        elif character == START:
            player_x, player_y = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exit_x, exit_y = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert player_x is not None and player_y is not None, 'No start in maze file.'
assert exit_x is not None and exit_y is not None, 'No exit in maze file.'

while True:
    display_maze(maze)
    while True:
        print('                           W')
        print('Enter direction, or QUIT: ASD.')
        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if move not in ['W', 'A', 'S', 'D']:
            print('Invalidal direction. Enter one of W, A, S, or D.')
            continue
        if move == 'W' and maze[(player_x, player_y - 1)] == EMPTY:
            break
        elif move == 'A' and maze[(player_x - 1, player_y)] == EMPTY:
            break
        elif move == 'S' and maze[(player_x, player_y + 1)] == EMPTY:
            break
        elif move == 'D' and maze[(player_x + 1, player_y)] == EMPTY:
            break
        print('You cannot move in that direction.')
    if move == 'W':
        while True:
            player_y -= 1
            if (player_x, player_y) == (exit_x, exit_y):
                break
            if maze[(player_x, player_y - 1)] == WALL:
                break
            if (maze[(player_x - 1, player_y)] == EMPTY
               or maze[((player_x + 1, player_y))] == EMPTY):
                break
    elif move == 'A':
        while True:
            player_x -= 1
            if (player_x, player_y) == (exit_x, exit_y):
                break
            if maze[(player_x - 1, player_y)] == WALL:
                break
            if (maze[(player_x, player_y - 1)] == EMPTY
               or maze[((player_x, player_y + 1))] == EMPTY):
                break
    elif move == 'S':
        while True:
            player_y += 1
            if (player_x, player_y) == (exit_x, exit_y):
                break
            if maze[(player_x, player_y + 1)] == WALL:
                break
            if (maze[(player_x - 1, player_y)] == EMPTY
               or maze[((player_x + 1, player_y))] == EMPTY):
                break
    elif move == 'D':
        while True:
            player_x += 1
            if (player_x, player_y) == (exit_x, exit_y):
                break
            if maze[(player_x + 1, player_y)] == WALL:
                break
            if (maze[(player_x, player_y - 1)] == EMPTY
               or maze[((player_x, player_y + 1))] == EMPTY):
                break
    if (player_x, player_y) == (exit_x, exit_y):
        display_maze(maze)
        print('You have reached the exit! Good job!')
        print('Thanks for playing!')
        sys.exit()
