"""Я обвиняю!
Детективная игра с обманом и пропавшей кошкой."""

import time
import random
import sys


SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS',
            'SENATOR SCHMEAR', 'MRS. FEATHERTOSS', 'DR. JEAN SPLICER',
            'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL',
         'ANIMEVHS TAPE', 'JAR OF PICKLES', 'ONE COWBOY BOOT',
         'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE',
          'BOWLING ALLEY', 'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY',
          'ALBINO ALLIGATOR PIT']
TIME_TO_SLOVE = 300
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)

known_suspects_and_items = []
visited_pleces = {}
currnet_location = 'TAXI'
accused_suspects = []
liars = random.sample(SUSPECTS, random.randint(3, 4))
accusations_left = 3
culprit = random.choice(SUSPECTS)
random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

clues = {}
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue

    clues[interviewee] = {}
    clues[interviewee]['debag_liar'] = False
    for item in ITEMS:
        if random.randint(0, 1) == 0:
            clues[interviewee][item] = PLACES[ITEMS.index(item)]
        else:
            clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]
    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
        else:
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]

for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue

    clues[interviewee] = {}
    clues[interviewee]['debag_liar'] = True
    for item in ITEMS:
        if random.randint(0, 1) == 0:
            while True:
                clues[interviewee][item] = random.choice(PLACES)
                if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                    break
        else:
            while True:
                clues[interviewee][item] = random.choice(SUSPECTS)
                if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                    break
    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            while True:
                clues[interviewee][suspect] = random.choice(PLACES)
                if clues[interviewee][suspect] != PLACES[ITEMS.index(item)]:
                    break
        else:
            while True:
                clues[interviewee][suspect] = random.choice(ITEMS)
                if (clues[interviewee][suspect]
                        != ITEMS[SUSPECTS.index(suspect)]):
                    break

