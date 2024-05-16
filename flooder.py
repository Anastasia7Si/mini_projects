"""Заливка.
Многоцветная игра, в которой нужно заполнить игралную доску одним цветом.
Включает специальный режим для игроков с дальтонизмом.
По мотивам игры Flood It!"""

import random
import sys

try:
    import bext
except ImportError:
    print('This program requires the bext mobule, which you')
    print('can install with command "pip install Bext".')
    sys.exit()

BOARD_WIDTN = 16
BOARD_HEIGHT = 14
MOVES_PER_GAME = 20

HEART = chr(9829)
DIAMOND = chr(9830)
SPADE = chr(9824)
CLUB = chr(9827)
BALL = chr(9679)
TRIANGLE = chr(9650)

BLOCK = chr(9608)
LEFT_RIGHT = chr(9472)
UP_DOWN = chr(9474)
DOWN_RIGHT = chr(9484)
DOWN_LEFT = chr(9488)
UP_RIGHT = chr(9492)
UP_LEFT = chr(9496)

TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: 'red', 1: 'green', 2: 'blue',
              3: 'yellow', 4: 'cyan', 5: 'purple'}
COLOR_MODE = 'color_mode'
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND,
              3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = 'shape_mode'


def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print('''Flooder.
             Set the upper left color/shape, whitch fills in all the
             adjacent squares of that color/shape. Try to make the
             entire board the same color/shape.''')
    print('Do you wont to play in colorblind mode? Y/N')
    response = input('> ')
    if response.upper().startswith('Y'):
        display_mode = SHAPE_MODE
    else:
        display_mode = COLOR_MODE

    game_board = get_new_board()
    moves_left = MOVES_PER_GAME

    while True:
        display_board(game_board, display_mode)

        print('Moves left: ', moves_left)
        player_move = ask_for_player_move(display_mode)
        change_tile(player_move, game_board, 0, 0)
        moves_left -= 1

        if has_won(game_board):
            display_board(game_board, display_mode)
            print('You have won!')
            break
        elif moves_left == 0:
            display_board(game_board, display_mode)
            print('You have run out of moves!')
            break


def get_new_board():
    """Возвращает ассоциативный массив с новой доской "Заливки"."""
    board = {}
    for x in range(BOARD_WIDTN):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = random.choice(TILE_TYPES)

    for i in range(BOARD_WIDTN * BOARD_HEIGHT):
        x = random.randint(0, BOARD_WIDTN - 2)
        y = random.randint(0, BOARD_HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]
    return board


def display_board(board, display_mode):
    """Выводит игральную доску на экран."""
    bext.fg('white')
    print(DOWN_RIGHT + (LEFT_RIGHT * BOARD_WIDTN) + DOWN_LEFT)

    for y in range(BOARD_HEIGHT):
        bext.fg('white')
        if y == 0:
            print('>', end='')
        else:
            print(UP_DOWN, end='')

        for x in range(BOARD_WIDTN):
            bext.fg(COLORS_MAP[board[(x, y)]])
            if display_mode == COLOR_MODE:
                print(BLOCK, end='')
            elif display_mode == SHAPE_MODE:
                print(SHAPES_MAP[board[(x, y)]], end='')

        bext.fg('white')
        print(UP_DOWN)
    print(UP_RIGHT + (LEFT_RIGHT * BOARD_WIDTN) + UP_LEFT)


def ask_for_player_move(display_mode):
    """Даём возможность игроку выбрать цвет верхнего левого элемента."""
    while True:
        bext.fg('white')
        print('Choose one of: ', end='')
        if display_mode == COLOR_MODE:
            bext.fg('red')
            print('(R)ed ', end='')
            bext.fg('green')
            print('(G)reen ', end='')
            bext.fg('blue')
            print('(B)lue ', end='')
            bext.fg('yellow')
            print('(Y)ellow ', end='')
            bext.fg('cyan')
            print('(C)yan ', end='')
            bext.fg('purple')
            print('(P)urple ', end='')
        elif display_mode == SHAPE_MODE:
            bext.fg('red')
            print('(H)eart ', end='')
            bext.fg('green')
            print('(T)riangle ', end='')
            bext.fg('blue')
            print('(D)iamond ', end='')
            bext.fg('yellow')
            print('(B)all ', end='')
            bext.fg('cyan')
            print('(C)lub ', end='')
            bext.fg('purple')
            print('(S)pade ', end='')
        bext.fg('white')
        print('or QUIT')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if display_mode == COLOR_MODE and response in tuple('RGBYCP'):
            return {'R': 0, 'G': 1, 'B': 2,
                    'Y': 3, 'C': 4, 'P': 5}[response]
        if display_mode == SHAPE_MODE and response in tuple('HTDBCS'):
            return {'H': 0, 'T': 1, 'D': 2,
                    'B': 3, 'C': 4, 'S': 5}[response]


def change_tile(tile_type, board, x, y, char_to_change=None):
    """Меняем цвет/форму клетки с помощью алгооритма рекурсивной заливки."""
    if x == 0 and y == 0:
        char_to_change = board[(x, y)]
        if tile_type == char_to_change:
            return

    board[(x, y)] = tile_type

    if x > 0 and board[(x - 1, y)] == char_to_change:
        change_tile(tile_type, board, x - 1, y, char_to_change)
    if y > 0 and board[(x, y - 1)] == char_to_change:
        change_tile(tile_type, board, x, y - 1, char_to_change)
    if x < BOARD_WIDTN - 1 and board[(x + 1, y)] == char_to_change:
        change_tile(tile_type, board, x + 1, y, char_to_change)
    if y < BOARD_HEIGHT - 1 and board[(x, y + 1)] == char_to_change:
        change_tile(tile_type, board, x, y + 1, char_to_change)


def has_won(board):
    """Возвращает True, если вся доска - одного цвета/формы."""
    tile = board[(0, 0)]

    for x in range(BOARD_WIDTN):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] != tile:
                return False
    return True


if __name__ == '__main__':
    main()
