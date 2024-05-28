"""Магический хруастальный шар.
Задвайте вопросы типа да/нет о своём будущем."""

import random
import time


def slow_space_print(text, interval=0.1):
    """Медленно выводит текст с пробелами между буквами и буквами i
    в нижнем регистре."""
    for character in text:
        if character == 'I':
            print('i ', end='', flush=True)
        else:
            print(character + ' ', end='', flush=True)
        time.sleep(interval)
    print()
    print()


slow_space_print('MAGIC FORTUNE BALL.')
input('> ')
replies = [
    'LET ME THINK ON THIS...',
    'AN INTERESTING QUESTION...',
    'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
    'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?',
    'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
    'YES... NO... MAYBE... I WILL THINK ON IT...',
    'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...',
    'I SHALL CONSULT MY VISIONS...',
    'YOU MAY WANT TO SIT DOWN FOR THIS...',
]
slow_space_print(random.choice(replies))
slow_space_print('.' * random.randint(4, 12), 0.7)
slow_space_print('I HAVE AN ANSWER...', 0.2)
time.sleep(1)
answers = [
    'YES, FOR SURE',
    'MY ANSWER IS NO',
    'ASK ME LATER',
    'I AM PROGRAMMED TO SAY YES',
    'THE STARS SAY YES, BUT I SAY NO',
    'I DUNNO MAYBE',
    'FOCUS AND ASK ONCE MORE',
    'DOUBTFUL, VERY DOUBTFUL',
    'AFFIRMATIVE',
    'YES, THOUGH YOU MAY NOT LIKE IT',
    'NO, BUT YOU MAY WISH IT WAS SO',
]
slow_space_print(random.choice(answers), 0.05)
