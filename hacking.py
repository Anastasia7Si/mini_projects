"""Мини-игра со взломом.
Мини-игра со взломом из Fallout 3. Найдите семибуквенное слово-пароль
с помощью подсказок, возвращаемых при каждой попытке угадать его."""

import random
import sys


GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?'

with open('seven_letters_words.txt') as word_list_file:
    WORDS = word_list_file.readlines()
for i in range(len(WORDS)):
    WORDS[i] = WORDS[i].strip().upper()


def main():
    """Запуск игры со взломом."""
    print('''Hacking Minigame.
             Find the password in the computers's memory. You are given clues
             after each guess. For example, if the secret password is MONITOR
             but the player guessed CONTAIN, they are given the hint that
             2 out of 7 letters were correct, becouse both MONITOR and CONTAIN
             have a letter O and N as their 2nd and 3rd letter.
             You get four guesses.\n''')
    input('Press Enter to begin...')
    game_words = get_words()
    computer_mamory = get_computer_memory_str(game_words)
    secret_password = random.choice(game_words)

    print(computer_mamory)
    for tries_remaining in range(4, 0, -1):
        player_move = ask_for_player_guess(game_words, tries_remaining)
        if player_move == secret_password:
            print('A C C E S S  G R A N T E D')
            return
        else:
            num_matches = num_matching_letters(secret_password, player_move)
            print(f'Access Denied ({num_matches}/7 correct).')
    print(f'Out of tries. Secret password was {secret_password}.')


def get_words():
    """Возвращает список из 12-ти слов - возможных паролей."""

    secret_password = random.choice(WORDS)
    words = [secret_password]
    while len(words) < 3:
        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 0:
            words.append(random_word)

    for i in range(500):
        if len(words) == 5:
            break

        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 3:
            words.append(random_word)

    for i in range(500):
        if len(words) == 12:
            break

        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) != 0:
            words.append(random_word)

    while len(words) < 12:
        random_word = get_one_word_except(words)
        words.append(random_word)

    assert len(words) == 12
    return words


def get_one_word_except(block_list=None):
    """Возвращает случайное слово из списка WORDS, не входящее в block_list."""

    if block_list is None:
        block_list = []

    while True:
        random_word = random.choice(WORDS)
        if random_word not in block_list:
            return random_word


def num_matching_letters(word_1, word_2):
    """Возвращает число совпадающих букв в указанных двух словах."""

    matches = 0
    for i in range(len(word_1)):
        if word_1[i] == word_2[i]:
            matches += 1
    return matches


def get_computer_memory_str(words):
    """Возвращает строковое значение, соответствующее "памяти компьютера"."""

    lines_with_words = random.sample(range(16 * 2), len(words))
    memory_adress = 16 * random.randint(0, 4000)
    computer_memory = []
    next_word = 0
    for line_num in range(16):
        left_half = ''
        right_half = ''
        for j in range(16):
            left_half += random.choice(GARBAGE_CHARS)
            right_half += random.choice(GARBAGE_CHARS)
        if line_num in lines_with_words:
            insertion_index = random.randint(0, 9)
            left_half = (left_half[:insertion_index] + words[next_word]
                         + left_half[insertion_index + 7:])
            next_word += 1
        if line_num + 16 in lines_with_words:
            insertion_index = random.randint(0, 9)
            right_half = (right_half[:insertion_index] + words[next_word]
                          + right_half[insertion_index + 7:])
            next_word += 1

        computer_memory.append(
            '0x' + hex(memory_adress)[2:].zfill(4)
            + '  ' + left_half + '    '
            + '0x' + hex(memory_adress + (16*16))[2:].zfill(4)
            + '  ' + right_half)

        memory_adress += 16
    return '\n'.join(computer_memory)


def ask_for_player_guess(words, tries):
    """Ввод пользователем догадки."""

    while True:
        print(f'Enter password: ({tries} tries remaining).')
        guess = input('> ')
        if guess in words:
            return guess
        print('That is not one of the possible password listad above.')
        print(f'Try entering "{words[0]} or "{words[1]}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
