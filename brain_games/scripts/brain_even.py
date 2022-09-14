from brain_games.game_engine import engine
from brain_games.games.game_even import is_even, GAME_QUESTION


def main():
    engine(is_even, GAME_QUESTION)


if __name__ == '__main__':
    main()
