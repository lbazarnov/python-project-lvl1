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

    random_item = randint(2, len(progression)) - 1
    correct_answer = str(progression[random_item])
    dots = '..'
    progression[random_item] = dots
    progression = ' '.join([str(i) for i in progression])

    return progression, correct_answer


def dispatch_answer():
    """Brain Progression game logic"""
    question, correct_answer = create_progression()
    question = f'Question: {question}'

    return question, correct_answer
