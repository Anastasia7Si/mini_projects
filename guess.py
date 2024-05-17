"""Угадай число.
Угадайте загаданное число по подсказкам."""

import random


def ask_for_guess():
    while True:
        guess = input('> ')

        if guess.isdecimal():
            return int(guess)
        print('Please inter a number between 1 and 100.')


print('Guess the Number.')
print()
secret_number = random.randint(1, 100)
print('I thinking of a number between 1 and 100.')

for i in range(10):
    print(f'You have {10 - i} guesses left take a guess.')

    guess = ask_for_guess()
    if guess == secret_number:
        break

    if guess < secret_number:
        print('Your guess is too low.')
    if guess > secret_number:
        print('Your guess is too high.')

if guess == secret_number:
    print('Yay! You guessed my number!')
else:
    print('Game over. The number I was thinling af was ', secret_number)
