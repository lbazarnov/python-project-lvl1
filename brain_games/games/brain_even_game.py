from brain_games.cli import (
    get_user_answer, generate_number, welcome_user, check_answer)


def run_brain_even_game():
    """Brain Even game logic"""
    user_name = welcome_user()
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(description)
    game_round = 0
    while game_round < 3:
        number = generate_number()
        print(f'Question: {number}')
        user_answer = get_user_answer()

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        game_round = check_answer(
            user_answer, correct_answer, user_name, game_round)
