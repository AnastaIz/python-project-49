import random


GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even():
    number = random.randint(1, 100)
    return number, number % 2 == 0 and 'yes' or 'no'
