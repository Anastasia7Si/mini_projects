"""Царская игра Ура.
Игра 5000-летней давности из Месопотамии. Два игрока бьют фишки
друг друга, стремясь достичь финиша."""

import random
import sys


X_PLAYER = 'X'
O_PLAYER = 'O'
EMPTY = ' '
X_HOME = 'x_home'
O_HOME = 'o_home'
X_GOAL = 'x_goal'
O_GOAL = 'o_goal'
ALL_SPACES = 'hgfetsijklmnopdcbarq'
X_TRACK = 'HefghijklmnopstG'
O_TRACK = 'HabcdijklmnopqrG'
FLOWER_SPACES = ('h', 't', 'l', 'd', 'r')
BOARD_TEMPLATE = """
                       {}           {}
                       Home              Goal
                         v                 ^
    +-----+-----+-----+--v--+           +--^--+-----+
    |*****|     |     |     |           |*****|     |
    |* {} *<  {}  <  {}  <  {}            | |* {} *<  {} |
    |****h|    g|    f|    e|           |****t|    s|
    +--v--+-----+-----+-----+-----+-----+-----+--^--+
    |     |     |     |*****|     |     |     |     |
    |  {}  >  {}  >  {}  >* {} *> {}   >   {} >  {}  > {}  |
    |    i|    j|    k|****l|    m|    n|    o|    p|
    +--^--+-----+-----+-----+-----+-----+-----+--v--+
    |*****|     |     |     |           |*****|     |
    |* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
    |****d|    c|    b|    a|           |****r|    q|
    +-----+-----+-----+--^--+           +--v--+-----+
                         ^                 v
                       Home              Goal
                       {}           {}
"""


def main():
    print('''The Royal Game of Ur.
             This is a 5000 year old game. Two players must their tokens
             from their home to their goal. On your turn you flip four coins
             and can move one token a number of spaces equal to the heads you
             got.
             Ur is a racing game; the first player to move all seven of their
             tokens to their goal wins. To do this, tokens travel from their
             home to their goal:
                          X Home      X Goal
                            v           ^
              +---+---+---+-v-+       +-^-+---+
              |v<<<<<<<<<<<<< |       | ^<|<< |
              |v  |   |   |   |       |   | ^ |
              +v--+---+---+---+---+---+---+-^-+
              |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>^ |
              |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>v |
              +^--+---+---+---+---+---+---+-v-+
              |^  |   |   |   |       |   | v |
              |^<<<<<<<<<<<<< |       | v<<<< |
              +---+---+---+-^-+       +-v-+---+
                            ^           v
                          O Home      O Goal
             If you land on an opponent's token in the mibble track, it gets
             sent back home. The **flower** spaces let you take another turn.
             Tokens in the middle flower space are safe and cannot be landed
             on.''')
    input('Press Enter to begin...')
    game_board = get_new_board()
    turn = O_PLAYER
    while True:
        if turn == X_PLAYER:
            opponent = O_PLAYER
            home = X_HOME
            track = X_TRACK
            goal = X_GOAL
            opponent_home = O_HOME
        elif turn == O_PLAYER:
            opponent = X_PLAYER
            home = O_HOME
            track = O_TRACK
            goal = O_GOAL
            opponent_home = X_HOME
        display_board(game_board)
        input(f'It is {turn}\'s turn. Press Enter to flip...')
        flip_tally = 0
        print('Flips: ', end='')
        for i in range(4):
            result = random.randint(0, 1)
            if result == 0:
                print('T', end='')
            else:
                print('H', end='')
            if i != 3:
                print('-', end='')
            flip_tally += result
        print('  ', end='')

        if flip_tally == 0:
            input('You lose a turn. Press Enter to continue...')
            turn = opponent
            continue

        valid_moves = get_valid_moves(game_board, turn, flip_tally)
        if valid_moves == []:
            print('There are no possible moves, so you lose a turn.')
            input('Press Enter to continue...')
            turn = opponent
            continue

        while True:
            print(f'Select move {flip_tally} spaces: ', end='')
            print(' '.join(valid_moves) + ' quit')
            move = input('> ').lower()
            if move == 'quit':
                print('Thanks for playing!')
                sys.exit()
            if move in valid_moves:
                break
            print('That is not a valid move.')

        if move == 'home':
            game_board[home] -= 1
            next_track_space_index = flip_tally
        else:
            game_board[move] = EMPTY
            next_track_space_index = track.index(move) + flip_tally

        moving_onto_goal = next_track_space_index == len(track) - 1
        if moving_onto_goal:
            game_board[goal] += 1
            if game_board[goal] == 7:
                display_board(game_board)
                print(f'{turn} has won the game!')
                print('Thanks for playing!')
                sys.exit()
        else:
            next_board_space = track[next_track_space_index]
            if game_board[next_board_space] == opponent:
                game_board[opponent_home] += 1
            game_board[next_board_space] = turn

        if next_board_space in FLOWER_SPACES:
            print(f'{turn} landed on a flower space and goes agian.')
            input('Press Enter to continue...')
        else:
            turn = opponent


def get_new_board():
    """Возвращает ассоциативный массив, отражающий состояние доски.
    Ключами служат строковые значения меток клетов, значения -
    X_PLAYER, O_PLAYER или EMPTY. Также сожержит счетчики количества
    фишек в доме и на финише для обоих игроков."""

    board = {X_HOME: 7, X_GOAL: 0, O_HOME: 7, O_GOAL: 0}
    for space_label in ALL_SPACES:
        board[space_label] = EMPTY
    return board


def display_board(board):
    """Отображает игральную доску на экране."""

    print('\n' * 60)
    x_home_tokens = ('X' * board[X_HOME]).ljust(7, '.')
    o_home_tokens = ('O' * board[O_HOME]).ljust(7, '.')
    x_goal_tokens = ('X' * board[X_GOAL]).ljust(7, '.')
    o_goal_tokens = ('O' * board[O_GOAL]).ljust(7, '.')

    spaces = []
    spaces.append(x_home_tokens)
    spaces.append(x_goal_tokens)
    for space_label in ALL_SPACES:
        spaces.append(board[space_label])
    spaces.append(o_home_tokens)
    spaces.append(o_goal_tokens)
    print(BOARD_TEMPLATE.format(*spaces))


def get_valid_moves(board, player, flip_tally):
    """Проверяет доступные к соевршению ходы."""

    valid_moves = []
    if player == X_PLAYER:
        opponent = O_PLAYER
        track = X_TRACK
        home = X_HOME
    elif player == O_PLAYER:
        opponent = X_PLAYER
        track = O_TRACK
        home = O_HOME

    if board[home] > 0 and board[track[flip_tally]] == EMPTY:
        valid_moves.append('home')

    for track_space_index, space in enumerate(track):
        if space in ('H', 'G') or board[space] != player:
            continue
        next_track_space_index = track_space_index + flip_tally
        if next_track_space_index >= len(track):
            continue
        else:
            next_board_space_key = track[next_track_space_index]
            if next_board_space_key == 'G':
                valid_moves.append(space)
                continue
        if board[next_board_space_key] in (EMPTY, opponent):
            if next_board_space_key == '1' and board['1'] == opponent:
                continue
            valid_moves.append(space)
    return valid_moves


if __name__ == '__main__':
    main()
