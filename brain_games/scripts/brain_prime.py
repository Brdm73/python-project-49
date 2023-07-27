#!/usr/bin/env python3
from ..games.prime import play_prime
from ..common_games_logic import game_engine


def main():
    generated_question, correct_answer, game_question = play_prime()
    game_engine(generated_question, correct_answer, game_question)


if __name__ == '__main__':
    main()
