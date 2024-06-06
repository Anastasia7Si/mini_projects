"""Игра в 15.
Расставьте пронумерованные костяшки в правильном порядке."""

import random
import sys


BLANK = '  '


def main():
    print('''Slidding Tile Puzzle.
             Use the WASD keys to move the tiles back into
             their original order:
                1 2 3 4
                5 6 7 8
             9 10 11 12
            13 14 15''')
    input('Press Enter to begin...')
    game_board = get_new_puzzle()
    while True:
        display_board(game_board)
        player_move = ask_for_player_move(game_board)
        make_move(game_board, player_move)
        if game_board == get_new_board():
            print('You won!')
            sys.exit()


def get_new_board():
    """Возвращает список списков, соответсвующий новой игре."""

    return [
        ['1 ', '5 ', '9 ', '13'], ['2 ', '6 ', '10', '14'],
        ['3 ', '7 ', '11', '15'], ['4 ', '8 ', '12', BLANK]
    ]


def get_new_puzzle(moves=200):
    """Генерируем новую игру с помощю случайных ходов из упорядоченного
    состояния."""

    board = get_new_board()
    for i in range(moves):
        make_random_move(board)
    return board


def display_board(board):
    """Отображает заданную доску на экране."""

    labels = [
        board[0][0], board[1][0], board[2][0], board[3][0],
        board[0][1], board[1][1], board[2][1], board[3][1],
        board[0][2], board[1][2], board[2][2], board[3][2],
        board[0][3], board[1][3], board[2][3], board[3][3]
    ]
    board_to_draw = """
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+""".format(*labels)
    print(board_to_draw)


def find_blank_space(board):
    """Возвращает кортеж (x, y) с местоположением пустой клетки."""

    for x in range(4):
        for y in range(4):
            if board[x][y] == '  ':
                return (x, y)


def ask_for_player_move(board):
    """Запрашивает у игрока, какую костяшку передвигать."""

    blank_x, blank_y = find_blank_space(board)
    w = 'W' if blank_y != 3 else ' '
    a = 'A' if blank_x != 3 else ' '
    s = 'S' if blank_y != 0 else ' '
    d = 'D' if blank_x != 0 else ' '

    while True:
        print(f'                            ({w})')
        print(f'Enter WASD (or QUIT): ({a}) ({s}) ({d})')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if response in (w + a + s + d).replace(' ', ''):
            return response


def make_move(board, move):
    """Производит заданный ход move на заданной доске board."""

    bx, by = find_blank_space(board)
    if move == 'W':
        board[bx][by], board[bx][by + 1] = board[bx][by + 1], board[bx][by]
    elif move == 'A':
        board[bx][by], board[bx + 1][by] = board[bx + 1][by], board[bx][by]
    elif move == 'S':
        board[bx][by], board[bx][by - 1] = board[bx][by - 1], board[bx][by]
    elif move == 'D':
        board[bx][by], board[bx - 1][by] = board[bx - 1][by], board[bx][by]


def make_random_move(board):
    """Передвигает костяшку случайным образом."""

    blank_x, blank_y = find_blank_space(board)
    valid_moves = []
    if blank_y != 3:
        valid_moves.append('W')
    if blank_x != 3:
        valid_moves.append('A')
    if blank_y != 0:
        valid_moves.append('S')
    if blank_x != 0:
        valid_moves.append('D')
    make_move(board, random.choice(valid_moves))


if __name__ == '__main__':
    main()
