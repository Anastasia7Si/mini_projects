"""Моделирование статистики за миллион бросков костей.
Моделирование миллиона бросков игральных костей."""

import random
import time

print('''Million Dice Roll Statistics Simulator.
         Enter how many six-sided dice you want to roll.''')
number_of_dice = int(input('> '))
results = {}
for i in range(number_of_dice, (number_of_dice * 6) + 1):
    results[i] = 0

print(f'Simulating 1 000 000 rolls of {number_of_dice} dice...')
last_print_time = time.time()
for i in range(1_000_000):
    if time.time() > last_print_time + 1:
        print(f'{round(i / 10_000, 1)}% done...')
        last_print_time = time.time()
    total = 0
    for j in range(number_of_dice):
        total += random.randint(1, 6)
    results[total] += 1

print('TOTAL - ROLLS - PERCENTAGE')
for i in range(number_of_dice, (number_of_dice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10_000, 1)
    print(f'  {i} - {roll} rolls - {percentage}%')
