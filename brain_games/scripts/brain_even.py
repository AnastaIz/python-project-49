from random import randint
from brain_games.scripts.game_engine import engine


def is_even(number):
    counter = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            counter += 1
    return (counter == 0 and number > 1) and 'yes' or 'no'


def is_even_game():
    number = randint(1, 20)
    return number, is_even(number)


game_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    engine(is_even_game, game_question)


if __name__ == '__main__':
    main()
