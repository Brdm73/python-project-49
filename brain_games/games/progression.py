import random

GAME_LOGO = "brain-progression\n"
GAME_QUESTION = 'What number is missing in the progression?'


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


def transform_progression_to_string(progression):
    return ' '.join(map(str, progression))


def generate_question():
    progression, hidden_index = generate_progression()
    correct_answer = progression[hidden_index]
    # print("!!! Debugging !!! correct_answer: " + str(correct_answer))
    progression[hidden_index] = '..'
    question = transform_progression_to_string(progression)
    return question, correct_answer
