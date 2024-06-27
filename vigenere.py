"""Шифр Виженера.
Шифр Виженера - многоалфавитный шифр подстановки, настолько
эффективный, что его не могли взломать многие столетия."""


try:
    import pyperclip
except ImportError:
    pass


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('''Vgenère Cipher.
             The Vgenère Cipher is polyalphabetic substitution cipher
             that was powerful enought to remain unbroken for centuries.''')
    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ')
        if response.startswith('e'):
            mode = 'encrypt'
            break
        elif response.startswith('d'):
            mode = 'decrypt'
            break
        print('Please enter the letter e or d.')

    while True:
        print('Please specify the key to use.')
        print('It can be a word or any combination of letters:')
        response = input('> ').upper()
        if response.isalpha:
            key = response
            break

    print(f'Enter the massege to {mode}.')
    message = input('> ')
    if mode == 'encrypt':
        translated = encrypt_message(message, key)
    elif mode == 'decrypt':
        translated = decrypt_message(message, key)
    print(f'{mode.title()}sed meassege: ')
    print(translated)

    try:
        pyperclip.copy(translated)
        print(f'(Full {mode}sed text copied to clipboard.)')
    except NameError:
        pass


def encrypt_message(message, key):
    """Шифрует сообщение в соответствии с ключом."""

    return translate_message(message, key, 'encrypt')


def decrypt_message(message, key):
    """Дешифрует сообщение в соответствии с ключом."""

    return translate_message(message, key, 'decrypt')


def translate_message(message, key, mode):
    """Шефрует/дешефрует сообщение в соответствии с ключом."""

    translated = []
    key_index = 0
    key = key.upper()
    for symbol in message:
        number = LETTERS.find(symbol.upper())
        if number != -1:
            if mode == 'encrypt':
                number += LETTERS.find(key[key_index])
            elif mode == 'decrypt':
                number -= LETTERS.find(key[key_index])
            number %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[number])
            elif symbol.islower():
                translated.append(LETTERS[number].lower())

            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            translated.append(symbol)
    return ''.join(translated)


if __name__ == '__main__':
    main()
