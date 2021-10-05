from brain_games.engine import generate_number

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def dispatch_answer():
    """Brain Even game logic"""
    number = generate_number()
    question = f'Question: {number}'

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
