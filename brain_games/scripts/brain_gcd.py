import random
import prompt
from brain_games.constants import MAX_ATTEMPTS
from brain_games.scripts.brain_games import greet
from brain_games.cli import welcome_user, congratulations_user, try_again_user


def gcd(num1, num2):
    if num1 < num2:
        num, num2 = num2, num1
    for i in range(num2, 0, -1):
        if num1 % i == 0 and num % i == 0:
            return i


def greatest_common_divisor(name):
    print('Find the greatest common divisor of given numbers.')

    round_played = 0

    while round_played < MAX_ATTEMPTS:
        random_number1 = random.randint(1, 12)
        random_number2 = random.randint(1, 12)

        print(f'Question: {random_number1} {random_number2}')
        user_answer = prompt.integer('Your answer: ')
        right_answer = gcd(random_number1, random_number2)

        if user_answer == right_answer:
            print('Correct!')
            round_played += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}') ")
            try_again_user(name)
            break
        
    if round_played == MAX_ATTEMPTS:
        congratulations_user(name)


def main():
    greet()
    name = welcome_user()
    greatest_common_divisor(name)


if __name__ == "__main__":
    main()