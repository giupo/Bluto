# -*- coding: utf-8 -*-

def yes_or_no():
    """Helper function to handle user input for yes or no"""
    while True:
        user_input = input('Y|N: ')
        answer = user_input.lower()
        if answer not in ('y', 'yes', 'n', 'no'):
            print(f"\nOptions are yes|no or y|n, Not '{user_input}'")
        else:
            return answer in ('y', 'yes')
