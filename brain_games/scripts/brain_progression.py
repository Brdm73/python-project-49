#!/usr/bin/env python3
from ..games.progression import play_progression
from ..common_games_logic import game_engine


def main():
    generated_question, correct_answer, game_question = play_progression()
    game_engine(generated_question, correct_answer, game_question)

if __name__ == '__main__':
    main()
