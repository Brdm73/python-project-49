import random

GAME_LOGO = "brain-prime\n"
GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    return True if counter == 2 else False


def generate_question():
    question = random.randint(1, 100)
    correct_answer = "yes" if is_prime(question) else "no"

    return question, correct_answer
