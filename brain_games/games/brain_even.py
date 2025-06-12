import random
from brain_games.engine import run_game

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = random.randint(MIN_NUM, MAX_NUM)
    question = number
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer


def main():
    run_game(DESCRIPTION, generate_round)


if __name__ == "__main__":
    main()
