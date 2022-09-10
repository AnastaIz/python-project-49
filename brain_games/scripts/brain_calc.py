import random
import operator
from brain_games.scripts.game_engine import engine


game_question = "What is the result of the expression?"


def calc():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    oper = random.choice('+-*')

    if oper == '+':
        result = operator.add(number1, number2)
    elif oper == '-':
        result = operator.sub(number1, number2)
    else:
        result = operator.mul(number1, number2)

    return f'{number1} {oper} {number2}', str(result)


def main():
    engine(calc, game_question)


if __name__ == '__main__':
    main()
