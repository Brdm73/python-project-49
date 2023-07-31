#!/usr/bin/env python3

from brain_games.cli import welcome_user


def game_engine(game):
    """
     Описание функции.
      Аргументы:
     На вход ожидается модуль содержащий следующие атрибуты:
     GAME_LOGO
     GAME_QUESTION
     generate_question() (функция должна возвращать: question, correct_answer)
     """
    correct_answers_count = 0
    name = welcome_user()
    print(game.GAME_LOGO)
    print(game.GAME_QUESTION)

    while correct_answers_count < 3:
        question, correct_answer = game.generate_question()
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
