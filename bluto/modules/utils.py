# -*- coding: utf-8 -*-

def yes_or_no():
    """Helper function to handle user input for yes or no"""
    while True:
        answer = input('Y|N: ').lower()
        if answer not in ('y', 'yes', 'n', 'no'):
            print(f"\nThe options Are yes|no Or Y|N, Not '{answer}'")
        else:
            return answer in ('y', 'yes')
