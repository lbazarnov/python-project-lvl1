import prompt
from random import randint

ROUNDS_TOTAL = 3
FIRST_NUMBER = 1
LAST_NUMBER = 100


def get_user_name():
    """Prompt user for his name"""
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def welcome_user():
    """Asks user for his name and greets him"""
    user_name = get_user_name()
    greeting = f'Hello, {user_name}!'
    print(greeting)
    return user_name


def get_user_answer():
    """Prompt user for his answer"""
    return prompt.string('Your answer: ')


def generate_number():
    """Generates random number in range of 1 to 100"""
    return randint(FIRST_NUMBER, LAST_NUMBER)


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
        \nCorrect answer was '{correct_answer}'.
        \nLet's try again, {user_name}!"""
        print(message)
        game_round = ROUNDS_TOTAL
        return game_round
