"""Гипотеза Коллатца.
Генерирует члены последовательности Коллатца по заданному начальному числу."""

import sys

print('''Collatz Sequence, or, the 3n + 1 Problem.
         The Collatz sequence is a sequence of numbers producted from a
         starting number n, following three rules:

         1) If n is even, the next number n is n / 2.
         2)If n is odd, the next number n if n * 3 + 1.
         3)If n is 1, stop. Otherwise, repeat.
         It is generally throught, but so far not mathematically proven, that
         every starting number eventually terminates at 1.''')

print('Enter a starting number (greater than 0) os QUIT.')
response = input('> ')

if not response.isdecimal() or response == '0':
    print('You must enter na integer greater than 0.')
    sys.exit()

number = int(response)
print(number, end='\n', flush=True)

result = []
while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    result.append(number)

print(result)
print(len(result))
