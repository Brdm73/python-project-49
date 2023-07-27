import random


def play_calc():
    print("brain-calc\n")

    def generate_question():
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2}"
        correct_answer = eval(question)
        # print("TEST!!!! correct answer is: " + str(correct_answer))
        return question, correct_answer

    game_question = "What is the result of the expression?"
    generated_question, correct_answer = generate_question()

    return generated_question, correct_answer, game_question
