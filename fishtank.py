"""Аквариум.
Безмятежное динамическое изображение аквариума.
Нажмите Ctrl+C для остановки.
Аналогична ASCIIQuarium и @EmojiAquarium, но эта программа основана
на более старой программе ASCII-аквариума под DOS."""

import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext mobule, which you')
    print('can install with command "pip install Bext".')
    sys.exit()

WIDTH, HEIGHT = bext.size()
WIDTH -= 1

NUM_KELP = 2
NU_FISH = 10
NUM_BUBBLERS = 1
FRAMES_PER_SECOND = 4
FISH_TYPES = [
  {'right': ['><>'],          'left': ['<><']},
  {'right': ['>||>'],         'left': ['<||<']},
  {'right': ['>))>'],         'left': ['<[[<']},
  {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
  {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
  {'right': ['>-==>'],        'left': ['<==-<']},
  {'right': [r'>\\>'],        'left': ['<//<']},
  {'right': ['><)))*>'],      'left': ['<*(((><']},
  {'right': ['}-[[[*>'],      'left': ['<*]]]-{']},
  {'right': [']-<)))b>'],     'left': ['<d(((>-[']},
  {'right': ['><XXX*>'],      'left': ['<*XXX><']},
  {'right': ['_.-._.-^=>', '.-._.-.^=>',
             '-._.-._^=>', '._.-._.^=>'],
   'left':  ['<=^-._.-._', '<=^.-._.-.',
             '<=^_.-._.-', '<=^._.-._.']},
]
LONGEST_FISH_LENGTH = 10
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2


def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP
    bext.bg('black')
    bext.clear()

    FISHES = []
    for a in range(NU_FISH):
        FISHES.append(generate_fish())

    BUBBLERS = []
    for i in range(NUM_BUBBLERS):
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))
    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelp_x = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {'x': kelp_x, 'segments': []}
        for i in range(random.randint(6, HEIGHT - 1)):
            kelp['segments'].append(random.choice([')', '(']))
        KELPS.append(kelp)

    STEP = 1
    while True:
        simulate_aquarium()
        draw_aquarium()
        time.sleep(1 / FRAMES_PER_SECOND)
        clear_aquarium()
        STEP += 1


def get_random_color():
    """Возвращает строковое значение со случайным цветом."""
    return random.choice(('black', 'red', 'green', 'yellow', 'blue',
                          'purple', 'cyan', 'white'))


def generate_fish():
    """Возвращает соответствующей рыбке ассоциативный массив."""
    fish_type = random.choice(FISH_TYPES)
    collor_pattern = random.choice(('random', 'head-tail', 'single'))
    fish_length = len((fish_type['right'][0]))
    if collor_pattern == 'random':
        colors = []
        for i in range(fish_length):
            colors.append(get_random_color())
    if collor_pattern == 'single' or collor_pattern == 'head-tail':
        colors = [get_random_color()] * fish_length
    if collor_pattern == 'head-tail':
        head_tail_color = get_random_color()
        colors[0] = head_tail_color
        colors[-1] = head_tail_color

    fish = {'right': fish_type['right'],
            'left': fish_type['left'],
            'colors': colors,
            'h_speed': random.randint(1, 6),
            'v_speed': random.randint(5, 15),
            'time_toH_dir_change': random.randint(10, 60),
            'time_toV_dir_change': random.randint(2, 20),
            'going_right': random.choice([True, False]),
            'going_down': random.choice([True, False])}
    fish['x'] = random.randint(0, WIDTH - 1 - LONGEST_FISH_LENGTH)
    fish['y'] = random.randint(0, HEIGHT - 2)
    return fish


def simulate_aquarium():
    """Моделирует один шаг движений в аквариуме."""
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP

    for fish in FISHES:
        if STEP % fish['h_speed'] == 0:
            if fish['going_right']:
                if fish['x'] != RIGHT_EDGE:
                    fish['x'] += 1
                else:
                    fish['going_right'] = False
                    fish['colors'].reverse()
            else:
                if fish['x'] != LEFT_EDGE:
                    fish['x'] -= 1
                else:
                    fish['going_right'] = True
                    fish['colors'].reverse()
        fish['time_toH_dir_change'] -= 1
        if fish['time_toH_dir_change'] == 0:
            fish['time_toH_dir_change'] = random.randint(10, 60)
            fish['going_right'] = not fish['going_right']

        if STEP % fish['v_speed'] == 0:
            if fish['going_down']:
                if fish['y'] != BOTTOM_EDGE:
                    fish['y'] += 1
                else:
                    fish['going_down'] = False
            else:
                if fish['y'] != TOP_EDGE:
                    fish['y'] -= 1
                else:
                    fish['going_down'] = True
        fish['time_toV_dir_change'] -= 1
        if fish['time_toV_dir_change'] == 0:
            fish['time_toV_dir_change'] = random.randint(10, 60)
            fish['going_down'] = not fish['going_down']

    for bubble in BUBBLES:
        dice_roll = random.randint(1, 6)
        if (dice_roll == 1) and (bubble['x'] != LEFT_EDGE):
            bubble['x'] -= 1
        elif (dice_roll == 2) and (bubble['x'] != RIGHT_EDGE):
            bubble['x'] += 1
        bubble['x'] -= 1

    for i in range(len(BUBBLES) - 1, -1, -1):
        if BUBBLES[i]['y'] == TOP_EDGE:
            del BUBBLES[i]

    for kelp in KELPS:
        for i, kelp_segment in enumerate(kelp['segments']):
            if random.randint(1, 20) == 1:
                if kelp_segment == '(':
                    kelp['segments'][i] = ')'
                elif kelp_segment == ')':
                    kelp['segments'][i] = '('


def draw_aquarium():
    """Отрисовываем аквариум на экране."""
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP

    bext.fg('white')
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', 'o')), end='')

    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])

        if fish['going_right']:
            fish_text = fish['right'][STEP % len(fish['right'])]
        else:
            fish_text = fish['left'][STEP % len(fish['left'])]

        for i, fish_part in enumerate(fish_text):
            bext.fg(fish['colors'][i])
            print(fish_part, end='')

    bext.fg('green')
    for kelp in KELPS:
        for i, kelp_segment in enumerate(kelp['segments']):
            if kelp_segment == '(':
                bext.goto(kelp['x'], BOTTOM_EDGE - i)
            elif kelp_segment == ')':
                bext.goto(kelp['x'] + 1, BOTTOM_EDGE - i)
            print(kelp_segment, end='')

    bext.fg('yellow')
    bext.goto(0, HEIGHT - 1)
    print(chr(9617) * (WIDTH - 1), end='')

    sys.stdout.flush()


def clear_aquarium():
    """Зарисовываем весь аквариум пробелами."""
    global FISHES, BUBBLERS, BUBBLES, KELPS

    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(' ', end='')

    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])
        print(' ' * len(fish['left'][0]), end='')

    for kelp in KELPS:
        for i, kelp_segment in enumerate(kelp['segments']):
            bext.goto(kelp['x'], HEIGHT - 2 - i)
            print(' ', end='')

    sys.stdout.flush()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
