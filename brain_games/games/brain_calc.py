from random import choice
from brain_games.engine import generate_number

DESCRIPTION = 'What is the result of the expression?'


def get_result(operand, first_number, second_number):
    """Finds result of operation"""
    if operand == '+':
        result = first_number + second_number
    elif operand == '-':
        result = first_number - second_number
    elif operand == '*':
        result = first_number * second_number

    return result


def get_question_and_answer():
    """Brain Calc game logic"""
    first_number = generate_number()
    second_number = generate_number()
    operand = choice(['+', '-', '*'])
    question = f'{first_number} {operand} {second_number}'
    correct_answer = str(get_result(operand, first_number, second_number))
    return question, correct_answer
