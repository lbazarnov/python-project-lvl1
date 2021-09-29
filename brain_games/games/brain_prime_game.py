from brain_games.cli import (
    get_user_answer, generate_number, welcome_user, check_answer)


def is_prime(number):
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False

        divider += 1

    return True


def run_brain_prime_game():
    """Brain Prime game logic"""
    user_name = welcome_user()
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501 :)
    print(description)
    game_round = 0

    while game_round < 3:
        number = generate_number()
        print(f'Question: {number}')

        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        user_answer = get_user_answer()
        game_round = check_answer(
            user_answer, correct_answer, user_name, game_round)
