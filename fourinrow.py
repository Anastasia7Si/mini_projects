"""Четыре в ряд.
Игра с отбрасыванием игровых элементов, требуюзая выстроить
четыре в ряд, аналогично игре Connect Four."""

import sys

EMPTY_SPACE = '.'
PLAYER_X = 'X'
PLAYER_O = 'O'

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABLES = ('1', '2', '3', '4', '5', '6', '7')
assert len(COLUMN_LABLES) == BOARD_WIDTH


def main():
    print(''' Four in a Row.
             Two players take turns dropping tiles into one of seven columns,
             trying to make four in a row horizontally, vertically or
             diagonally.''')

    game_board = get_new_board()
    player_turn = PLAYER_X

    while True:
        display_board(game_board)
        player_move = ask_for_player_move(player_turn, game_board)
        game_board[player_move] = player_turn

        if is_winner(player_turn, game_board):
            display_board(game_board)
            print(f'Player {player_turn} has won!')
            sys.exit()
        elif is_full(game_board):
            display_board(game_board)
            print('There is a tie!')
            sys.exit()

        if player_turn == PLAYER_X:
            player_turn = PLAYER_O
        elif player_turn == PLAYER_O:
            player_turn = PLAYER_X


def get_new_board():
    """Возвращает ассоциативный массив, соответствующий игральное доске
    для Connect Four.
    Ключами служат кортежи (column_index, row_index) из двух целых чисел,
    а занчениями - одно из строковых значений 'X', 'O' или '.' (пустое
    место). """

    board = {}
    for column_index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT):
            board[(column_index, row_index)] = EMPTY_SPACE
    return board


def display_board(board):
    """Отображает доску и все клетки на экране.
    Подготовка списка для передачи в строковой метод format()
    для шаблона доски. В этом спике хранятся все клетки доски
    (и пустые участки) слева направо, сверху вниз:"""

    tile_chars = []
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            tile_chars.append(board[(column_index, row_index)])
    print("""
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+""".format(*tile_chars))


def ask_for_player_move(player_tile, board):
    """Даём возможность игроку выбрать столбец на доске
    для размещения элемента.
    Возвращает кортеж (столбец, строка), в который попадает элемент."""

    while True:
        print(f'Player {player_tile}, enter a column or QIUT.')
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response not in COLUMN_LABLES:
            print(f'Enter a number from 1 to {BOARD_WIDTH}.')
            continue

        column_index = int(response) - 1
        if board[(column_index, 0)] != EMPTY_SPACE:
            print('That column is full, select another one.')
            continue

        for row_index in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(column_index, row_index)] == EMPTY_SPACE:
                return (column_index, row_index)


def is_full(board):
    """"Возвращает True, если в 'board' нет пустых участков,
     в противном случае возвращает False."""

    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            if board[(column_index, row_index)] != EMPTY_SPACE:
                return False
    return True


def is_winner(player_tile, board):
    """"Возвращает True, если 'player_tile' содержит в одной строке
    на 'board' четыре элемента в ряд, иначе возвращает False."""

    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT):
            tile_1 = board[(column_index, row_index)]
            tile_2 = board[(column_index + 1, row_index)]
            tile_3 = board[(column_index + 2, row_index)]
            tile_4 = board[(column_index + 3, row_index)]
            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT - 3):
            tile_1 = board[(column_index, row_index)]
            tile_2 = board[(column_index, row_index + 1)]
            tile_3 = board[(column_index, row_index + 2)]
            tile_4 = board[(column_index, row_index + 3)]
            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT - 3):
            tile_1 = board[(column_index, row_index)]
            tile_2 = board[(column_index + 1, row_index + 1)]
            tile_3 = board[(column_index + 2, row_index + 2)]
            tile_4 = board[(column_index + 3, row_index + 3)]
            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True

            tile_1 = board[(column_index + 3, row_index)]
            tile_2 = board[(column_index + 2, row_index + 1)]
            tile_3 = board[(column_index + 1, row_index + 2)]
            tile_4 = board[(column_index, row_index + 3)]
            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True
    return False


if __name__ == '__main__':
    main()
