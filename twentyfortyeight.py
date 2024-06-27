"""Игра "2048".
Игра, в которой при сдвиге "плиток" объединяются числа, растущие
в геометрической прогрессии. На основе игры "2048" Гарбриэле Чирули -
клона игра "1024" от Veewo Studios, которая является клоном игры Threes!"""

import random
import sys


BLANK = 0


def main():
    print('''Twenty Forty-Eight.
             Slide all the tiles on the board in one of four directions.
             Tiles with like numbers will combine into larger-numbered tiles.
             A new 2 tile is added to the board on each move. You win if
             you can create a 2048 tile. You lose if the board fills
             up the tiles before then.''')
    input('Press Enter to begin...')
    game_board = get_new_board()
    while True:
        draw_board(game_board)
        print('Score: ', get_score(game_board))
        player_move = ask_for_player_move()
        game_board = make_move(game_board, player_move)
        add_two_to_board(game_board)
        if is_full(game_board):
            draw_board(game_board)
            print('Game Over - Thanks for playing!')
            sys.exit()


def get_new_board():
    """Возвращает новую структуру данных для доски, которая
    предсталвяет собой ассоциативный массив, ключи которого -
    кортежи (x, y), а значения находятся в соответствующих клетках.
    Эти значения равны либо числам - степеням двойки, либо BLANK.
    Система координат выглядит так:
         X0 1 2 3
        Y+-+-+-+-+
        0| | | | |
         +-+-+-+-+
        1| | | | |
         +-+-+-+-+
        2| | | | |
         +-+-+-+-+
        3| | | | |
         +-+-+-+-+"""

    new_board = {}
    for x in range(4):
        for y in range(4):
            new_board[(x, y)] = BLANK

    starting_twos_placed = 0
    while starting_twos_placed < 2:
        random_space = (random.randint(0, 3), random.randint(0, 3))
        if new_board[random_space] == BLANK:
            new_board[random_space] = 2
            starting_twos_placed += 1
    return new_board


def draw_board(board):
    """"Отрисовываем структуру данных для доски на экране."""

    labels = []
    for y in range(4):
        for x in range(4):
            tile = board[(x, y)]
            label_for_this_tile = str(tile).center(5)
            labels.append(label_for_this_tile)
    print('''
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
          '''.format(*labels))


def get_score(board):
    """Возвращает сумму всех "плиток" в труктуре данных для доски."""

    score = 0
    for x in range(4):
        for y in range(4):
            if board[(x, y)] != BLANK:
                score += board[(x, y)]
    return score


def combine_tiles_in_column(column):
    """column представляет собой список из четырёх "плиток". Индекс 0
    соответсвует низу столбца column, а сила тяжести тянет "плитки" вниз,
    в случае равных значений они объединяются. Например,
    combine_tiles_in_column ([2, BLANK, 2, BLANK]) возвращает
    [4, BLANK, BLANK, BLANK]."""

    combined_tiles = []
    for i in range(4):
        if column[i] != BLANK:
            combined_tiles.append(column[i])
    while len(combined_tiles) < 4:
        combined_tiles.append(BLANK)

    for i in range(3):
        if combined_tiles[i] == combined_tiles[i + 1]:
            combined_tiles[i] *= 2
            for above_index in range(i + 1, 3):
                combined_tiles[above_index] = combined_tiles[above_index + 1]
            combined_tiles[3] = BLANK
    return combined_tiles


def ask_for_player_move():
    """Просим игрока указать направление следующего хода (или выйти).
    Проверяем ход на допустимость: 'W', 'A', 'S' или 'D'. """

    print('Enter move: (WASD or Q to quit.)')
    while True:
        move = input('> ').upper()
        if move == 'Q':
            print("Thanks for playing!")
            sys.exit()
        if move in ('W', 'A', 'S', 'D'):
            return move
        else:
            print("Enter one of 'W', 'A', 'S', 'D or 'Q'.")


def make_move(board, move):
    """Производит ход на доске.
    Аргумент move - 'W', 'A', 'S' или 'D'. Функция возвращает
    получившуюся структуру данных для доски (board)."""

    if move == 'W':
        all_column_spaces = [[(0, 0), (0, 1), (0, 2), (0, 3)],
                             [(1, 0), (1, 1), (1, 2), (1, 3)],
                             [(2, 0), (2, 1), (2, 2), (2, 3)],
                             [(3, 0), (3, 1), (3, 2), (3, 3)]]
    elif move == 'A':
        all_column_spaces = [[(0, 0), (1, 0), (2, 0), (3, 0)],
                             [(0, 1), (1, 1), (2, 1), (3, 1)],
                             [(0, 2), (1, 2), (2, 2), (3, 2)],
                             [(0, 3), (1, 3), (2, 3), (3, 3)]]
    elif move == 'S':
        all_column_spaces = [[(0, 3), (0, 2), (0, 1), (0, 0)],
                             [(1, 3), (1, 2), (1, 1), (1, 0)],
                             [(2, 3), (2, 2), (2, 1), (2, 0)],
                             [(3, 3), (3, 2), (3, 1), (3, 0)]]
    elif move == 'D':
        all_column_spaces = [[(3, 0), (2, 0), (1, 0), (0, 0)],
                             [(3, 1), (2, 1), (1, 1), (0, 1)],
                             [(3, 2), (2, 2), (1, 2), (0, 2)],
                             [(3, 3), (2, 3), (1, 3), (0, 3)]]

    board_after_move = {}
    for column_spaces in all_column_spaces:
        first_tile_space = column_spaces[0]
        second_tile_space = column_spaces[1]
        third_tile_space = column_spaces[2]
        fourth_tile_space = column_spaces[3]

        first_tile = board[first_tile_space]
        second_tile = board[second_tile_space]
        third_tile = board[third_tile_space]
        fourth_tile = board[fourth_tile_space]

        column = [first_tile, second_tile, third_tile, fourth_tile]
        combine_tiles_column = combine_tiles_in_column(column)

        board_after_move[first_tile_space] = combine_tiles_column[0]
        board_after_move[second_tile_space] = combine_tiles_column[1]
        board_after_move[third_tile_space] = combine_tiles_column[2]
        board_after_move[fourth_tile_space] = combine_tiles_column[3]
    return board_after_move


def add_two_to_board(board):
    """Добавляет на доску две случайные новые "плитки"."""

    while True:
        random_space = (random.randint(0, 3), random.randint(0, 3))
        if board[random_space] == BLANK:
            board[random_space] = 2
            return


def is_full(board):
    """Возвразает True, если в труктуре данных для доски нет пустых клеток."""

    for x in range(4):
        for y in range(4):
            if board[(x, y)] == BLANK:
                return False
    return True


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
