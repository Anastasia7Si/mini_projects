"""Шифр ROT13.
Простейший шифр сдвига для шафрования и дешифровки текста."""

try:
    import pyperclip
except ImportError:
    pass


UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxy'

print('ROT13 Cipher.\n')
while True:
    print('Enter a message to encrypt/decrypt (or QIUT).')
    massege = input('> ')
    if massege.upper() == 'QUIT':
        break
    translated = ''
    for character in massege:
        if character.isupper():
            trans_char_index = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[trans_char_index]
        elif character.islower():
            trans_char_index = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[trans_char_index]
        else:
            character += character
    print(f'The translated message is: {translated}.\n')

    try:
        pyperclip.copy(translated)
        print('(Copied to clipboard.)')
    except NameError:
        pass
