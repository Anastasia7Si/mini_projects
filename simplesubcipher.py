"""Простой шифр подстановки.
Простой шифр подстановки с взаимооднозначным преобразованием всех
символов открытого и зашифрованного текста."""

import random


try:
    import pyperclip
except ImportError:
    pass


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('''Simple Substitution Cipher.
             A simple substitution cipher has a one-to-one translation
             for each symbol in the plaintext and each symbol in the
             ciphertext.''')
    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            mode = 'encrypt'
            break
        elif response.startswith('d'):
            mode = 'decrypt'
            break
        print('Please enter the letter e or d.')
    while True:
        print('Please specify the key to use.')
        if mode == 'encrypt':
            print('or enter RANDOM to have one generated for you.')
        response = input('> ').upper()
        if response == 'RANDOM':
            key = generate_random_key()
            print(f'The key is {key}. KEEP THIS SECRET!')
            break
        else:
            if check_key(response):
                key = response
                break
    print(f'Enter the message to {mode}.')
    message = input('> ')

    if mode == 'encrypt':
        translated = encrypt_message(message, key)
    elif mode == 'decrypt':
        translated = decrypt_message(message, key)
    print(f'The {mode}sed message is: {translated}')

    try:
        pyperclip.copy(translated)
        print(f'(Full {mode}sed text copied to clipboard.)')
    except NameError:
        pass


def generate_random_key():
    """генерирует и возвращает случайный ключ шифрования."""

    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


def check_key(key):
    """Возвращает True, если ключ допустимый. В противном случае
    возвращает False."""

    key_list = list(key)
    letters_list = list(LETTERS)
    key_list.sort()
    letters_list.sort()
    if key_list != letters_list:
        print('There is an error in the key or symbol set.')
        return False
    return True


def encrypt_message(message, key):
    """Шифрует сообщение  в соответсвии с ключом key."""

    return translate_message(message, key, 'encrypt')


def decrypt_message(message, key):
    """Дешифрует сообщение  в соответсвии с ключом key."""

    return translate_message(message, key, 'decrypt')


def translate_message(message, key, mode):
    """Дешифрует и шифрует сообщение в соответсвии с ключом key."""

    translated = ''
    chars_A = LETTERS
    chars_B = key
    if mode == 'decrypt':
        chars_A, chars_B = chars_B, chars_A
    for symbol in message:
        if symbol.upper() in chars_A:
            symbol_index = chars_A.find(symbol.upper())
            if symbol.isupper():
                translated += chars_B[symbol_index].upper()
            else:
                translated += chars_B[symbol_index].lower()
        else:
            translated += symbol
    return translated


if __name__ == '__main__':
    main()
