from brain_games.games import brain_calc
from brain_games.engine import run_game


def main():
    run_game(brain_calc.DESCRIPTION, brain_calc.generate_round)


if __name__ == "__main__":
    main()
