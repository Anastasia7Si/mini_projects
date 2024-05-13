"""Выбрасыватель игральных костей.
Моделирует выбрасывание костей, в нотации Dungeons & Dragons."""

import random
import sys

print('''Dice Roller.
         Enter what kind and how many dice ti roll. The format is the number of
         dice, followed by "d", followed by number of sides the dice have.
         You can also add a plus or minus adjustment.

         Examples:
            3d6 rolls three 6-sided dice
            1d10+2 rolls one 10-sided die and adds 2
            2d38-1 rolls two 38-sided die and subtracts 1
            QUIT quits the program.''')

while True:
    try:
        dise_str = input('> ')
        if dise_str.upper() == ' QUIT':
            print('Thanks for playing!')
            sys.exit()

        dise_str = dise_str.lower().replace(' ', '')
        d_index = dise_str.find('d')
        if d_index == -1:
            raise Exception('Missing the "d" character.')

        number_of_dise = dise_str[:d_index]
        if not number_of_dise.isdecimal():
            raise Exception('Missing the naumber of dise.')
        number_of_dise = int(number_of_dise)

        mod_index = dise_str.find('+')
        if mod_index == -1:
            mod_index = dise_str.find('-')
            if mod_index == -1:
                mod_index = dise_str.find('*')

        if mod_index == -1:
            number_of_sides = dise_str[d_index + 1:]
        else:
            number_of_sides = dise_str[d_index + 1: mod_index]
        if not number_of_sides.isdecimal():
            raise Exception('Missing the number of sides.')
        number_of_sides = int(number_of_sides)

        rolls = []
        for i in range(number_of_dise):
            result = random.randint(1, number_of_sides)
            rolls.append(result)

        if mod_index == -1:
            mod_amount = 0

        else:
            mod_amount = int(dise_str[mod_index + 1:])
            if dise_str[mod_index] == '-':
                sum_rolls = sum(rolls) - mod_amount
            elif dise_str[mod_index] == '+':
                sum_rolls = sum(rolls) + mod_amount
            elif dise_str[mod_index] == '*':
                sum_rolls = sum(rolls) * mod_amount

        print('Total: ', sum_rolls, '(Each die: ', end='')

        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        if mod_amount != 0:
            mod_sign = dise_str[mod_index]
            print(f', {mod_sign}{abs(mod_amount)}', end='')
        print(')')

    except Exception as exc:
        print('Invalidal input. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue
