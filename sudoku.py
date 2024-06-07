"""Головоломка судоку.
Классическая головоломка на расстановку цифр на доске 9Х9.
"""

import copy
import random
import sys


EMPTY_SPACE = '.'
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH


class SudokuGrid:

    def __init__(self, original_setup):
        self.original_setup = original_setup
        self.grid = {}
        self.reset_grid()
        self.moves = []

    def reset_grid(self):
        """Восстоналивает состояние поле, отслеживаемое в self.grid,
        до состояния из self.original_setup."""

        for x in range(1, GRID_LENGTH + 1):
            for y in range(1, GRID_LENGTH + 1):
                self.grid[(x, y)] = EMPTY_SPACE

        assert len(self.original_setup) == FULL_GRID_SIZE
        i = 0
        y = 0
        while i < FULL_GRID_SIZE:
            for x in range(GRID_LENGTH):
                self.grid[(x, y)] = self.original_setup[i]
                i += 1
            y += 1

    def make_move(self, column, row, number):
        """Помещает число в столбец column (буква от A до I) и строку
        row (число от 1 до 9) в поле."""

        x = 'ABCDEFGHI'.find(column)
        y = int(row) - 1

        if self.original_setup[y * GRID_LENGTH + x] != EMPTY_SPACE:
            return False

        self.grid[(x, y)] = number
        self.moves.append(copy.copy(self.grid))
        return True

    def undo(self):
        """Устанавливает текущее состояние поля равным предыдущему
        состоянию из списка self.moves."""

        if self.moves == []:
            return
        self.moves.pop()

        if self.moves == []:
            self.reset_grid()
        else:
            self.grid = copy.copy(self.moves[-1])

    def display(self):
        """Отображает текущее состояние поля на экране."""

        print('   A B C  D E F  G H I')
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                if x == 0:
                    print(str(y + 1) + '  ', end='')
                print(self.grid[(x, y)] + ' ', end='')
                if x == 2 or x == 5:
                    print('| ', end='')
            print()
            if y == 2 or y == 5:
                print('   ------+-------+------')

    def _is_complete_set_of_numbers(self, numbers):
        """Возвращает True, если numbers содержит цивры от 1 до 9."""

        return sorted(numbers) == list('123456789')

    def is_sloved(self):
        """Возвращает True, если текущее поле
        находится в решённом состоянии."""

        for row in range(GRID_LENGTH):
            row_numbers = []
            for x in range(GRID_LENGTH):
                number = self.grid[(x, row)]
                row_numbers.append(number)
            if not self._is_complete_set_of_numbers(row_numbers):
                return False
        for column in range(GRID_LENGTH):
            column_numbers = []
            for y in range(GRID_LENGTH):
                number = self.grid[(column, y)]
                row_numbers.append(number)
            if not self._is_complete_set_of_numbers(column_numbers):
                return False
        for box_x in (0, 3, 6):
            for box_y in (0, 3, 6):
                box_numbers = []
                for x in range(BOX_LENGTH):
                    for y in range(BOX_LENGTH):
                        number = self.grid[(box_x + x, box_y + y)]
                        box_numbers.append(number)
                if not self._is_complete_set_of_numbers(box_numbers):
                    return False
        return True


print('''Sudoku Puzzle.
         Sudoku is a number placement logic puzzle game. A Sudoku
         grid as a 9x9 grid of numbers. Try to place numbers in the grid
         such that every row, column, and 3x3 box has the numbers 1 throught
         9 once and only once.
         For example, here is a starting Sudoke grid and its solved from:

         5 3 . | . 7 . | . . .      5 3 4 | 6 7 8 | 9 1 2
         6 . . | 1 9 5 | . . .      6 7 2 | 1 9 5 | 3 4 8
         . 9 8 | . . . | . 6 .      1 9 8 | 3 4 2 | 5 6 7
         ------+-------+------      ------+-------+------
         8 . . | . 6 . | . . 3      8 5 9 | 7 6 1 | 4 2 3
         4 . . | 8 . 3 | . . 1 -->  4 2 6 | 8 5 3 | 7 9 1
         7 . . | . 2 . | . . 6      7 1 3 | 9 2 4 | 8 5 6
         ------+-------+------      ------+-------+------
         . 6 . | . . . | 2 8 .      9 6 1 | 5 3 7 | 2 8 4
         . . . | 4 1 9 | . . 5      2 8 7 | 4 1 9 | 6 3 5
         . . . | . 8 . | . 7 9      3 4 5 | 2 8 6 | 1 7 9''')
input('Press Enter to begin...')

with open('sudokupuzzles.txt') as puzzle_file:
    puzzles = puzzle_file.readlines()

for i, puzzle in enumerate(puzzles):
    puzzles[i] = puzzle.strip()

grid = SudokuGrid(random.choice(puzzles))
while True:
    grid.display()
    if grid.is_sloved():
        print('Congratulations! You solved the puzzle!')
        print('Thanks for playing!')
        sys.exit()
    while True:
        print('\nEnter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:')
        print('(For example, a move looks like "B4 9".)')
        action = input('> ').upper().strip()
        if len(action) > 0 and action[0] in ('R', 'N', 'U', 'O', 'Q'):
            break
        if len(action.split()) == 2:
            sapce, number = action.split()
            if len(sapce) != 2:
                continue
            column, row = sapce
            if column not in list('ABCDEFGHI'):
                print(f'There is no column {column}.')
                continue
            if not row.isdecimal() or not (1 <= int(row) <= 9):
                print(f'There is no row {row}.')
                continue
            if not (1 <= int(number) <= 9):
                print(f'Select a number from 1 to 9, not {number}.')
                continue
            break
    print()

    if action.startswith('R'):
        grid.reset_grid()
        continue
    if action.startswith('N'):
        grid = SudokuGrid(random.choice(puzzles))
        continue
    if action.startswith('U'):
        grid.undo()
        continue
    if action.startswith('O'):
        original_grid = SudokuGrid(grid.original_setup)
        print('The orogonal grid looked like this:')
        original_grid.display()
        input('Press Enter to continue...')
    if action.startswith('Q'):
        print('Thanks for playing!')
        sys.exit()

    if grid.make_move(column, row, number) is False:
        print('You cannot overwrite the original grid\'s numbers.')
        print('Enter ORIGINAL to view the original grid.')
        input('Press Enter to continue...')
