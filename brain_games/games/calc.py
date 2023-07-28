import random

GAME_LOGO = "brain-calc\n"
GAME_QUESTION = 'What is the result of the expression?'


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2}"
    correct_answer = eval(question)
    # print("TEST!!!! correct answer is: " + str(correct_answer))
    return question, correct_answer
