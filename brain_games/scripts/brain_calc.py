from brain_games.game_engine import engine
from brain_games.games.game_calc import calc, GAME_QUESTION


def main():
    engine(calc, GAME_QUESTION)


if __name__ == '__main__':
    main()
