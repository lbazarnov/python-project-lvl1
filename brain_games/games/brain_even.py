from brain_games.engine import generate_number

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Checks a number is even or not"""
    if number % 2 == 0:
        return True


def get_question_and_answer():
    """Brain Even game logic"""
    number = generate_number()
    question = f'Question: {number}'

    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
