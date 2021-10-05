from brain_games.engine import generate_number

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


def dispatch_answer():
    """Brain GCD game logic"""
    first_number = generate_number()
    second_number = generate_number()
    question = f'Question: {first_number} {second_number}'
    correct_answer = str(get_gcd(first_number, second_number))
    return question, correct_answer
