#!/usr/bin/env python
import prompt
from random import randint

first_number = 1
last_number = 100


def main():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_number = randint(first_number, last_number)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')

        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if user_answer.lower() == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {username}")
            break
    if user_answer == correct_answer:
        print(f'Congratulations, {username}')


if __name__ == '__main__':
    main()
