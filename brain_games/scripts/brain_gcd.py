from brain_games.game_engine import engine
from brain_games.games.game_gcd import gcd_game, GAME_QUESTION


def main():
    engine(gcd_game, GAME_QUESTION)


if __name__ == '__main__':
    main()
