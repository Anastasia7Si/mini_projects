"""Девяносто девять бутылок молока на стене.
Выводит полный текст одной из самых длинных песен на свете!
Нажмите Ctrl-C для остановки."""

import sys
import time

print('Ninety-Nine Bottles.')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99
PAUSE = 2

try:
    while bottles > 1:
        print(bottles, ' bottles of milk on the wall,')
        time.sleep(PAUSE)
        print(bottles, ' bottles of milk,')
        time.sleep(PAUSE)
        print('Take one down, pass it around, ')
        time.sleep(PAUSE)
        bottles = bottles - 1
        print(bottles, ' bottles of milk on the wall!')
        time.sleep(PAUSE)
        print()
    print('1 bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of milk,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of milk on the wall!')
except KeyboardInterrupt:
    sys.exit()
