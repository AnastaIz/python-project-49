import random


GAME_QUESTION = "What is the result of the expression?"


def generate_round():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    oper = random.choice('+-*')

    if oper == '+':
        result = number1 + number2
    elif oper == '-':
        result = number1 - number2
    else:
        result = number1 * number2

    return f'{number1} {oper} {number2}', str(result)
