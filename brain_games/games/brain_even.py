from brain_games.engine import generate_number

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Checks a number is even or not"""
    return number % 2 == 0


def get_question_and_answer():
    """Brain Even game logic"""
    question = generate_number()

    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
