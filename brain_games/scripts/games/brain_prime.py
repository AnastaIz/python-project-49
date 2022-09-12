import random
from brain_games.scripts.game_engine import engine


game_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    counter = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            counter += 1
    return (counter == 0 and number > 1) and 'yes' or 'no'


def is_prime_game():
    number = random.randint(1, 20)
    return number, is_prime(number)


def main():
    engine(is_prime_game, game_question)


if __name__ == '__main__':
    main()
