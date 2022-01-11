from brain_games.engine import generate_number

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Checks a number is prime or not"""
    if number < 2:
        return False

    divisor = 2

    while divisor <= number / 2:
        if number % divisor == 0:
            return False

        divisor += 1

    return True


def get_question_and_answer():
    """Brain Prime game logic"""
    question = generate_number()

    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
