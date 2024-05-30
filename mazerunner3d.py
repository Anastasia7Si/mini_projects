"""Трёхмерный дабиринт.
Перемещайтесь по лабиринту и попытайтесь выбраться из него в 3D!
Файлы лабиринтов можно найти по адрсу https://invpy.com/mazes/."""

import copy
import sys
import os


WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617)
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'


def wall_str_to_wall_dict(wall_str):
    """"Получает на входе строковое представление изображения стены
    (например, такое, как в ALL_OPEN и CLOSED) и возвращает её предсталвение
    в виде ассоциативного массива с картежами (x, y) в роли ключей
    и строковых значений из одного символа для вывода на этой позиции x, y."""

    wall_dict = {}
    height = 0
    width = 0
    for y, line in enumerate(wall_str.splitlines()):
        if y > height:
            height = y
        for x, character in enumerate(line):
            if x > width:
                width = x
            wall_dict[(x, y)] = character
    wall_dict['height'] = height + 1
    wall_dict['width'] = width + 1
    return wall_dict


EXIT_DICT = {
    (0, 0): 'E', (1, 0): 'X', (2, 0): 'I',
    (3, 0): 'T', 'height': 1, 'width': 4
}
ALL_OPEN = wall_str_to_wall_dict(r'''
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................'''.strip())
CLOSED = {}
CLOSED['A'] = wall_str_to_wall_dict(r'''
_____
.....
.....
.....
____'''.strip())
CLOSED['B'] = wall_str_to_wall_dict(r'''
.\.
..\
...
...
...
../
./.'''.strip())
CLOSED['C'] = wall_str_to_wall_dict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________'''.strip())
CLOSED['D'] = wall_str_to_wall_dict(r'''
./.
/..
...
...
...
 \..
 .\.'''.strip())
CLOSED['E'] = wall_str_to_wall_dict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..'''.strip())
CLOSED['F'] = wall_str_to_wall_dict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..'''.strip())
PASTE_CLOSED_TO = {
        'A': (6, 4), 'B': (4, 3), 'C': (3, 1),
        'D': (10, 3), 'E': (0, 0), 'F': (12, 0)
    }


def display_wall_dict(wall_dict):
    """Отображает на экране ассоциативный массив стенки,
    возвращаемый wall_str_to_wall_dict()."""

    print(BLOCK * (wall_dict['width'] + 2))
    for y in range(wall_dict['height']):
        print(BLOCK, end='')
        for x in range(wall_dict['width']):
            wall = wall_dict[(x, y)]
            if wall == '.':
                wall = ' '
            print(wall, end='')
        print(BLOCK)
    print(BLOCK * (wall_dict['width'] + 2))


def paste_wall_dict(src_wall_dict, dst_wall_dict, left, top):
    """Копируем ассоциативный массив представления стенки из
    src_wall_dict поверх dst_wall_dict, смещённый до позиции left, top."""

    dst_wall_dict = copy.copy(dst_wall_dict)
    for x in range(src_wall_dict['width']):
        for y in range(src_wall_dict['height']):
            dst_wall_dict[(x + left, y + top)] = src_wall_dict[(x, y)]
    return dst_wall_dict


def make_wall_dict(maze, player_x, player_y, player_direction, exit_x, exit_y):
    """Создаём ассоциативный массив представления стенки в соответствии
    с расположение и направлением движения игрока в лабиринте (с выходом
    в точке exit_x, exit_y) путём вставки ассоциативных массивов стенок
    поверх ALL_OPEN и возвращаем его."""

    if player_direction == NORTH:
        offests = (('A', 0, -2), ('B', -1, -1), ('C', 0, -1),
                   ('D', 1, -1), ('E', -1, 0), ('F', 1, 0))
    if player_direction == SOUTH:
        offests = (('A', 0, 2), ('B', 1, 1), ('C', 0, 1),
                   ('D', -1, 1), ('E', 1, 0), ('F', -1, 0))
    if player_direction == EAST:
        offests = (('A', 2, 0), ('B', 1, -1), ('C', 1, 0),
                   ('D', 1, 1), ('E', 0, -1), ('F', 0, 1))
    if player_direction == WEST:
        offests = (('A', -2, 0), ('B', -1, 1), ('C', -1, 0),
                   ('D', -1, -1), ('E', 0, 1), ('F', 0, -1))
    section = {}
    for sec, x_off, y_off in offests:
        section[sec] = maze.get((player_x + x_off, player_y + y_off), WALL)
        if (player_x + x_off, player_y + y_off) == (exit_x, exit_y):
            section[sec] = EXIT
    wall_dict = copy.copy(ALL_OPEN)
    for sec in 'ABDCEF':
        if section[sec] == WALL:
            wall_dict = paste_wall_dict(CLOSED[sec], wall_dict,
                                        PASTE_CLOSED_TO[sec][0],
                                        PASTE_CLOSED_TO[sec][1])
    if section['C'] == EXIT:
        wall_dict = paste_wall_dict(EXIT_DICT, wall_dict, 7, 9)
    if section['E'] == EXIT:
        wall_dict = paste_wall_dict(EXIT_DICT, wall_dict, 0, 11)
    if section['F'] == EXIT:
        wall_dict = paste_wall_dict(EXIT_DICT, wall_dict, 13, 11)
    return wall_dict


print('Maze runner 3D.')
print('(Maze files are got from https://invpy.com/mazes/)')

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
player_dir = NORTH

while True:
    display_wall_dict(make_wall_dict(maze, player_x, player_y, player_dir,
                                     exit_x, exit_y))
    while True:
        print(f'Location ({player_x}, {player_y})   Direction: {player_dir}')
        print('                     (W)')
        print('Eneter direction:  (A) (D) or QUIT.')
        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if (move not in ['F', 'L', 'R', 'W', 'A', 'D']
           and not move.startswith('T')):
            print('Invalidal direction. Enter one of F, L, or R (or W, A, D).')
            continue
        if move == 'F' or move == 'W':
            if player_dir == NORTH and maze[(player_x, player_y - 1)] == EMPTY:
                player_y -= 1
                break
            if player_dir == SOUTH and maze[(player_x, player_y + 1)] == EMPTY:
                player_y += 1
                break
            if player_dir == EAST and maze[(player_x + 1, player_y)] == EMPTY:
                player_x += 1
                break
            if player_dir == WEST and maze[(player_x - 1, player_y)] == EMPTY:
                player_x -= 1
                break
        elif move == 'L' or move == 'A':
            player_dir = {
                NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH
            }[player_dir]
            break
        elif move == 'R' or move == 'D':
            player_dir = {
                NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH
            }[player_dir]
            break
        elif move.startswith('T'):
            player_x, player_y = move.split()[1].split(',')
            player_x = int(player_x)
            player_y = int(player_y)
            break
        else:
            print('You cannot move in that direction.')
    if (player_x, player_y) == (exit_x, exit_y):
        print('You have reached the exit! Good job!')
        print('Thanks for playing!')
        sys.exit()
