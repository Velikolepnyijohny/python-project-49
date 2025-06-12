import random
import math
from brain_games.engine import run_game

DESCRIPTION = "Find the greatest common divisor of given numbers."
MIN_NUM = 1
MAX_NUM = 100


def generate_round():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer


def main():
    run_game(DESCRIPTION, generate_round)


if __name__ == "__main__":
    main()
