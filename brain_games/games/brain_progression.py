from brain_games.engine import generate_number
from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def create_progression():
    """Creates arithmetic progression"""
    number = generate_number()
    progression = []
    progression_difference = randint(2, 5)
    progression_length = randint(5, 10)

    while len(progression) < progression_length:
        progression.append(number)
        number += progression_difference

    return progression


def convert_progression():
    """Converts progression to string"""
    progression = create_progression()
    puzzled_item = randint(2, len(progression)) - 1
    correct_answer = str(progression[puzzled_item])
    dots = '..'
    progression[puzzled_item] = dots
    progression = ' '.join([str(i) for i in progression])

    return progression, correct_answer


def get_question_and_answer():
    """Brain Progression game logic"""
    progression, correct_answer = convert_progression()
    question = f'Question: {progression}'

    return question, correct_answer
