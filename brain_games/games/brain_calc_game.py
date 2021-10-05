from random import choice
from brain_games.engine import generate_number

DESCRIPTION = 'What is the result of the expression?'


def get_result(operator, first_number, second_number):
    """Finds result of operation"""
    if operator == '+':
        result = first_number + second_number
        return result

    if operator == '-':
        result = first_number - second_number
        return result

    if operator == '*':
        result = first_number * second_number
        return result


def dispatch_answer():
    """Brain Calc game logic"""
    first_number = generate_number()
    second_number = generate_number()
    operator = choice(['+', '-', '*'])
    question = f'Question: {first_number} {operator} {second_number}'
    correct_answer = str(get_result(operator, first_number, second_number))
    return question, correct_answer
