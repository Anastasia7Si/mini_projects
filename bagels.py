"""Бейглз. Дедуктивная логическая игра на угадывание числа по подсказкам."""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Bagels, a deductive logic game.
          I am thinking of a {} - digit number with no repeated digits.
          Try to guess what it is. Here some clues:
          When I say:   That means:
            Pico        One digit is correct but in the wrong position.
            Fermi       One digit is correct and in the right position.
            Bagels      No digit is correct.
          For example, if the secret number was 248 and your guess was 843, the
          clues would be Farmi Pico'''.format(MAX_GUESSES))

    while True:
        secret_number = get_secret_number()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        number_guesses = 1
        while number_guesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(number_guesses))
                guess = input('> ')

            clues = get_clues(guess, secret_number)
            print(clues)
            number_guesses += 1

            if guess == secret_number:
                break
            if number_guesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secret_number))

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing! <3')


def get_secret_number():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""

    numbers = list('0123456789')
    random.shuffle(numbers)

    secret_number = ''
    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    return secret_number


def get_clues(guess, secret_number):
    """ВОзвращает строку с подсказками Pico, Fermi, Bagels
    для полученной на входе пары из догадки и секретного числа."""

    if guess == secret_number:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()
