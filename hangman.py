"""Виселица.
Угадайте буквы загаданного слова, пока не будет нарисована виселица."""

import random
import sys


HANGMAN_PICS = [
 r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
 r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
 r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
 r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
 r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
 r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
 r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

CATEGORY = 'Animals'
WORDS = '''ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR
           COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE
           HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER
           OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON
           SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD
           TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'''.split()


def main():
    print('Hagman.')
    missed_letters = []
    correct_lettrs = []
    secret_word = random.choice(WORDS)

    while True:
        draw_hangman(missed_letters, correct_lettrs, secret_word)
        guess = get_player_guess(missed_letters + correct_lettrs)
        if guess in secret_word:
            correct_lettrs.append(guess)
            found_all_letters = True
            for secret_word_letter in secret_word:
                if secret_word_letter not in correct_lettrs:
                    found_all_letters = False
                    break
            if found_all_letters:
                print('Yes! The secret word is: ', secret_word)
                print('You have won!')
                break
        else:
            missed_letters.append(guess)
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                draw_hangman(missed_letters, correct_lettrs, secret_word)
                print('You have run out of guesses!')
                print('The word wos:', secret_word)
                break


def draw_hangman(missed_letters, correct_lettrs, secret_word):
    """Рисуем текущее состояние виселицы вместе с неугаданными
    и правильно угаданными буквами заданного слова."""
    print(HANGMAN_PICS[len(missed_letters)])
    print('The category is: ', CATEGORY)
    print()
    print('Missed latters: ', end='')
    for letter in missed_letters:
        print(letter, end='')
    if len(missed_letters) == 0:
        print('No missed letters yet.')
    print()

    blanks = ['_'] * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_lettrs:
            blanks[i] = secret_word[i]
    print(' '.join(blanks))


def get_player_guess(already_guessed):
    """Возвращает введенную пользователем букву. Убеждается,
    что пользователь ввел одну букву, которую не вводил ранее."""
    while True:
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Chose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
