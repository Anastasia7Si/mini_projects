"""гУбКоРеГиСтР
Преобразует сообщения в гУбКоТеКсТ."""

import random


try:
    import pyperclip
except ImportError:
    pass


def main():
    """Запуск программы "гУбКоРеГиСтР"."""

    print('''sPoNgEcAsE.
             eNtEr YoUr MeSsAgE:''')
    sponge_text = message_to_spongecase(input('> '))
    print('\n', sponge_text)

    try:
        pyperclip.copy(sponge_text)
        print('(CoPiEd SpOnGeTeXt to ClIpbOaRd.)')
    except NameError:
        pass


def message_to_spongecase(message):
    """Возвращает заданную строку в губкорегистре."""

    sponge_text = ''
    use_upper = False
    for character in message:
        if not character.isalpha():
            sponge_text += character
            continue
        if use_upper:
            sponge_text += character.upper()
        else:
            sponge_text += character.lower()

        if random.randint(1, 100) <= 90:
            use_upper = not use_upper
    return sponge_text


if __name__ == '__main__':
    main()
