import random
from ..common_games_logic import game_engine


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

    game_engine(generate_question, game_question)