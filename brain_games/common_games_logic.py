#!/usr/bin/env python3

from brain_games.cli import welcome_user


def game_engine(generate_question, game_question):
    """
     Описание функции.
      Аргументы:
     arg1 -- функция возвращающая question(текущий вопрос),
      correct_answer(правильный ответ на него)
     arg2 -- переменная с тексом общего вопрос для конктретной игры
     """
    correct_answers_count = 0
    name = welcome_user()

    while correct_answers_count < 3:
        question, correct_answer = generate_question()
        print(game_question)
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if str(user_answer) == str(correct_answer):
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
