"""Поросячья латынь.
Переводит сообщения на английском на поросячью латынь."""

try:
    import peperclip
except ImportError:
    pass

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')


def main():
    print('''Igpay Atinlay (Pig Latin)
             Enter yout message:''')
    pig_latin = english_to_pig_lanit(input('> '))
    print(pig_latin)
    try:
        peperclip.copy(pig_latin)
        print('(Copied pig laton to clipboard.)')
    except NameError:
        pass


def english_to_pig_lanit(message):
    """Перевод сообщения на поросячью латынь."""

    pig_latin = ''
    for word in message.split():
        prefix_non_letters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]
        if len(word) == 0:
            pig_latin = pig_latin + prefix_non_letters + ' '
            continue
        suffix_non_letters = ''
        while not word[-1].isalpha():
            suffix_non_letters = word[-1] + suffix_non_letters
            word = word[:-1]

        was_upper = word.isupper()
        was_title = word.istitle()
        word = word.lower()
        prefix_consonants = ''
        while len(word) > 0 and word not in VOWELS:
            prefix_consonants += word[0]
            word = word[1:]
        if prefix_consonants != '':
            word += prefix_consonants + 'ay'
        else:
            word += 'yay'

        if was_upper:
            word = word.upper()
        if was_title:
            word = word.title()

        pig_latin += prefix_non_letters + word + suffix_non_letters + ' '
    return pig_latin


if __name__ == '__main__':
    main()
