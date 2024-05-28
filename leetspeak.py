"""Leet.
Переводит сообщения на английском зяыке в l33t."""

import random


try:
    import pyperclip
except ImportError:
    pass


def main():
    print('''L3375P34< (leetspeak)
             Enter your message: ''')
    english = input('> ')
    leetspeak = english_to_leetspeak(english)
    print(leetspeak)

    try:
        pyperclip.copy(leetspeak)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass


def english_to_leetspeak(message):
    """Преобразует строковое значение на английском языке из message
    в leetspeak."""

    char_mapping = {
        'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
        'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
        'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
        'v': ['\\/']
        }
    leetspeak = ''
    for char in message:
        if char.lower() in char_mapping and random.random() <= 0.70:
            possible_lett_replacements = char_mapping[char.lower()]
            leet_replacement = random.choice(possible_lett_replacements)
            leetspeak = leetspeak + leet_replacement
        else:
            leetspeak = leetspeak + char
    return leetspeak


if __name__ == '__main__':
    main()
