import random


DESCRIPTION = "What is the result of the expression?"


def calculate(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    else:
        raise ValueError(f"Invalid operator: {operator}")


def generate_round():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operators = ["+", "-", "*"]
    operator = random.choice(operators)
    question = f"{number1} {operator} {number2}"
    correct_answer = str(calculate(number1, number2, operator))
    return question, correct_answer
