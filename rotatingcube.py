"""Вращающийся куб.
Динмачиеское изображение вращающегося куба.
Нажнимте Ctrl+C для остановки."""

import math
import time
import sys
import os


PAUSE_AMOUNT = 0.1
WIDTH, HEIGHT = 80, 24
SCALE_X = (WIDTH - 4) // 8
SCALE_Y = (HEIGHT - 4) // 8
SCALE_Y *= 2
TRANSLATE_X = (WIDTH - 4) // 2
TRANSLATE_Y = (HEIGHT - 4) // 2
LINE_CHAR = chr(9608)
X_ROTATE_SPEED = 0.03
Y_ROTATE_SPEED = 0.08
Z_ROTATE_SPEED = 0.13

X = 0
Y = 1
Z = 2

CUBE_CORNERS = [
     [-1, -1, -1],
     [1, -1, -1],
     [-1, -1, 1],
     [1, -1, 1],
     [-1, 1, -1],
     [1, 1, -1],
     [-1, 1, 1],
     [1, 1, 1]
]
rotated_corners = [None, None, None, None, None, None, None, None]
x_rotation = 0.0
y_rotation = 0.0
z_rotation = 0.0


def line(x1, y1, x2, y2):
    """Возвращает список точек, лежащих на прямой между заданными точками.
    Использует алгортим Брезенхэма."""

    points = []
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]
    is_steep = abs(y2 - y1) > abs(x2 - x1)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    is_reversed = x1 > x2
    if is_reversed:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        delta_x = x2 - x1
        delta_y = abs(y2 - y1)
        extra_y = int(delta_x / 2)
        current_y = y2
        if y1 < y2:
            y_direction = 1
        else:
            y_direction = -1
        for current_x in range(x2, x1 - 1, -1):
            if is_steep:
                points.append((current_y, current_x))
            else:
                points.append((current_x, current_y))
            extra_y -= delta_y
            if extra_y <= 0:
                current_y -= y_direction
                extra_y += delta_x
    else:
        delta_x = x2 - x1
        delta_y = abs(y2 - y1)
        extra_y = int(delta_x / 2)
        current_y = y1
        if y1 < y2:
            y_direction = 1
        else:
            y_direction = -1
        for current_x in range(x1, x2 + 1):
            if is_steep:
                points.append((current_y, current_x))
            else:
                points.append((current_x, current_y))
            extra_y -= delta_y
            if extra_y < 0:
                current_y += y_direction
                extra_y += delta_x
    return points


def rotate_point(x, y, z, ax, ay, az):
    """Возвращает кортеж (x, y, z) из повёрнутых аргументов x, y, z.
    Вращение на углы ax, ay, az (в радианах) относительно начала
    координат 0, 0, 0. Направление осей координат:
     -y
      |
      +-- +x
     /
    +z"""

    rotated_x = x
    rotated_y = (y * math.cos(ax)) - (z * math.sin(ax))
    rotated_z = (y * math.sin(ax)) + (z * math.cos(ax))
    x, y, z = rotated_x, rotated_y, rotated_z
    rotated_x = (z * math.sin(ay)) + (x * math.cos(ay))
    rotated_y = y
    rotated_z = (z * math.cos(ay)) - (x * math.sin(ay))
    x, y, z = rotated_x, rotated_y, rotated_z
    rotated_x = (x * math.cos(az)) - (y * math.sin(az))
    rotated_y = (x * math.sin(az)) + (y * math.cos(az))
    rotated_z = z
    return (rotated_x, rotated_y, rotated_z)


def adjust_point(point):
    """Преобразуем трёхмерную точку XYZ в двумерную точку XY, подходящую для
    отображения на жкране. Для этого масштабируем данную двумерную точку на
    SCALE_X и SCALE_Y, а замтем сдвигаем её на TRANSLATE_X и TRANSLATE_Y."""

    return (int(point[X] * SCALE_X + TRANSLATE_X),
            int(point[Y] * SCALE_Y + TRANSLATE_Y))


try:
    while True:
        x_rotation += X_ROTATE_SPEED
        y_rotation += Y_ROTATE_SPEED
        z_rotation += Z_ROTATE_SPEED
        for i in range(len(CUBE_CORNERS)):
            x = CUBE_CORNERS[i][X]
            y = CUBE_CORNERS[i][Y]
            z = CUBE_CORNERS[i][Z]
            rotated_corners[i] = rotate_point(x, y, z,
                                              x_rotation, y_rotation,
                                              z_rotation)
        cube_points = []
        for from_corner_index, to_corner_index in ((0, 1), (1, 3), (3, 2),
                                                   (2, 0), (0, 4), (1, 5),
                                                   (2, 6), (3, 7), (4, 5),
                                                   (5, 7), (7, 6), (6, 4)):
            from_x, from_y = adjust_point(
                rotated_corners[from_corner_index]
                )
            to_x, to_y = adjust_point(rotated_corners[to_corner_index])
            points_on_line = line(from_x, from_y, to_x, to_y)
            cube_points.extend(points_on_line)
        cube_points = tuple(frozenset(cube_points))

        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in cube_points:
                    print(LINE_CHAR, end='', flush=False)
                else:
                    print(' ', end='', flush=False)
            print(flush=False)
        print('Press Ctrl-C to quit.', end='', flush=True)
        time.sleep(PAUSE_AMOUNT)

        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

except KeyboardInterrupt:
    print('Rotating Cube')
    sys.exit()
