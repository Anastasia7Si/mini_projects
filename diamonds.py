"""Ромбы.
Рисует ромбы различного размера.
                           /\       /\
                          /  \     //\\
            /\     /\    /    \   ///\\\
           /  \   //\\  /      \ ////\\\\
 /\   /\  /    \ ///\\\ \      / \\\\////
/  \ //\\ \    / \\\///  \    /   \\\///
\  / \\//  \  /   \\//    \  /     \\//
 \/   \/    \/     \/      \/       \/
"""


def main():
    print('Diamonds.')

    for diamond_size in range(1, 6):
        display_out_line_diamond(diamond_size)
        print()
        display_filled_diamond(diamond_size)
        print()


def display_out_line_diamond(size):
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/', end='')
        print(' ' * (i * 2), end='')
        print('\\')

    for i in range(size):
        print(' ' * i, end='')
        print('\\', end='')
        print(' ' * ((size - i - 1) * 2), end='')
        print('/')


def display_filled_diamond(size):
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/' * (i + 1), end='')
        print('\\' * (i + 1))

    for i in range(size):
        print(' ' * i, end='')
        print('\\' * (size - i), end='')
        print('/' * (size - i))


if __name__ == '__main__':
    main()
