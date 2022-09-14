from brain_games.game_engine import engine
from brain_games.games.game_prime import is_prime, GAME_QUESTION


def main():
    engine(is_prime, GAME_QUESTION)


if __name__ == '__main__':
    main()
