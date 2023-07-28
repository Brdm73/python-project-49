import random

GAME_LOGO = "brain-gcd\n"
GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f"{a} {b}"
    # print("Test question: " + question)
    correct_answer = gcd(a, b)
    # print("!!! Debugging !!! correct_answer: " + str(correct_answer))
    return question, correct_answer
