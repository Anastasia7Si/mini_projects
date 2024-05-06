"""генератор заголовков-приманок.
Генератор заголовков-применок для сайта со скучным контентом."""

import random

OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


def main():
    print('Clickbait Headline Generator.')
    print()

    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generete:')
        response = input('> ')

        if not response.isdecimal():
            print('Please enter number.')
        else:
            number_of_headlines = int(response)
            break

    for i in range(number_of_headlines):
        clickbait_type = random.randint(1, 8)

        if clickbait_type == 1:
            head_line = generate_are_millennials_killing_headline()
        elif clickbait_type == 2:
            head_line = generate_what_you_dont_know_headline()
        elif clickbait_type == 3:
            head_line = generate_bit_companies_hate_headline()
        elif clickbait_type == 4:
            head_line = generate_you_wont_believe_headline()
        elif clickbait_type == 5:
            head_line = generate_dont_want_you_to_know_headline()
        elif clickbait_type == 6:
            head_line = generate_gift_idea_headline()
        elif clickbait_type == 7:
            head_line = generate_reasons_why_headline()
        elif clickbait_type == 8:
            head_line = ganerate_job_automated_headline()
        print(head_line)
    print()

    website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Googles',
                             'Facesbook', 'Tweedie', 'Pastagram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or you\'re fired!')


def generate_are_millennials_killing_headline():
    return f'Are Millennials Killing the {random.choice(NOUNS)} Industry?'


def generate_what_you_dont_know_headline():
    plural_noun = random.choice(NOUNS) + 's'
    return (f'Without This {random.choice(NOUNS)}, {plural_noun} '
            f'Could kill You {random.choice(WHEN)}.')


def generate_bit_companies_hate_headline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun_1 = random.choice(NOUNS)
    noun_2 = random.choice(NOUNS)
    return (f'Big Companies Hate {pronoun}! See How This {state} {noun_1} '
            f'Invented a Cheaper {noun_2}.')


def generate_you_wont_believe_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(OBJECT_PRONOUNS)
    place = random.choice(PLACES)
    return (f'You Won\'t Bealive What This {state} {noun} '
            f'Found in {pronoun} {place}.')


def generate_dont_want_you_to_know_headline():
    plural_noun_1 = random.choice(NOUNS) + 's'
    plural_noun_2 = random.choice(NOUNS) + 's'
    return (f'What {plural_noun_1} Don\'t Want You to Know '
            f'About {plural_noun_2}.')


def generate_gift_idea_headline():
    number = random.randint(7, 15)
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    return f'{number} Gifts Ideas to Give Your {noun} From {state}.'


def generate_reasons_why_headline():
    number_1 = random.randint(3, 19)
    number_2 = random.randint(1, number_1)
    plural_noun_1 = random.choice(NOUNS) + 's'
    return (f'{number_1} Reasons Why {plural_noun_1} Are More Intarasting '
            f'Than You Think (Number {number_2}) Will Surprise You!')


def ganerate_job_automated_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    i = random.randint(0, 2)
    pronoun_1 = POSSESIVE_PRONOUNS[i]
    pronoun_2 = PERSONAL_PRONOUNS[i]

    if pronoun_1 == 'Their':
        return (f'This {state} {noun} Don\'t Thiks Robots Would Take '
                f'{pronoun_1} Job. {pronoun_2} Were Wrong.')
    else:
        return (f'This {state} {noun} Don\'t Thiks Robots Would Take '
                f'{pronoun_1} Job. {pronoun_2} Was Wrong.')


if __name__ == '__main__':
    main()
