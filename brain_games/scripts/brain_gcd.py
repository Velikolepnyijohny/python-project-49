from brain_games.games import brain_gcd
from brain_games.engine import run_game


def main():
    run_game(brain_gcd.DESCRIPTION, brain_gcd.generate_round)


if __name__ == "__main__":
    main()
