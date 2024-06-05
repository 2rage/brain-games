#!/usr/bin/env python3

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def congratulations_user(name):
    print(f'Congratulations, {name}!')


def try_again_user(name):
     print(f"Let's try again, {name}")
