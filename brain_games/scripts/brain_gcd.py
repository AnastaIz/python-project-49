import math
import random
from brain_games.scripts.game_engine import engine


game_question = "Find the greatest common divisor of given numbers."


def gcd_game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = math.gcd(number1, number2)

    return f"{number1} {number2}", str(result)


def main():
    engine(gcd_game, game_question)


if __name__ == '__main__':
    main()
