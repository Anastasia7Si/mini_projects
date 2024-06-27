"""Головоломка с вёдрами воды.
Головоломка с переливанием воды."""

import sys


print('Water Bucket Puzzle.')

GOAL = 4
steps = 0
water_in_bucket = {'8': 0, '5': 0, '3': 0}

while True:
    print(f'\nTry to get {GOAL}L water into one of theese buckets: ')

    water_display = []
    for i in range(1, 9):
        if water_in_bucket['8'] < i:
            water_display.append('     ')
        else:
            water_display.append('WWWWW')
    for i in range(1, 6):
        if water_in_bucket['5'] < i:
            water_display.append('     ')
        else:
            water_display.append('WWWWW')
    for i in range(1, 4):
        if water_in_bucket['3'] < i:
            water_display.append('     ')
        else:
            water_display.append('WWWWW')
    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8L         5L         3L'''.format(*water_display))

    for water_amount in water_in_bucket.values():
        if water_amount == GOAL:
            print(f'Good job! You Solved it in {steps} steps!')
            sys.exit()

    print('You can:')
    print('  (F)ill the bucket.')
    print('  (E)mpty the bucket.')
    print('  (P)our one bucket into another.')
    print('  (Q)uit.')
    while True:
        move = input('> ').upper()
        if move in ('QUIT', 'Q'):
            print('Thanks for playing!')
            sys.exit()
        if move in ('F', 'E', 'P'):
            break
        print('Enter F, E, P or Q.')

    while True:
        print('Select a bucket 8, 5, 3, or QUIT.')
        src_bucket = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if src_bucket in ('8', '5', '3'):
            break

    if move == 'F':
        src_bucket_size = int(src_bucket)
        water_in_bucket[src_bucket] = src_bucket_size
        steps += 1
    elif move == 'E':

        water_in_bucket[src_bucket] = 0
        steps += 1
    elif move == 'P':
        while True:
            print('Select a bucket to pour into: 8, 5, or 3.')
            dst_bucket = input('> ').upper()
            if dst_bucket in ('8', '5', '3'):
                break
        dst_bucket_size = int(dst_bucket)
        empty_space_in_dst_bucket = (
            dst_bucket_size - water_in_bucket[dst_bucket]
            )
        water_in_src_bucket = water_in_bucket[src_bucket]
        amount_to_pour = min(empty_space_in_dst_bucket, water_in_src_bucket)
        water_in_bucket[src_bucket] -= amount_to_pour
        water_in_bucket[dst_bucket] += amount_to_pour
        steps += 1
    elif move == 'C':
        pass
