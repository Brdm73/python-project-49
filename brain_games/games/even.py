import random
from ..games.common_games_logic import game_engine


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


#     while correct_answers < 3:
#         num = random.randint(1, 100)
#         print("Question:", num)
#         answer = input('Answer "yes" if the number is even, otherwise answer "no" ')
#
#         if (is_even(num) and answer == "yes") or (not is_even(num) and answer == "no"):
#             print("Correct!")
#             correct_answers += 1
#         else:
#             if answer == "yes":
#                 print(f"{answer} is wrong answer ;(. Correct answer was 'no'")
#                 print("Let's try again, " + name)
#             else:
#                 print(f"{answer} is wrong answer ;(. Correct answer was 'yes'")
#                 print("Let's try again, " + name)
#             return
#
#     print("Congratulations, " + name + "!")
#
#
# if __name__ == '__main__':
#     main()
