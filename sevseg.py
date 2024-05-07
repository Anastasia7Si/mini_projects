"""Sevseg.
Семисегментный модуль индикации, используемый в программах "Обратный
отсчёт" и "Цифровые часы"."""

"""Семимегментный индикатор, сегменты обозначены буквами от A до G:
 __A__
|     | Все цифры, отображаемые на семисегментном индикаторе:
F     B  __     __  __        __   __  __   __   __
|__G__| |  | |  __| __| |__| |__  |__    | |__| |__|
|     | |__| | |__  __|    |  __| |__|   | |__|  __|
E     C
|__D__|"""


def get_sev_seg_str(number, win_wigth=0):
    """Врзвращает строковое значение для цифры на семисегментном
    индикаторе. Если возвращаемое строковое значение меньше win_wigth,
    оно дополняется нулями."""
    number = str(number).zfill(win_wigth)
    rows = ['', '', '']
    for i, numaral in enumerate(number):
        if numaral == '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue
        elif numaral == '-':
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numaral == '0':
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numaral == '1':
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   | '
        elif numaral == '2':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numaral == '3':
            rows[0] += '__ '
            rows[1] += '__|'
            rows[2] += '__|'
        elif numaral == '4':
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numaral == '5':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numaral == '6':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numaral == '7':
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numaral == '8':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numaral == '9':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        if i != len(number) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)


if __name__ == '__main__':
    print('This module is meant to be iported rather than run.')
    print('For example, this code:')
    print('     import sevseg')
    print('     my_number = sevseg.get_sev_seg_str(42, 3)')
    print('     print(my_number)')
    print()
    print('Will print 42, zero padded to three digits:')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')
