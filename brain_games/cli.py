#!/usr/bin/env python3

import prompt
from colorama import Fore
from brain_games.constants import MAX_NAME_LENGTH

def welcome_user():
    while True:
        name = prompt.string('May I have your name? ')
        if len(name) < MAX_NAME_LENGTH:
            print('Your name must be at least 4 characters long. Please try again.')
        elif name.isdigit():
            print('Your name cannot Consist only of digits. Please try again.')
        else:
            break

    print(f'Hello, {Fore.CYAN}{name}{Fore.RESET}')
    return name


def congratulations_user(name):
    print(f'Congratulations, {Fore.CYAN}{name}{Fore.RESET}!')


def try_again_user(name):
     print(f"Let's try again, {Fore.CYAN}{name}{Fore.RESET}")
