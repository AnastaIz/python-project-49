import random


GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
    number = random.randint(1, 20)
    counter = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            counter += 1
    return number, (counter == 0 and number != 1) and 'yes' or 'no'
