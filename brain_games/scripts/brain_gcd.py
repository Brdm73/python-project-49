#!/usr/bin/env python3
from ..games.gcd import play_gcd
from ..common_games_logic import game_engine


def main():
    generated_question, correct_answer, game_question = play_gcd()
    game_engine(generated_question, correct_answer, game_question)


if __name__ == '__main__':
    main()
