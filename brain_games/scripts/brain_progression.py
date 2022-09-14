from brain_games.game_engine import engine
from brain_games.games.game_progression import progression, GAME_QUESTION


def main():
    engine(progression, GAME_QUESTION)


if __name__ == '__main__':
    main()
