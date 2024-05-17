"""Простак.
Как заитриговать простака на многие часы (программа-шутка)."""

print('Gullible.')

while True:
    print('Do you wont to know how to keep a gullible person buse'
          ' for hours? Y/N')
    response = input('> ')
    if response.lower() in ('no', 'n'):
        break
    if response.lower() in ('yes', 'y'):
        continue
    print(f'{response} is not valid yes/no response.')
