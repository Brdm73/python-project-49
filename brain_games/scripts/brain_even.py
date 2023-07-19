#!/usr/bin/env python3

import random
from ..cli import welcome_user


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def main():
    correct_answers = 0

    name = welcome_user()

    while correct_answers < 3:
        num = random.randint(1, 100)
        print("Question:", num)
        answer = input('Answer "yes" if the number is even, otherwise answer "no" ')

        if (is_even(num) and answer == "yes") or (not is_even(num) and answer == "no"):
            print("Correct!")
            correct_answers += 1
        else:
            if answer == "yes":
                print(f"{answer} is wrong answer ;(. Correct answer was 'no'")
                print("Let's try again, " + name)
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was 'yes'")
                print("Let's try again, " + name)
            return

    print("Congratulations, " + name + "!")


if __name__ == '__main__':
    main()
