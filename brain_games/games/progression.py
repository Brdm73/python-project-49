import random
from ..games.common_games_logic import game_engine


def generate_progression():
    # Генерируем случайную длину прогрессии от 5 до 10
    length = random.randint(5, 10)
    # Генерируем случайную арифметическую прогрессию
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    progression = [start + (step * i) for i in range(length)]
    # Генерируем случайную позицию для скрытого элемента
    hidden_index = random.randint(0, length - 1)
    return progression, hidden_index


def play_progression():
    print("brain-progression\n")

    def generate_question():
        progression, hidden_index = generate_progression()
        correct_answer = progression[hidden_index]
        # print("!!! Вebugging !!! correct_answer: " + str(correct_answer))
        progression[hidden_index] = '..'
        question = progression
        return question, correct_answer

    game_question = "What number is missing in the progression?"

    game_engine(generate_question, game_question)