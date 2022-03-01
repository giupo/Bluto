# -*- coding: utf-8 -*-

import os
import shutil
import webbrowser

def yes_or_no():
    """Helper function to handle user input for yes or no"""
    while True:
        user_input = input('Y|N: ')
        answer = user_input.lower()
        if answer not in ('y', 'yes', 'n', 'no'):
            print(f"\nOptions are yes|no or y|n, Not '{user_input}'")
        else:
            return answer in ('y', 'yes')


def remove_reports(docs, log_dir, report_location):
    """Removes reports retrieved"""
    shutil.rmtree(docs)
    shutil.rmtree(log_dir)
    os.remove(report_location)


def handle_local_data(docs, log_dir, report_location):
    """
    helper function for interactively handle local data persistence
    """
    print("\nWould you like to keep all local data?\n")
    print("(Local Logs, Downloded Documents, HTML Evidence Report)")
    if yes_or_no():
        print(f"\nThe documents are located here: {docs}")
        print(f"The logs are located here: {log_dir}.")
        print(f"\nAn evidence report has been written to {report_location}\n")
        print("Would you like to open this report now?\n")
        if yes_or_no():
            print(f'\nOpening {report_location}')
            webbrowser.open('file://{report_location}')
    else:
        print("removing local data...")
        remove_reports(docs, log_dir, report_location)
        print("done removing local data.")
