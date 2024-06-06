"""Бега улиток.
Бега быстроногих улиток!"""

import random
import time
import sys


MAX_NUMBER_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40

print('''Snail Race.
         @v <-- snail''')
while True:
    print(f'How any sails will race? Max: {MAX_NUMBER_SNAILS}.')
    response = input('> ')
    if response.isdecimal():
        number_snails_racing = int(response)
        if 1 < number_snails_racing <= MAX_NUMBER_SNAILS:
            break
    print(f'Enter a number between 2 and {MAX_NUMBER_SNAILS}.')

snail_names = []
for i in range(1, number_snails_racing + 1):
    while True:
        print(f'Enter sanil #{str(i)}\'s name:')
        name = input('> ')
        if len(name) == 0:
            print('Please enter a name.')
        elif name in snail_names:
            print('Choose a name that has not already been used.')
        else:
            break
    snail_names.append(name)

print('\n' * 40)
len_road = ' ' * (FINISH_LINE - len('START'))
finish_line = ' ' * (FINISH_LINE - len('|'))
print(f'START{len_road}FINISH')
print(f'|{finish_line}|')
snail_progress = {}
for snail_name in snail_names:
    print(snail_name[:MAX_NAME_LENGTH])
    print('@v')
    snail_progress[snail_name] = 0
time.sleep(1.5)

while True:
    for i in range(random.randint(1, number_snails_racing // 2)):
        random_snail_name = random.choice(snail_names)
        snail_progress[random_snail_name] += 1
        if snail_progress[random_snail_name] == FINISH_LINE:
            print(random_snail_name, 'has won!')
            sys.exit()
    time.sleep(0.5)
    print('\n' * 40)
    print(f'START{len_road}FINISH')
    print(f'|{finish_line}|')
    for snail_name in snail_names:
        spaces = snail_progress[snail_name]
        print((' ' * spaces) + snail_name[:MAX_NAME_LENGTH])
        print(('.' * snail_progress[snail_name] + '@v'))
