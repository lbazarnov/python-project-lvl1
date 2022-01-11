from brain_games.engine import generate_number

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_number, second_number):
    while second_number != 0:
        first_number, second_number = second_number, first_number % second_number  # noqa: E501

    return first_number


def get_question_and_answer():
    """Brain GCD game logic"""
    first_number = generate_number()
    second_number = generate_number()
    question = f'{first_number} {second_number}'
    correct_answer = str(get_gcd(first_number, second_number))
    return question, correct_answer
