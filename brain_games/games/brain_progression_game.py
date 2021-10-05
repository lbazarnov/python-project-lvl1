from brain_games.engine import (
    get_user_answer, generate_number, welcome_user, check_answer)
from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def create_progression():
    """Creates arithmetic progression"""
    number = generate_number()
    progression = []
    progression_difference = randint(2, 5)
    progression_length = randint(5, 10)

    while len(progression) < progression_length:
        progression.append(number)
        number += progression_difference

    random_item = randint(2, len(progression)) - 1
    correct_answer = str(progression[random_item])
    dots = '..'
    progression[random_item] = dots
    progression = ' '.join([str(i) for i in progression])

    return progression, correct_answer


def run_brain_progression_game():
    """Brain Progression game logic"""
    user_name = welcome_user()
    print(DESCRIPTION)
    game_round = 0

    while game_round < 3:
        question, correct_answer = create_progression()
        print(f'Question: {question}')
        user_answer = get_user_answer()

        game_round = check_answer(
            user_answer, correct_answer, user_name, game_round)
