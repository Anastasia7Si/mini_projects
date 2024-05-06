"""Имитационное моделирование парадокса дней рождения."""

import datetime
import random


def get_birthdays(number_of_birthdays):
    """Возвращаем список объектов дат для случайных дней рождения."""
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(1990, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    """Возвращаем объекты дня рождения, встречающегося
    несколько раз в списке дней рождения."""
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1:]):
            if birthday_a == birthday_b:
                return birthday_a


print('''Birthday Paradox.
      The Birthday Paradox shows us that in a group of N people, the odds
      that two of them have atching birthdays is  surorisingly large.
      This program doas a Monte Carlo simulation (that is, repeated random
      simulations) to explore this concept.

      (It's not actually a paradox, it's just a surprising result.)''')


MONTHS = ('Jan', 'Fab', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', ' Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_birthdays = int(response)
        break

print()

print('Here are', num_birthdays, 'birthdays:')
birthdays = get_birthdays(num_birthdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    month_name = MONTHS[birthday.month - 1]
    date_text = ' {} {}'.format(month_name, birthday.day)
    print(date_text, end='')
print()
print()

match = get_match(birthdays)

print('In this simulation, ', end='')
if match is not None:
    month_name = MONTHS[match.month - 1]
    date_text = '{} {}'.format(month_name, match.day)
    print('multiple people have a birthday on', date_text)
else:
    print('there are no matching birthdays.')

print()

print('Generating', num_birthdays, 'random birthdays 100 000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100 000 simulations.')
simulation_match = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = get_birthdays(num_birthdays)
    if get_match(birthdays) is not None:
        simulation_match += 1
print('100 000 simulations run.')

probability = round(simulation_match / 100_000 * 100, 2)
print('Out of 100 000 simulations of', num_birthdays, 'people where was a '
      'matching birthday in that group', simulation_match, 'times. This means')
print('that', num_birthdays, 'people have a', probability, '% chance of '
      'having a matching birthday in their group.')
print('That\'s probably more than you would think!')