zophie_clues = {}
for interviewee in random.sample(SUSPECTS, random.randint(3, 4)):
    kind_of_clue = random.randint(1, 3)
    if kind_of_clue == 1:
        if interviewee not in liars:
            zophie_clues[interviewee] = culprit
        elif interviewee in liars:
            while True:
                zophie_clues[interviewee] = random.choice(SUSPECTS)
                if zophie_clues[interviewee] != culprit:
                    break
    elif kind_of_clue == 2:
        if interviewee not in liars:
            zophie_clues[interviewee] = PLACES[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                zophie_clues[interviewee] = random.choice(PLACES)
                if (zophie_clues[interviewee]
                   != PLACES[SUSPECTS.index(culprit)]):
                    break
    elif kind_of_clue == 3:
        if interviewee not in liars:
            zophie_clues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                zophie_clues[interviewee] = random.choice(ITEMS)
                if zophie_clues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                    break

# Раскомментируйте, чтобы увидеть держимое структур данных с зацепками
# import pprint
# pprint.pprint(clues)
# pprint.pprint(zophie_clues)
# print('culprit =', culprit)

print('''J\'ACCUSE! (a mystery game)
         Inspired by Homestar Runner\'s "Where\'s an Egg?" game.
         You care the world-famous detective Mathilde Camus.
         ZOPHIE THE CAY has gone missing and you must sift through the clues.
         Suspects either always tell lies, or always tell the truth. Ask tham
         about other people, places, and items to see if the details they give
         are truthful and consistent with yoyr observations. Then you will know
         if their clue about ZOPHIE THE CAT is true or not.
         Will you find ZOPHIE THE CAT in time and accuse the guilty party?''')
input('Press Enter to begin...')

start_time = time.time()
end_time = start_time + TIME_TO_SLOVE

while True:
    if time.time() > end_time or accusations_left == 0:
        if time.time() > end_time:
            print('You have run out of time!')
        elif accusations_left == 0:
            print('You have accused too many incorrect people!')
        culprit_index = SUSPECTS.index(culprit)
        print(f'It was {culprit} at the {PLACES[culprit_index]} with the '
              f'{ITEMS[culprit_index]} who catnapped her!')
        print('Better luck next time, Detective')
        sys.exit()
    print()
    minutes_left = int(end_time - time.time()) // 60
    seconds_left = int(end_time - time.time()) % 60
    print(f'Time left: {minutes_left} min {seconds_left} sec.')

    if currnet_location == 'TAXI':
        print('You are in your TAXI. Where do you want to go?')
        for place in sorted(PLACES):
            place_info = ''
            if place in visited_pleces:
                place_info = visited_pleces[place]
            name_label = '(' + place[0] + ')' + place[1:]
            spacing = " " * (LONGEST_PLACE_NAME_LENGTH - len(place))
            print(f'{name_label} {spacing}{place_info}')
        print('(Q)UIT GAME')

        while True:
            response = input('> ').upper()
            if response == '':
                continue
            if response == 'Q':
                print('Thanks for playing!')
                sys.exit()
            if response in PLACE_FIRST_LETTERS.keys():
                break
        currnet_location = PLACE_FIRST_LETTERS[response]
        continue

    print(f'You are at the {currnet_location}.')
    currnet_location_index = PLACES.index(currnet_location)
    the_person_here = SUSPECTS[currnet_location_index]
    the_item_here = ITEMS[currnet_location_index]
    print(f'{the_person_here} with the {the_item_here} is here.')

    if the_person_here not in known_suspects_and_items:
        known_suspects_and_items.append(the_person_here)
    if ITEMS[currnet_location_index] not in known_suspects_and_items:
        known_suspects_and_items.append(ITEMS[currnet_location_index])
    if currnet_location not in visited_pleces.keys():
        visited_pleces[currnet_location] = (f'{the_person_here.lower()}, '
                                            f'{the_item_here.lower()}')

    if the_person_here in accused_suspects:
        print('They are offended that you accused them,')
        print('and will not help with your investigation.')
        print('You go back to your TAXI.')
        print()
        input('Press Enter co continue...')
        currnet_location = 'TAXI'
        continue
    print()
    print(f'(J)"J\'ACCUSE" ({accusations_left} accusations left.)')
    print('(Z) Ask if they know where ZOPHIE THA CAT is.')
    print('(T) Go back to the TAXI.')
    for i, suspect_or_item in enumerate(known_suspects_and_items):
        print(f'({i + 1}) Ask about {suspect_or_item}.')

    while True:
        response = input('> ').upper()
        if response in 'JZT' or (response.isdecimal() and 0 < int(response)
                                 <= len(known_suspects_and_items)):
            break
    if response == 'J':
        accusations_left -= 1
        if the_person_here == culprit:
            print('You\'ve cracked the case, Detective!')
            print(f'It was {culprit} who had catnapped ZOPHIE THE CAT.')
            minutes_taked = int(time.time() - start_time) // 60
            seconds_taked = int(time.time() - start_time) % 60
            print(f'Good job! You sloved it in {minutes_taked} '
                  f'min {seconds_taked} sec.')
            sys.exit()
        else:
            accused_suspects.append(the_person_here)
            print('You have accused the wrong person, Ditective!')
            print('They will not help you with anymore clues.')
            print('You go back to yout TAXI.')
            currnet_location = 'TAXI'
    elif response == 'Z':
        if the_person_here not in zophie_clues:
            print('"I don\'t know anything about ZOPHIE CAT."')
        elif the_person_here in zophie_clues:
            print(f'They give you this clue: "{zophie_clues[the_person_here]}')
            if (zophie_clues[the_person_here] not in known_suspects_and_items
               and zophie_clues[the_person_here] not in PLACES):
                known_suspects_and_items.append(zophie_clues[the_person_here])
    elif response == 'T':
        currnet_location = 'TAXI'
        continue
    else:
        thing_being_asked_about = known_suspects_and_items[int(response) - 1]
        if thing_being_asked_about in (the_person_here, the_item_here):
            print('Theu give you this clue: "No comment."')
        else:
            print(f'They give you this clue: "'
                  f'{clues[the_person_here][thing_being_asked_about]}"')
            if (clues[the_person_here][thing_being_asked_about]
               not in known_suspects_and_items
               and clues[the_person_here][thing_being_asked_about]
               not in PLACES):
                known_suspects_and_items.append(
                    clues[the_person_here][thing_being_asked_about]
                    )

    input('Press Enter to continue...')
