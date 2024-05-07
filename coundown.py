"""Обратный отсчёт.
Отображает динамическое изображение таймера обратного отсчёта с помощью
семисегментного индикатора. Для остановки нажмите Ctrl+C."""

import time
import sys
from sevseg import get_sev_seg_str

seconds_left = 120

try:
    while True:
        print('\n' * 20)
        hours = str(seconds_left // 3600)
        minutes = str((seconds_left % 3600) // 60)
        seconds = str(seconds_left % 60)
        hours_digits = get_sev_seg_str(hours, 2)
        (hours_top_row, hours_middle_row,
         hours_bottom_row) = hours_digits.splitlines()

        minutes_digits = get_sev_seg_str(minutes, 2)
        (minutes_top_row, minutes_middle_row,
         minutes_bottom_row) = minutes_digits.splitlines()

        seconds_digits = get_sev_seg_str(seconds, 2)
        (seconds_top_row, seconds_middle_row,
         seconds_bottom_row) = seconds_digits.splitlines()

        print(hours_top_row + '     '
              + minutes_top_row + '     ' + seconds_top_row)
        print(hours_middle_row + '  *  '
              + minutes_middle_row + '  *  ' + seconds_middle_row)
        print(hours_bottom_row + '  *  '
              + minutes_bottom_row + ' *  ' + seconds_bottom_row)

        if seconds_left == 0:
            print()
            print('     * * * * BOOM * * * *')
            break
        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)
        seconds_left -= 1
except KeyboardInterrupt:
    print('Countdown.')
    sys.exit()
