"""Три карты Монте.
Найдите даму червей после перемешивания карт.
(В реальной жизни мошенник обычно прячет даму червей в руке, так что
вы никогда не выиграете.)"""

import random
import time


NUM_SWAPS = 16
DELAY = 0.8
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
LEFT = 0
MIDDLE = 1
RIGHT = 2


def display_cards(cards):
    """Отображает карты из списка cards (достоинство, масть)."""

    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rank, suit = card
        rows[0] += ' __   '
        rows[1] += '|{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    for i in range(5):
        print(rows[i])


def get_random_card():
    """Возвращает случайную карту - НЕ даму червей."""
    while True:
        rank = random.choice(list('23456789JQKA') + ['10'])
        suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])
        if rank != 'Q' and suit != HEARTS:
            return (rank, suit)


print('Three-Card Monte.\n')
print('Find the red lady (the Queen of Hearts)! Keep an eye on how')
print('the cards move.\n')

cards = [('Q', HEARTS), get_random_card(), get_random_card()]
random.shuffle(cards)
display_cards(cards)
input('Press Enter  when you ready to begin...')

for i in range(NUM_SWAPS):
    swap = random.choice(['l-m', 'm-r', 'l-r', 'm-l', 'r-m', 'r-l'])
    if swap == 'l-m':
        print('swapping left and middle...')
        cards[LEFT], cards[MIDDLE] = cards[MIDDLE], cards[LEFT]
    elif swap == 'm-r':
        print('swapping middle and right...')
        cards[MIDDLE], cards[RIGHT] = cards[RIGHT], cards[MIDDLE]
    elif swap == 'l-r':
        print('swapping left and right...')
        cards[LEFT], cards[RIGHT] = cards[RIGHT], cards[LEFT]
    elif swap == 'm-l':
        print('swapping middle and left...')
        cards[MIDDLE], cards[LEFT] = cards[LEFT], cards[MIDDLE]
    elif swap == 'r-m':
        print('swapping right and middle...')
        cards[RIGHT], cards[MIDDLE] = cards[MIDDLE], cards[RIGHT]
    elif swap == 'r-l':
        print('swapping right and left...')
        cards[RIGHT], cards[LEFT] = cards[LEFT], cards[RIGHT]
    time.sleep(DELAY)

print('\n' * 40)

while True:
    print('Which card has the Queen of Hearts? (LEFT MIDDLE RIGHT)')
    guess = input('> ')
    if guess in ['LEFT', 'MIDDLE', 'RIGHT']:
        if guess == 'LEFT':
            guess_index = 0
        elif guess == 'MIDDLE':
            guess_index = 1
        elif guess == 'RIGHT':
            guess_index = 2
        break

# Раскомментируйте этот код, чтобы игрок всегда проигрывал
'''if cards[guess_index] == ('Q', HEARTS):
    possible_new_index = [0, 1, 2]
    possible_new_index.remove(guess_index)
    new_index = random.choice(possible_new_index)
    cards[guess_index], cards[new_index] = cards[new_index], cards[guess_index]'''

display_cards(cards)

if cards[guess_index] == ('Q', HEARTS):
    print('You won!')
    print('Thanks for playing!')
else:
    print('You lost!')
    print('Thanks for playing, sucker!')
