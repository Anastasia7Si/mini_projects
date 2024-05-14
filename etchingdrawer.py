"""Гравировщик.
Графическая программа, рисующая непрерывную линию на экране с помощью
клавиш WASD. Создана под влиянием игры "Ыолшебный экран".

Например, нарисовать фрактальную кривую Гильберта можно с помощью:
SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW

Или даже ещё большую фрактальную кривую Гильберта с помощью:
DDSAASSDDWDDSDDWWAAWDDDDSDDWDDDDSAASDDSAAAAWAASSSDDWDDDDSAASDDSAAAAWA
ASAAAAWDDWWAASAAWAASSDDSAASSDDWDDDDSAASDDSAAAAWAASSDDSAASSDDWDDSDDWWA
AWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWAAWDDDDSDDWDDSDDWDDDDSAASDDS
AAAAWAASSDDSAASSDDWDDSDDWWAAWDDDDDDSAASSDDWDDSDDWWAAWDDWWAASAAAAWDDWA
AWDDDDSDDWWAAWDDWWAASAAWAASSDDSAAAAWAASAAAAWDDWAAWDDDDSDDWWWAASAAAAWD
DWAAWDDDDSDDWDDDDSAASSDDWDDSDDWWAAWDD"""

import shutil
import sys

UP_DOWN_CHAR = chr(9474)
LEFT_RIGHT_CHAR = chr(9472)
DOWN_RIGHT_CHAR = chr(9484)
DOWN_LEFT_CHAR = chr(9488)
UP_RIGHT_CHAR = chr(9492)
UP_LEFT_CHAR = chr(9496)
UP_DOWN_RIGHT_CHAR = chr(9500)
UP_DOWN_LEFT_CHAR = chr(9508)
DOWN_LEFT_RIGHT_CHAR = chr(9516)
UP_LEFT_RIGHT_CHAR = chr(9524)
CROSS_CHAR = chr(9532)

CANVAS_WIDTH = shutil.get_terminal_size()[0] - 1
CANVAS_HEIGHT = shutil.get_terminal_size()[0] - 5

"""Ключи ассоциативного массива canvas представляют собой целочисленные
кортежи (x, y) координат, а значение - набор букыв W, A, S, D, описывающих
тип отрисовываемой линии."""

canvas = {}
cursor_x = 0
cursor_y = 0


def get_canvas_string(canvas_data, c_x, c_y):
    """Возвращает многострочное значение рисуемой в canvas_data линии."""
    canvas_str = ''

    """canvas_data - ассоциативный массив с ключами (x, y) и значениями
    в виже множеств из строк символов 'W', 'A', 'S', 'D', описыавющих,
    в каком направлени идёт линия в каждой точке xy."""
    for row_number in range(CANVAS_HEIGHT):
        for column_number in range(CANVAS_WIDTH):
            if column_number == c_x and row_number == c_y:
                canvas_str += '#'
                continue

            cell = canvas_data.get((column_number, row_number))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvas_str += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvas_str += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvas_str += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvas_str += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvas_str += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                canvas_str += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvas_str += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvas_str += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvas_str += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvas_str += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvas_str += CROSS_CHAR
            elif cell is None:
                canvas_str += ' '
        canvas_str += '\n'
    return canvas_str


moves = []
while True:
    print(get_canvas_string(canvas, cursor_x, cursor_y))
    print('WASD keys to move, H for help, C to clear, F to save, or QUIT.')
    response = input('> ').upper()

    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
    elif response == 'H':
        print('Enter W, A, S, D characters to move the cursor and')
        print('draw a line behind it as it moves. For example, ddd')
        print('draws a line going right and sssdddwwwaaa draws a box.')
        print()
        print('You can save your drawing to a text file by entering F.')
        input('Press Enter to return to the program...')
        continue
    elif response == 'C':
        canvas = {}
        moves.append('C')
    elif response == 'F':
        try:
            print('Enter filename to save to:')
            filename = input('> ')

            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(get_canvas_string(canvas, None, None))
        except Exception:
            print('ERROR: Could not save file.')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue
        moves.append(command)

        if canvas == {}:
            if command in ('W', 'S'):
                canvas[(cursor_x, cursor_y)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                canvas[(cursor_x, cursor_y)] = set(['A', 'D'])

        if command == 'W' and cursor_y > 0:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_y = cursor_y - 1
        elif command == 'S' and cursor_y < CANVAS_HEIGHT - 1:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_y = cursor_y + 1
        elif command == 'A' and cursor_y > 0:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_x = cursor_x - 1
        elif command == 'D' and cursor_y < CANVAS_WIDTH - 1:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_x = cursor_x + 1
        else:
            continue

        if (cursor_x, cursor_y) not in canvas:
            canvas[(cursor_x, cursor_y)] = set()

        if command == 'W':
            canvas[(cursor_x, cursor_y)].add('S')
        elif command == 'S':
            canvas[(cursor_x, cursor_y)].add('W')
        elif command == 'A':
            canvas[(cursor_x, cursor_y)].add('D')
        elif command == 'D':
            canvas[(cursor_x, cursor_y)].add('A')
