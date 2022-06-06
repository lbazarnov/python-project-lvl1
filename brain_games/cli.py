import prompt


def welcome_user():
    """Asks user for his name and greets him"""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    greeting = f'Hello, {user_name}!'
    print(greeting)