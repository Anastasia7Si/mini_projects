"""Моделирование индикатора хода выполнения.
Пример динамического индикатора хода выполнения,
пригодного для использования и в других программах."""

import random
import time


BAR = chr(9608)


def main():
    print('Progress Bar Simulation.')
    bytes_downloaded = 0
    download_size = 4096
    while bytes_downloaded < download_size:
        bytes_downloaded += random.randint(0, 100)
        bar_str = get_progress_bar(bytes_downloaded, download_size)
        print(bar_str, end='', flush=True)
        time.sleep(0.2)
        print('\b' * len(bar_str), end='', flush=True)


def get_progress_bar(progress, total, bar_width=40):
    """Возвращает строковое значение, соответствующее индикатору хода
    выполнения из bar_width полосок, дошедшему до progress из общего
    количества total."""

    progress_bar = ''
    progress_bar += '['

    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    number_of_bars = int((progress / total) * bar_width)
    progress_bar += BAR * number_of_bars
    progress_bar += ' ' * (bar_width - number_of_bars)
    progress_bar += ']'

    percent_complete = round(progress / total * 100, 1)
    progress_bar += ' ' + str(percent_complete) + '%'
    progress_bar += ' ' + str(progress) + '/' + str(total)
    return progress_bar


if __name__ == '__main__':
    main()
