"""Последовательность Фибоначчи.
Вычисляет числа из последовательности Фибоначчи: 0, 1, 1, 2, 3, 5, 8, 13..."""

import sys

print('''Fibonacci Sequence.
         The Fibonacci sequence begins with 0 and 1, and the next number is the
         sum of previous two numbers. The sequence continues forever:
         0, 1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...''')

while True:
    while True:
        print('Enter the N-th Fibonacci number you wish to')
        print('calculate (such as 5, 50, 1000, 99999), or QUIT to quit.')
        response = input('> ').upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response.isdecimal() and int(response) > 0:
            nth = int(response)
            break
        print('Please enter a number greater than 0, or QUIT.')
    print()

    if nth == 1:
        print('0')
        print('The 1st Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0', '1')
        print('The 2nd Fibonacci number is 1.')
        continue

    if nth >= 10_000:
        print('WARNING: This will take a while to display on the')
        print('screen. If you want to quit this program before it is')
        print('done, press Ctrl-C.')
        input('Press Enter to begin...')

    second_to_last_number = 0
    last_number = 1
    fin_numbers_calculated = 2
    print('0, 1, ', end='')

    while True:
        next_number = second_to_last_number + last_number
        fin_numbers_calculated += 1

        print(next_number, end='')

        if fin_numbers_calculated == nth:
            print()
            print(f'The # {fin_numbers_calculated} Fibonacci '
                  f'number is {next_number}.')
            break
        print(', ', end='')

        second_to_last_number = last_number
        last_number = next_number
