"""Радуга.
Отображает простое динамическое изображение радуги.
Нажмите Ctrl-C для остановки."""

import time
import sys


try:
    import bext
except ImportError:
    print('This program requires the bext mobule, which you')
    print('can install with command "pip install Bext".')
    sys.exit()

print('Rainbow.')
print('Press Ctrl+C to stop.')
time.sleep(3)

indent = 0
indent_increasing = True

try:
    while True:
        print(' ' * indent, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##')

        if indent_increasing:
            indent += 1
            if indent == 60:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
        time.sleep(0.02)
except KeyboardInterrupt:
    sys.exit()
