"""Быстрый стрелок.
Проверьте свои рефлексы и узнайте,

самый ли вы быстрый стрелок на Диком Западе."""

import random
import sys
import time

print('Fast Draw.')
print()
print('Time to tast your raflexes and see if you are the fastest.')
print('draw in the west!')
print('When you see "DRAW", you have 0.3 seconds to press Enter.')
print('But you lise if you press Enter before "DRAW" appears.')
print()
input('Press Enter to begin...')

while True:
    print()
    print('It is high noon...')
    time.sleep(random.randint(20, 50) / 10.0)
    print('DRAW!')
    draw_time = time.time()
    input()
    time_elapsed = time.time() - draw_time

    if time_elapsed < 0.01:
        print('You drew before "DRAW" appeared! You lose.')
    elif time_elapsed > 0.3:
        time_elapsed = round(time_elapsed, 4)
        print(f'You took {time_elapsed} seconds to draw. Too slow!')
    else:
        time_elapsed = round(time_elapsed, 4)
        print(f'You took {time_elapsed} seconds to draw.')
        print('You are the fastest draw in the west! Yiu win!')

    print('Enter QUIT to stop, or press Enter to play again.')
    response = input('> ').upper()
    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
