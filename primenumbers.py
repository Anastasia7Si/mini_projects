"""Простые числа.
Вычисляет простые числа - числа, делящиеся нацело только на единицу
и на себя самое. Они применются на практике во множестве сфер."""

import math
import sys


def main():
    print('''Prime Numbers.
             Prime numbers are numbers that are only evenly divisible by
             one and themselves. They are used in a variety of prectical
             applications, but cannot be predicted. They must be
             calculated one at a time.\n''')
    while True:
        print('''Enter a number to start searching for primes from:
                 (Try 0 or 1_000_000_000_000 (12 zeros) or another number.)''')
        response = input('> ')
        if response.isdecimal():
            number = int(response)
            break
    input('Press Ctrl-C at any time to quit. Press Enter to begin...')
    while True:
        if is_prime(number):
            print(str(number) + ', ', end='', flush=True)
        number += 1


def is_prime(number):
    """Возвращает True, если число простое, в противном случае - False."""

    if number < 2:
        return False
    elif number == 2:
        return True

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
