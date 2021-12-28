import prompt
from random import randint

ROUNDS_TOTAL = 3
START = 1
FINISH = 100


def generate_number():
    """Generates random number in range of 1 to 100"""
    return randint(START, FINISH)


def check_answer(user_answer, correct_answer, user_name, game_round):
    """Checks user's answer"""
    if user_answer == correct_answer:
        message = 'Correct!'
        print(message)
        game_round += 1
        if game_round == ROUNDS_TOTAL:
            print(f'Congratulations, {user_name}!')
        return game_round
    else:
        message = f"""'{user_answer}' is wrong answer ;(.
        \nCorrect answer was '{correct_answer}'.
        \nLet's try again, {user_name}!"""
        print(message)
        game_round = ROUNDS_TOTAL
        return game_round


def start_game(game):
    """Runs a selected game"""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    greeting = f'Hello, {user_name}!'
    print(greeting)
    print(game.DESCRIPTION)
    game_round = 0
    while game_round < ROUNDS_TOTAL:
        question, correct_answer = game.get_question_and_answer()
        print(question)
        user_answer = prompt.string('Your answer: ')
        game_round = check_answer(
            user_answer, correct_answer, user_name, game_round)
