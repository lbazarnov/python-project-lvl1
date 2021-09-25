from random import choice
from brain_games.cli import (
    get_user_answer, generate_number, welcome_user, check_answer)


def get_result(operator, first_number, second_number):
    if operator == '+':
        result = first_number + second_number
        return result

    if operator == '-':
        result = first_number - second_number
        return result

    if operator == '*':
        result = first_number * second_number
        return result


def run_brain_calc_game():
    """Brain Calc game logic"""
    user_name = welcome_user()
    description = 'What is the result of the expression?'
    print(description)
    game_round = 0
    while game_round < 3:
        first_number = generate_number()
        second_number = generate_number()
        operator = choice(['+', '-', '*'])
        print(f'Question: {first_number} {operator} {second_number}')
        correct_answer = str(get_result(operator, first_number, second_number))
        user_answer = get_user_answer()

        game_round = check_answer(
            user_answer, correct_answer, user_name, game_round)
