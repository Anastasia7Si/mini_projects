"""Песочные часы.
Динмаическое изображение песочных часов. Нажмите Ctrl+c для остановки."""

import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext mobule, which you')
    print('can install with command "pip install Bext".')
    sys.exit()

PAUSE_LENGTH = 0.2
WIDE_FALL_CHANCE = 50
SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25
X = 0
Y = 1
SAND = chr(9617)
WALL = chr(9608)
HOURGLASS = set()

for i in range(18, 37):
    HOURGLASS.add((i, 1))
    HOURGLASS.add((i, 23))

for i in range(1, 5):
    HOURGLASS.add((18, i))
    HOURGLASS.add((36, i))
    HOURGLASS.add((18, i + 19))
    HOURGLASS.add((36, i + 19))

for i in range(8):
    HOURGLASS.add((19 + i, 5 + i))
    HOURGLASS.add((35 - i, 5 + i))
    HOURGLASS.add((25 - i, 13 + i))
    HOURGLASS.add((29 + i, 13 + i))

INITIAL_SAND = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        INITIAL_SAND.add((x, y + 4))


def main():
    bext.fg('yellow')
    bext.clear()
    bext.goto(0, 0)
    print('Ctrl-C to quit.', end='')

    for wall in HOURGLASS:
        bext.goto(wall[X], wall[Y])
        print(WALL, end='')

    while True:
        all_sand = list(INITIAL_SAND)
        for sand in all_sand:
            bext.goto(sand[X], sand[Y])
            print(SAND, end='')

        run_hour_glass_simulation(all_sand)


def run_hour_glass_simulation(all_send):
    """Моделируем падение песка, пока он не прекратит двигаться."""

    while True:
        random.shuffle(all_send)
        sand_moved_on_this_step = False
        for i, sand in enumerate(all_send):
            if sand[Y] == SCREEN_HEIGHT - 1:
                continue

            no_sand_below = (sand[X], sand[Y] + 1) not in all_send
            no_wall_below = (sand[X], sand[Y] + 1) not in HOURGLASS
            can_fall_down = no_sand_below and no_wall_below

            if can_fall_down:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
                bext.goto(sand[X], sand[Y] + 1)
                print(SAND, end='')

                all_send[i] = (sand[X], sand[Y] + 1)
                sand_moved_on_this_step = True
            else:
                below_left = (sand[X] - 1, sand[Y] + 1)
                no_sand_below_left = below_left not in all_send
                no_wall_below_left = below_left not in HOURGLASS
                left = (sand[X] - 1, sand[Y])
                no_wall_left = left not in HOURGLASS
                not_on_left_edge = sand[X] > 0
                can_fall_left = (no_sand_below_left and no_wall_below_left
                                 and no_wall_left and not_on_left_edge)

                below_right = (sand[X] + 1, sand[Y] + 1)
                no_sand_below_right = below_right not in all_send
                no_wall_below_right = below_right not in HOURGLASS
                right = (sand[X] + 1, sand[Y])
                no_wall_right = right not in HOURGLASS
                not_on_right_edge = sand[X] < SCREEN_WIDTH - 1
                can_fall_right = (no_sand_below_right and no_wall_below_right
                                  and no_wall_right and not_on_right_edge)

                falling_direction = None
                if can_fall_left and not can_fall_right:
                    falling_direction = - 1
                elif not can_fall_left and can_fall_right:
                    falling_direction = 1
                elif can_fall_left and can_fall_right:
                    falling_direction = random.choice((-1, 1))

            if random.random() * 100 <= WIDE_FALL_CHANCE:
                below_two_left = (sand[X] - 2, sand[Y] + 1)
                no_sand_below_two_left = below_two_left not in all_send
                no_wall_below_two_left = below_two_left not in HOURGLASS
                not_on_second_to_left_edge = sand[X] > 1
                can_fall_two_left = (can_fall_left and no_sand_below_two_left
                                     and no_wall_below_two_left
                                     and not_on_second_to_left_edge)

                below_two_right = (sand[X] + 2, sand[Y] + 1)
                no_sand_below_two_right = below_two_right not in all_send
                no_wall_below_two_right = below_two_left not in HOURGLASS
                not_on_second_to_right_edge = sand[X] < SCREEN_WIDTH - 2
                can_fall_two_right = (can_fall_right
                                      and no_sand_below_two_right
                                      and no_wall_below_two_right
                                      and not_on_second_to_right_edge)

                if can_fall_two_left and not can_fall_two_right:
                    falling_direction = - 2
                elif not can_fall_two_left and can_fall_two_right:
                    falling_direction = 2
                elif can_fall_two_left and can_fall_two_right:
                    falling_direction = random.choice((-2, 2))

                if falling_direction is None:
                    continue
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
                bext.goto(sand[X] + falling_direction, sand[Y] + 1)
                print(SAND, end='')

                all_send[i] = (sand[X] + falling_direction, sand[Y] + 1)
                sand_moved_on_this_step = True

        sys.stdout.flush()
        time.sleep(PAUSE_LENGTH)

        if not sand_moved_on_this_step:
            time.sleep(2)
            for sand in all_send:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
                break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
