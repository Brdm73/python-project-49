import random
from ..common_games_logic import game_engine


def is_even(num):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"


def play_even():
    print("brain-even\n")

    def generate_question():
        num = random.randint(1, 100)
        correct_answer = is_even(num)

        return num, correct_answer

    game_question = 'Answer "yes" if the number is even, otherwise answer "no" '

    game_engine(generate_question, game_question)
