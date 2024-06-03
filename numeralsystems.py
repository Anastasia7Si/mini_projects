"""Счёт в различных системах счисления.
Отображает эквивалентные числа в десятичной, двоичной и шестнадцатеричной
системах счисления."""

print('''Numeral System Counters.
         This programm shows you equivalent number in decimal (base 10),
         hexadecimal (base 16), and binary (base 2) numeral systems.
         (Ctrl-C to quit.)''')

while True:
    response = input('Enter the starting number (e. g. 0) > ')
    if response == '':
        response = 0
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than or equal to 0.')
start = int(response)

while True:
    response = input('Enter how many numbers to display (e. g. 1000) > ')
    if response == '':
        response = 1000
        break
    if response.isdecimal():
        break
    print('Please enter a number')
amount = int(response)

for number in range(start, start + amount):
    hex_number = hex(number)[2:].upper()
    oct_number = oct(number)[2:]
    bin_number = bin(number)[2:]
    print('DEC: ', number, '    HEX: ', hex_number,
          '    OCT: ', oct_number, '   BIN: ', bin_number)
