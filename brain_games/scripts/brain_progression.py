from brain_games.games import brain_progression
from brain_games.engine import run_game


def main():
    run_game(brain_progression.DESCRIPTION, brain_progression.generate_round)


if __name__ == "__main__":
    main()
