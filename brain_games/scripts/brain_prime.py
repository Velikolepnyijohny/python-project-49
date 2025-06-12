from brain_games.games import brain_prime
from brain_games.engine import run_game


def main():
    run_game(brain_prime.DESCRIPTION, brain_prime.generate_round)


if __name__ == "__main__":
    main()
