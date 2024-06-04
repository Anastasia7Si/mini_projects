"""лотерея Powerball.
Моделирование лотереи, позволяющее почувствовать всё удовольствие от
проигрыша в лтерее, не тратя понапрасну денег."""

import random


print('''Powerball Lottery.
         Each powerball lottery ticket costs $2. The jackpot for this game
         is $1.586 billion! It dosen't matter what the jackpot is, though,
         because the odds are 1 in 292,201,338, so you won't win.
         This simulation gives you the thrill of playing witahout wasting
         money.''')
while True:
    print('Enter 5 different numbers from 1 to 69, with spaces between')
    print('each number. (For example: 5, 17, 23, 42, 50)')
    response = input('> ')
    numbers = response.split()
    if len(numbers) != 5:
        print('Please enter 5 numbers, separated by spaces.')
        continue

    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print('Please enter numbers, like 27, 35, or 62.')
        continue

    for i in range(5):
        if not (1 <= numbers[i] <= 69):
            print('The numbers must all be between 1 and 69.')
            continue

    if len(set(numbers)) != 5:
        print('You must enter 5 different numbers.')
        continue
    break

while True:
    print('Enter the powerball number from 1 to 26.')
    response = input('> ')
    try:
        powerball = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15, or 22.')
        continue

    if not (1 <= powerball <= 26):
        print('The powerball numbers must be between 1 and 26.')
        continue
    break

while True:
    print('How many times do you want to play? (Max: 1_000_000)')
    response = input('> ')
    try:
        num_plays = int(response)
    except ValueError:
        print('Please enter a number, like 3, 15, or 22000.')
        continue

    if not (1 <= num_plays <= 1_000_000):
        print('You can play between 1 and 1_000_000 times.')
        continue
    break

price = '$' + str(2 * num_plays)
print(f'It costs {price} to play {num_plays} times, but don\'t worry.')
print('I\'m sure you\'ll win it all back.')
input('Press Enter to start...')

possible_numbers = list(range(1, 70))
for i in range(num_plays):
    random.shuffle(possible_numbers)
    winning_numbers = possible_numbers[0:5]
    winning_powerball = random.randint(1, 26)
    print('The winning numbers are: ', end='')
    all_winning_numbers = ''
    for i in range(5):
        all_winning_numbers += str(winning_numbers[i]) + ' '
    all_winning_numbers += 'and ' + str(winning_powerball)
    print(all_winning_numbers.ljust(21), end='')
    if (set(numbers) == set(winning_numbers)
       and powerball == winning_powerball):
        print()
        print('You have won the Powervall Lottyru! Congratulations,')
        print('you would be a billionaire if this was real!')
        break
    else:
        print(' You lost.')

print(f'You have waster {price}.')
print('Thanks for playing!')
