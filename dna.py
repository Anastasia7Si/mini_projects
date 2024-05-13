"""ДНК.
Просто динамическое изображение двойной спирали ДНК.
Нажмите Ctrl+C для остановки."""

import random
import sys
import time

PAUSE = 0.15
ROWS = [
    '           ##',
    '          #{}-{}#',
    '         #{}---{}#',
    '        #{}-----{}#',
    '       #{}------{}#',
    '      #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '       #{}-{}#',
    '        ##',
    '        #{}-{}#',
    '        #{}---{}#',
    '       #{}-----{}#',
    '       #{}------{}#',
    '        #{}------{}#',
    '         #{}-----{}#',
    '          #{}---{}#',
    '           #{}-{}#']

try:
    print('DNA Animation.')
    print('Press Ctrl-C to quit.')
    time.sleep(2)
    row_index = 0

    while True:
        row_index = row_index + 1
        if row_index == len(ROWS):
            row_index = 0

        if row_index == 0 or row_index == 9:
            print(ROWS[row_index])
            continue

        random_selection = random.randint(1, 4)
        if random_selection == 1:
            left_nucleotide, right_nucleotide = 'A', 'T'
        elif random_selection == 2:
            left_nucleotide, right_nucleotide = 'T', 'A'
        elif random_selection == 3:
            left_nucleotide, right_nucleotide = 'C', 'G'
        elif random_selection == 4:
            left_nucleotide, right_nucleotide = 'G', 'C'

        print(ROWS[row_index].format(left_nucleotide, right_nucleotide))
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
