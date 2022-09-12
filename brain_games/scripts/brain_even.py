import random
from brain_games.scripts.game_engine import engine


game_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even():
    number = random.randint(1, 100)
    return number, number % 2 == 0 and 'yes' or 'no'


def main():
    engine(is_even, game_question)


if __name__ == '__main__':
    main()
