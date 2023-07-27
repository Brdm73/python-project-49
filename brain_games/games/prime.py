import random


def play_prime():
    print("brain-prime\n")

    def generate_question():
        num = random.randint(1, 100)
        counter = 0
        for i in range(1, num + 1):
            if num % i == 0:
                counter += 1
        return num, "yes" if counter == 2 else "no"

    game_question = 'Answer "yes" if given number is prime. ' \
                    'Otherwise answer "no".'
    generated_question, correct_answer = generate_question()

    return generated_question, correct_answer, game_question
