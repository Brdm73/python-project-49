import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def play_gcd():
    print("brain-gcd\n")

    def generate_question():
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        question = f"{a} {b}"
        # print("Test question: " + question)
        correct_answer = gcd(a, b)
        # print("!!! Вebugging !!! correct_answer: " + str(correct_answer))
        return question, correct_answer

    game_question = 'Find the greatest common divisor of given numbers.'
    generated_question, correct_answer = generate_question()

    return generated_question, correct_answer, game_question
