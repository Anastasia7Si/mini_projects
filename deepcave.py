"""Глубокая пещера.
Динамическое изображение глубокой пещеры, ведущей до самого центра Земли."""

import random
import sys
import time

WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Deep Cave.')
print('Press Ctrl-C to stop.')
time.sleep(2)

left_wigth = 20
gap_width = 10

while True:
    right_wigth = WIDTH - gap_width - left_wigth
    print(('#' * left_wigth) + (' ' * gap_width) + ('#' * right_wigth))

    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    dice_roll = random.randint(1, 6)
    if dice_roll == 1 and left_wigth > 1:
        left_wigth = left_wigth - 1
    elif dice_roll == 2 and (left_wigth + gap_width) < (WIDTH - 1):
        left_wigth = left_wigth + 1
    else:
        pass

    dice_roll = random.randint(1, 6)
    if dice_roll == 1 and gap_width > 1:
        gap_width = gap_width - 1
    elif dice_roll == 2 and (left_wigth + gap_width) < (WIDTH - 1):
        gap_width = gap_width + 1
    else:
        pass
