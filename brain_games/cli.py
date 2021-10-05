from brain_games.engine import get_user_name


def welcome_user():
    """Asks user for his name and greets him"""
    user_name = get_user_name()
    greeting = f'Hello, {user_name}!'
    print(greeting)
    return user_name
