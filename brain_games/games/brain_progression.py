import random
from brain_games.engine import run_game

DESCRIPTION = "What number is missing in the progression?"
MIN_START = 1
MAX_START = 20
MIN_STEP = 2
MAX_STEP = 5
MIN_LENGTH = 5
MAX_LENGTH = 10


def generate_progression(start, step, length):
    """Generates an arithmetic progression."""
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression


def generate_round():
    """Generates a question and correct answer for the progression game."""
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer


def main():
    run_game(DESCRIPTION, generate_round)


if __name__ == "__main__":
    main()
