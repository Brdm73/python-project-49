from random import randint
import random

GAME_LOGO = "brain-progression\n"
GAME_QUESTION = 'What number is missing in the progression?'

LOWER_LIMIT = 1
UPPER_LIMIT = 100
PROGRESSION_LENGTH = 10

LOWER_STEP_LIMIT = 1
UPPER_STEP_LIMIT = 10


def generate_progression():
    # Генерируем  арифметическую прогрессию
    start = randint(LOWER_LIMIT, UPPER_LIMIT)
    step = randint(LOWER_STEP_LIMIT, UPPER_STEP_LIMIT)
    progression = [start + (step * i) for i in range(PROGRESSION_LENGTH)]
    # Генерируем случайную позицию для скрытого элемента
    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)
    return progression, hidden_index


def transform_progression_to_string(progression):
    return ' '.join(map(str, progression))


def generate_question():
    progression, hidden_index = generate_progression()
    correct_answer = progression[hidden_index]
    # print("!!! Debugging !!! correct_answer: " + str(correct_answer))
    progression[hidden_index] = '..'
    question = transform_progression_to_string(progression)
    return question, correct_answer
