"""Японский абак - соробан.
Моделирование японского счётного инструмента типа абака."""

NUMBER_OF_DIGITS = 20


def main():
    print('Soroban - The Japanese Abacus.\n')
    abacus_number = 0
    while True:
        display_abacus(abacus_number)
        display_controls()
        commands = input('> ')
        if commands == 'quit':
            break
        elif commands.isdecimal():
            abacus_number = int(commands)
        else:
            for letter in commands:
                if letter == 'q':
                    abacus_number += 1_000_000_000
                elif letter == 'a':
                    abacus_number -= 1_000_000_000
                elif letter == 'w':
                    abacus_number += 1_000_000_00
                elif letter == 's':
                    abacus_number -= 1_000_000_00
                elif letter == 'e':
                    abacus_number += 1_000_000_0
                elif letter == 'd':
                    abacus_number -= 1_000_000_0
                elif letter == 'r':
                    abacus_number += 1_000_000
                elif letter == 'f':
                    abacus_number -= 1_000_000
                elif letter == 't':
                    abacus_number += 1_000_00
                elif letter == 'g':
                    abacus_number -= 1_000_00
                elif letter == 'y':
                    abacus_number += 1_000_0
                elif letter == 'h':
                    abacus_number -= 1_000_0
                elif letter == 'u':
                    abacus_number += 1_000
                elif letter == 'j':
                    abacus_number -= 1_000
                elif letter == 'i':
                    abacus_number += 100
                elif letter == 'k':
                    abacus_number -= 100
                elif letter == 'o':
                    abacus_number += 10
                elif letter == 'l':
                    abacus_number -= 10
                elif letter == 'p':
                    abacus_number += 1
                elif letter == ';':
                    abacus_number -= 1
        if abacus_number < 0:
            abacus_number = 0
        if abacus_number > 9_999_999_999:
            abacus_number = 9_999_999_999


def display_abacus(number):
    """Отображает абакус."""

    number_list = list(str(number).zfill(NUMBER_OF_DIGITS))
    has_bead = []
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '01234')
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '56789')
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '12346789')
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '234789')
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '034589')
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '014569')
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '012567')
    for i in range(NUMBER_OF_DIGITS):
        has_bead.append(number_list[i] in '01235678')

    abacus_char = []
    for i, beat_present in enumerate(has_bead):
        if beat_present:
            abacus_char.append('O')
        else:
            abacus_char.append('|')

    chars = abacus_char + number_list
    print("""
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  |  |  |  |  |  |  |  |  |  |  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+
""".format(*chars))


def display_controls():
    """"Отображает команды управлениия."""

    print(' +q w e r t y u i o p')
    print(' -a s d f g h j k l ;')
    print('(Enter a number,\'quit\', or a stream of up/down letters)')


if __name__ == '__main__':
    main()
