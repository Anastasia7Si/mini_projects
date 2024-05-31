"""Проблема Монти Холла.
Моделирование задачи телевизионной игры Монти Холла."""

import random
import sys


ALL_CLOSED = """
+------+ +------+ +------+
|      | |      | |      |
|   1  | |   2  | |   3  |
|      | |      | |      |
|      | |      | |      |
|      | |      | |      |
+------+ +------+ +------+"""
FIRST_GOAT = """
+------+ +------+ +------+
|  ((  | |      | |      |
|  oo  | |   2  | |   3  |
| /_/|_| |      | |      |
|    | | |      | |      |
|GOAT||| |      | |      |
+------+ +------+ +------+"""
SECOND_GOAT = """
+------+ +------+ +------+
|      | |  ((  | |      |
|   1  | |  oo  | |   3  |
|      | | /_/|_| |      |
|      | |    | | |      |
|      | |GOAT||| |      |
+------+ +------+ +------+"""
THIRD_GOAT = """
+------+ +------+ +------+
|      | |      | |  ((  |
|   1  | |   2  | |  oo  |
|      | |      | | /_/|_|
|      | |      | |    | |
|      | |      | |GOAT|||
+------+ +------+ +------+"""
FIRST_CAR_OTHERS_GOAT = """
+------+ +------+ +------+
| CAR! | |   (( | |  ((  |
|    __| |   oo | |  oo  |
|   _/ | | /_/|_| | /_/|_|
| /_ __| |    | | |    | |
|   O  | |GOAT||| |GOAT|||
+------+ +------+ +------+"""
SECOND_CAR_OTHERS_GOAT = """
+------+ +------+ +------+
|  ((  | | CAR! | |  ((  |
|  oo  | |    __| |  oo  |
| /_/|_| |   _/ | | /_/|_|
|    | | | /_ __| |    | |
|GOAT||| |   O  | |GOAT|||
+------+ +------+ +------+"""
THIRD_CAR_OTHERS_GOAT = """
+------+ +------+ +------+
|  ((  | |  ((  | | CAR! |
|  oo  | |  oo  | |    __|
| /_/|_| | /_/|_| |   _/ |
|    | | |    | | | /_ __|
|GOAT||| |GOAT||| |   O  |
+------+ +------+ +------+
"""

print('''The Monty Hall Problem.
         In the Monty Hall game show, you can pick one of three doors. One door
         has a new car for a prize. The other rwo doors have worthless goats:
         {}
         Say you pick Door #1.
         Before the door you choose is opened, another door
         with a goat is opened:
         {}
         You can choose to either open the door you originally picked or swap
         to the other unopened door.

         It may seem like it dosen't matter if you swap or not, but your odds
         do improve if you swap doors! This program demonstrates the Monty Hall
         problem by letting you do repeated experimets.
         '''.format(ALL_CLOSED, THIRD_GOAT))
input('Press Enter to start...')

swap_wins = 0
swap_losses = 0
stay_wins = 0
stay_losses = 0
while True:
    door_that_has_car = random.randint(1, 3)
    print(ALL_CLOSED)
    while True:
        print('Pick a door 1, 2, or 3 (or "quit" to stop):')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if response in ('1', '2', '3'):
            break
    door_pick = int(response)

    while True:
        show_goat_door = random.randint(1, 3)
        if show_goat_door != door_pick and show_goat_door != door_that_has_car:
            break

    if show_goat_door == 1:
        print(FIRST_GOAT)
    elif show_goat_door == 2:
        print(SECOND_GOAT)
    elif show_goat_door == 3:
        print(THIRD_GOAT)

    print(f'Door {show_goat_door} contains a goat!')
    while True:
        print('Do you want to swap doors? Y/N.')
        swap = input('> ').upper()
        if swap in ('Y', 'N'):
            break

    if swap == 'Y':
        if door_pick == 1 and show_goat_door == 2:
            door_pick = 3
        elif door_pick == 1 and show_goat_door == 3:
            door_pick = 2
        elif door_pick == 2 and show_goat_door == 1:
            door_pick = 3
        elif door_pick == 2 and show_goat_door == 3:
            door_pick = 1
        elif door_pick == 3 and show_goat_door == 1:
            door_pick = 2
        elif door_pick == 3 and show_goat_door == 2:
            door_pick = 1

    if door_that_has_car == 1:
        print(FIRST_CAR_OTHERS_GOAT)
    elif door_that_has_car == 2:
        print(SECOND_CAR_OTHERS_GOAT)
    elif door_that_has_car == 3:
        print(THIRD_CAR_OTHERS_GOAT)
    print(f'Door {door_that_has_car} has the car!')

    if door_pick == door_that_has_car:
        print('You won!')
        if swap == 'Y':
            swap_wins += 1
        elif swap == 'N':
            stay_wins += 1
    else:
        print('Sorry, you lost.')
        if swap == 'Y':
            swap_losses += 1
        elif swap == 'N':
            stay_losses += 1

    total_swaps = swap_wins + swap_losses
    if total_swaps != 0:
        swap_success = round(swap_wins / total_swaps * 100, 1)
    else:
        swap_success = 0.0
    total_stays = stay_wins + stay_losses
    if total_stays != 0:
        stay_success = round(stay_wins / total_stays * 100, 1)
    else:
        stay_success = 0.0

    print()
    print('Swapping:        ', end='')
    print(f'{swap_wins} wins, {swap_losses} losses, ', end='')
    print(f'success rate {swap_success}%.')
    print('Not swapping:    ', end='')
    print(f'{stay_wins} wins, {stay_losses} losses, ', end='')
    print(f'success rate {stay_success}%.')
    print()
    input('Press Enter to repeat the experiment...')
