import random
from brain_games.engine import run_game

DESCRIPTION = 'Answer "yes" if the given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = number
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer

def main():
    run_game(DESCRIPTION, generate_round)

if __name__ == '__main__':
    main()
