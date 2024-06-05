import random
import prompt
from brain_games.cli import welcome_user, try_again_user, congratulations_user
from brain_games.scripts.brain_games import greet
from brain_games.constants import MAX_ATTEMPTS


def arithmetic_progression(first_num, difference, n):
    progression = []
    current_item = first_num
    for _ in range(n):
        progression.append(current_item)
        current_item += difference
    return progression


def progression_remove_random_index(progression):
    if not progression:
        print('Error, progression is empty')
        return None
    
    index_to_remove = random.randint(0, len(progression) - 1)
    removed_number = progression.pop(index_to_remove)
    progression.insert(index_to_remove, '..')
    return removed_number

def format_progression(progression):
    return ' '.join(map(str, progression))

def brain_progression(name):
    game_rounds = 0
    while game_rounds < MAX_ATTEMPTS:
        random_first_num = random.randint(1, 10)
        random_difference = random.randint(1, 10)
        random_n = random.randint(5, 15)
        random_progresison = arithmetic_progression(random_first_num, random_difference, random_n)
        removed_number = progression_remove_random_index(random_progresison)
        
        question = format_progression(random_progresison)
        print(f'Question: {question}')
        user_answer = prompt.integer('Your Answer: ')


        if removed_number == user_answer:
            print('Correct!')
            game_rounds += 1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {removed_number}')
            try_again_user(name)
            break

    if game_rounds == MAX_ATTEMPTS:
        congratulations_user(name)

def main():
    greet()
    name = welcome_user()
    brain_progression(name)

if __name__ == '__main__':
    main()