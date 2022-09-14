import math
import random


GAME_QUESTION = "Find the greatest common divisor of given numbers."


def gcd_game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = math.gcd(number1, number2)

    return f"{number1} {number2}", str(result)
