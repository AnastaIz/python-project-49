import random


GAME_QUESTION = "Find the greatest common divisor of given numbers."


def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    
    m = min(number1, number2)

    for i in range(1, m + 1):
        if number1 % i == 0 and number2 % i == 0:
            result = i

    return f"{number1} {number2}", str(result)
