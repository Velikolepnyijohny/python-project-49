import random

def is_even(number):
    """Checks if a number is even."""
    return number % 2 == 0

def generate_round():
    """Generates a question and correct answer for the even number game."""
    number = random.randint(1, 100)
    question = number
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer

def run_game(description, generate_round):
    """Runs the brain game."""
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print(description)
    for _ in range(3):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(description, generate_round)

if __name__ == '__main__':
    main()
