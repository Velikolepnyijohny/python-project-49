from brain_games.games import brain_even
from brain_games.engine import run_game


def main():
    run_game(brain_even.DESCRIPTION, brain_even.generate_round)

if __name__ == '__main__':
    main()
