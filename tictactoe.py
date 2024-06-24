"""Крестики-нолики.
Классическая настольная игра."""

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '


def main():
    print('Welcome to Tic-Tac-Toe!')
    game_board = get_blank_board()
    current_player, next_player = X, O
    while True:
        print(get_board_str(game_board))
        move = None
        while not is_valid_space(game_board, move):
            print(f'What is {current_player}\'s move? (1-9)')
            move = input('> ')
        update_board(game_board, move, current_player)
        if is_winner(game_board, current_player):
            print(get_board_str(game_board))
            print(f'{current_player} has won the game!')
            break
        elif is_board_full(game_board):
            print(get_board_str(game_board))
            print('The game is a tie!')
            break
        current_player, next_player = next_player, current_player
    print('Thanks for playing!')


def get_blank_board():
    """Создаём новую пустую доску для крестиков-ноликов."""

    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board


def get_board_str(board):
    """Возвращает текстовое представление доски."""

    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'],
                                board['4'], board['5'], board['6'],
                                board['7'], board['8'], board['9'])


def is_valid_space(board, space):
    """Возвращает True, если space на board представляет собой
    допустимый номер клеткиб причём эта клетка пуста."""

    return space in ALL_SPACES and board[space] == BLANK


def update_board(board, space, mark):
    """Присваеваем клетке(space) на доске(board) значение(mark)."""

    board[space] = mark


def is_winner(board, player):
    """Возвращает True, если игрок player победил на этой доске."""

    b, p = board, player
    return ((b['1'] == b['2'] == b['3'] == p) or
            (b['4'] == b['5'] == b['6'] == p) or
            (b['7'] == b['8'] == b['9'] == p) or
            (b['1'] == b['4'] == b['7'] == p) or
            (b['2'] == b['5'] == b['8'] == p) or
            (b['3'] == b['6'] == b['9'] == p) or
            (b['3'] == b['5'] == b['7'] == p) or
            (b['1'] == b['5'] == b['9'] == p))


def is_board_full(board):
    """Возвращает True, если все клетки на доске заполнены."""

    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True


if __name__ == '__main__':
    main()
