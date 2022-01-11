import prompt
from random import randint

ROUNDS_TOTAL = 3
START = 1
FINISH = 100


def generate_number():
    """Generates random number in range of 1 to 100"""
    return randint(START, FINISH)


def start_game(game):
    """Runs a selected game"""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(game.DESCRIPTION)
    for game_round in range(0, ROUNDS_TOTAL):
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            message = 'Correct!'
            print(message)
        else:
            message = f"""'{user_answer}' is wrong answer ;(.
            \nCorrect answer was '{correct_answer}'.
            \nLet's try again, {user_name}!"""
            print(message)
            break
    else:
        print(f'Congratulations, {user_name}!')
