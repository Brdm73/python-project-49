import random


GAME_LOGO = "brain-even\n"
GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no" '


def is_even(num):
    return num % 2 == 0


def generate_question():
    question = random.randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'

    return question, correct_answer
