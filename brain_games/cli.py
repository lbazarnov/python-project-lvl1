import prompt
from random import randint


def get_user_name():
    """Prompt user for his name"""
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def get_user_answer():
    """Prompt user for his answer"""
    return prompt.string('Your answer: ')


def welcome_user():
    """Asks user for his name and greets him"""
    user_name = get_user_name()
    greeting = f'Hello, {user_name}!'
    print(greeting)
    return user_name


def generate_number():
    """Generates random number in range of 1 to 100"""
    first_number = 1
    last_number = 100
    return randint(first_number, last_number)


def check_answer(user_answer, correct_answer, user_name, game_round):
    """Checks user's answer"""
    if user_answer == correct_answer:
        message = 'Correct!'
        print(message)
        game_round += 1
        if game_round == 3:
            print(f'Congratulations, {user_name}!')
        return game_round
    else:
        message = f"""'{user_answer}' is wrong answer ;(.
        \nCorrect answer was '{correct_answer}'."""
        print(message)
        game_round = 3
        return game_round
