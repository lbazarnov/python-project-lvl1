from brain_games.engine import generate_number
from random import randint

DESCRIPTION = 'What number is missing in the progression?'
MIN_PROGRESSION_DIFFERENCE = 2
MAX_PROGRESSION_DIFFERENCE = 5
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10


def create_progression(min_progression_length, max_progression_length,
                       progression_difference):
    """Creates arithmetic progression"""
    number = generate_number()
    progression = []
    progression_length = randint(min_progression_length, max_progression_length)
    while len(progression) < progression_length:
        progression.append(number)
        number += progression_difference

    return progression


def convert_progression(progression):
    """Converts progression to string"""
    converted_progression = ' '.join([str(i) for i in progression])

    return converted_progression


def get_question_and_answer():
    """Brain Progression game logic"""
    difference = randint(
        MIN_PROGRESSION_DIFFERENCE, MAX_PROGRESSION_DIFFERENCE)
    progression = create_progression(
        MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_DIFFERENCE, difference)
    puzzled_item = randint(2, len(progression)) - 1
    correct_answer = str(progression[puzzled_item])
    dots = '..'
    progression[puzzled_item] = dots
    progression = convert_progression(progression)
    question = f'{progression}'

    return question, correct_answer
