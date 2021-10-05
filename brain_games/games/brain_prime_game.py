from brain_games.engine import (
    ROUNDS_TOTAL, get_user_answer, generate_number, welcome_user, check_answer)

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    divisor = 2

    while divisor <= number / 2:
        if number % divisor == 0:
            return False

        divisor += 1

    return True


def run_brain_prime_game():
    """Brain Prime game logic"""
    user_name = welcome_user()
    print(DESCRIPTION)
    game_round = 0

    while game_round < ROUNDS_TOTAL:
        number = generate_number()
        print(f'Question: {number}')

        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        user_answer = get_user_answer()
        game_round = check_answer(
            user_answer, correct_answer, user_name, game_round)
