"""Цифровые часы.
Отображает показывающие текущее время цифровые часы с
семисегментным индикатором. Для остановки нажмите Ctrl+C."""

import time
import sys
from sevseg import get_sev_seg_str

seconds_left = 120

try:
    while True:
        print('\n' * 20)
        current_time = time.localtime()
        hours = str(current_time.tm_hour % 12)
        if hours == '0':
            hours == '12'
        minutes = str(current_time.tm_min)
        seconds = str(current_time.tm_sec)

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
        print()
        print('Press Ctrl-C to quit.')

        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != current_time.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital Clock.')
    sys.exit()
