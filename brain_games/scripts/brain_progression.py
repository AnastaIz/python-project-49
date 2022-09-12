import random
from brain_games.scripts.game_engine import engine


game_question = 'What number is missing in the progression?'


def progression():
    initial_term = random.randint(1, 20)
    step = random.randint(2, 10)

    pr = [str(initial_term + (step * i)) for i in range(10)]
    result = pr[random.randint(0, 9)]

    pr = ' '.join(pr)

    return pr.replace(result, '..'), result


def main():
    engine(progression, game_question)


if __name__ == '__main__':
    main()
