"""Повторение музыки.
Игра с подбором звуковых соответствий. Попробуйте запомнить
всё возврастающую последовательность букв. Создана под впечатлением
от электронной игры "Саймон"."""

import random
import sys
import time


try:
    import playsound
except ImportError:
    print('The playsound module needs to be installed to run this')
    print('program. On Windows, open a command prompt and run:')
    print('pip install playsound.')
    print('On macOS and Linux, open a terminal and run:')
    print('pip3 install playsound.')
    sys.exit()


print('''Soubd Mimic.
         Try to memorize a pattern of A S D F letters (each with
         its own sound) as it gets longer and longer...''')
input('Press Enter to begin...')

pattern = ''
while True:
    print('\n' * 60)
    pattern += random.choice('ASDF')
    print('Pattern: ', end='')
    for letter in pattern:
        print(letter, end=' ', flush=True)
        playsound.playsound('sound' + letter + '.wav')
    time.sleep(1)
    print('\n' * 60)
    print('Enter the pattern:')
    response = input('> ').upper()
    if response != pattern:
        print('Incorrect!')
        print(f'The pattern wos: {pattern}')
    else:
        print('Correct!')
    for letter in pattern:
        playsound.playsound('sound' + letter + '.wav')
    if response != pattern:
        print(f'You scored {len(pattern) - 1} points.')
        print('Thanks for playing!')
        sys.exit()
    time.sleep(1)
