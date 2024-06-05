import prompt
import random
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def even_number(name) -> int:
    print('Answer "yes" if the number is even, otherwise answer "no"')
    try_counter = 3

    while try_counter > 0:
        random_number = random.randrange(1, 99)
        print(f'Question: {random_number}')

        correct_answer = is_even(random_number)
        user_answer = prompt.string('Your answer: ')

        if user_answer != 'yes' and user_answer != 'no':
            print('Error. Please enter answer "yes" or "no"')
            break

        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break
        try_counter -= 1

    if try_counter == 0:
        print(f"Congratulations, {name}!")


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    greet()
    name = welcome_user()
    even_number(name)


if __name__ == '__main__':
    main()
