from brain_games.engine import (
    ROUNDS_TOTAL, get_user_answer, generate_number, welcome_user, check_answer)

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_number, second_number):
    """Finds GCD of two numbers"""
    a = first_number
    b = second_number
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def run_brain_gcd_game():
    """Brain GCD game logic"""
    user_name = welcome_user()
    print(DESCRIPTION)
    game_round = 0
    while game_round < ROUNDS_TOTAL:
        first_number = generate_number()
        second_number = generate_number()
        print(f'Question: {first_number} {second_number}')
        correct_answer = str(get_gcd(first_number, second_number))
        user_answer = get_user_answer()

        game_round = check_answer(
            user_answer, correct_answer, user_name, game_round)
