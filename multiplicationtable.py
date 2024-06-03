"""Таблица умножения.
Выводит на экран таблицу умножения."""


print('Multiplication Table')
print('  |   0   1   2   3   4   5   6   7  8   9  10  11  12')
print('--+---------------------------------------------------')

for number_1 in range(0, 13):
    print(str(number_1).rjust(2), end='')
    print('|', end='')
    for number_2 in range(0, 13):
        print(str(number_1 * number_2).rjust(3), end=' ')
    print()
