import random
from brain_games.scripts.brain_games import greet
from brain_games.cli import welcome_user


def math_addition(number1, number2) -> int:
    return number1 + number2


def math_subtraction(number1, number2) -> int:
    return number1 - number2


def math_multiplication(number1, number2) -> int:
    return number1 * number2


def math_division(number1, number2) -> int:
    return number1 // number2


def brain_calc(name):
    print('What is the result of the expression?')

    rounds_to_win = 3
    rounds_played = 0

    while rounds_played < rounds_to_win:

        random_list = [random.randint(1, 10), random.randint(1, 10)]
        sorted_random_list = sorted(random_list, reverse=True)

        possible_operators = ('+', '-', '*', '/')
        random_operator = random.choice(possible_operators)


        print(f'Question: {sorted_random_list[0]} {random_operator} {sorted_random_list[1]}')
        try:
            user_answer = int(input('Your answer: '))
        except ValueError:
            print('This is not an integer. Exiting the program.')
            return
        
        if random_operator == '+':
            correct_answer = math_addition(sorted_random_list[0], sorted_random_list[1])
        elif random_operator == '-':
            correct_answer = math_subtraction(sorted_random_list[0], sorted_random_list[1])
        elif random_operator == '*':
            correct_answer = math_multiplication(sorted_random_list[0], sorted_random_list[1])
        elif random_operator == '/':
            correct_answer = math_division(sorted_random_list[0], sorted_random_list[1])


        if user_answer == correct_answer:
            print('Correct!')
            rounds_played += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break

        if rounds_played == rounds_to_win:
            print(f'Congratulations, {name}!')


def main():
    greet()
    name = welcome_user() 
    brain_calc(name)


if __name__ == "__main__":
    main()