"""Арифметика с игральными костями.
Игра с обучающими карточками на сложение, в которой нужно
суммировать все очки на выброшенных игральных костях."""

import random
import time


DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3

QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 5

REWARD = 4
PENALTY = 1

assert MAX_DICE <= 14

D_1 = (['+-------+',
        '|       |',
        '|   O   |',
        '|       |',
        '+-------+'], 1)

D_2a = (['+-------+',
         '| O     |',
         '|       |',
         '|     O |',
         '+-------+'], 2)

D_2b = (['+-------+',
         '|     O |',
         '|       |',
         '| O     |',
         '+-------+'], 2)

D_3a = (['+-------+',
         '| O     |',
         '|   O   |',
         '|     O |',
         '+-------+'], 3)

D_3b = (['+-------+',
         '|     O |',
         '|   O   |',
         '| O     |',
         '+-------+'], 3)

D_4 = (['+-------+',
        '| O   O |',
        '|       |',
        '| O   O |',
        '+-------+'], 4)

D_5 = (['+-------+',
        '| O   O |',
        '|   O   |',
        '| O   O |',
        '+-------+'], 5)

D_6a = (['+-------+',
         '| O   O |',
         '| O   O |',
         '| O   O |',
         '+-------+'], 6)

D_6b = (['+-------+',
         '| O O O |',
         '|       |',
         '| O O O |',
         '+-------+'], 6)

ALL_DICE = [D_1, D_2a, D_2b, D_3a, D_3b, D_4, D_5, D_6a, D_6b]

print(f'''Dice Math.
       Add up the sides of all the dice displayed on the screen. You have
       {QUIZ_DURATION} seconds to answer as many as possible. You get {REWARD}
       points for each correct answer and lose {PENALTY} point for each
       incorrect answer.''')

input('Press Enter to begin...')

correct_answers = 0
incorrect_answers = 0
start_time = time.time()
while time.time() < start_time + QUIZ_DURATION:
    sum_answer = 0
    dice_faces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE)
        dice_faces.append(die[0])
        sum_answer += die[1]
    top_left_dice_corners = []
    for i in range(len(dice_faces)):
        while True:
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)
            top_left_x = left
            top_left_y = top
            top_right_x = left + DICE_WIDTH
            top_right_y = top
            bottom_left_x = left
            bottom_left_y = top + DICE_HEIGHT
            bottom_right_x = left + DICE_WIDTH
            bottom_right_y = top + DICE_HEIGHT

            overlaps = False
            for prev_die_left, prev_die_top in top_left_dice_corners:
                prev_die_right = prev_die_left + DICE_WIDTH
                prev_die_bottom = prev_die_top + DICE_HEIGHT

                for corner_x, corner_y in ((top_left_x, top_left_y),
                                           (top_right_x, top_right_y),
                                           (bottom_left_x, bottom_left_y),
                                           (bottom_right_x, bottom_right_y)):
                    if (prev_die_left <= corner_x < prev_die_right and
                            prev_die_top <= corner_y < prev_die_bottom):
                        overlaps = True
            if not overlaps:
                top_left_dice_corners.append((left, top))
                break

    canvas = {}
    for i, (die_left, die_top) in enumerate(top_left_dice_corners):
        die_face = dice_faces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                canvas_x = die_left + dx
                canvas_y = die_top + dy
                canvas[(canvas_x, canvas_y)] = die_face[dy][dx]

    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ''), end='')
        print()

    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sum_answer:
        correct_answers += 1
    else:
        print('Incorrect, the answer is ', sum_answer)
        time.sleep(2)
        incorrect_answers += 1


score = (correct_answers * REWARD) - (incorrect_answers * PENALTY)
print('Correct: ', correct_answers)
print('Incorrect: ', incorrect_answers)
print('Score: ', score)
