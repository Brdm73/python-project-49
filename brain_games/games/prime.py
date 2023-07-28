import random


GAME_LOGO = "brain-prime\n"
GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    question = random.randint(1, 100)
    counter = 0
    for i in range(1, question + 1):
        if question % i == 0:
            counter += 1
    return question, "yes" if counter == 2 else "no"
