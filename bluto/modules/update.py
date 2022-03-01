# -*- coding: utf-8 -*-

import subprocess
import re
import sys

from termcolor import colored
from bluto.modules.utils import yes_or_no
from bluto.modules.bluto_logging import info

def updateCheck(version):
    command_check = (["pip list -o"])
    process_check = subprocess.Popen(command_check, shell=True,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT)

    output_check = process_check.communicate()[0]
    for line in output_check.splitlines():
        if 'bluto' in str(line).lower():
            new_version = re.match("Bluto\s\(.*\)\s\-\sLatest\:\s(.*?)\s\[sdist\]", line).group(1)
            info('Update Available')
            print(colored('\nUpdate Available!', 'red'), colored('{}'.format(new_version), 'green'))
            print(colored('Would you like to attempt to update?\n', 'green'))
            if yes_or_no():
                return update()

    print(colored(f"You are running the latest version: {colored(version, 'blue')}\n", "green"))


def update():
    command_check = (["pip install bluto --upgrade"])
    process_check = subprocess.Popen(command_check,
                                     shell=True,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT)

    output_check = process_check.communicate()[0]
    lines = output_check.splitlines()
    info(lines)
    if "Successfully installed" in lines[:-1]:
        print(colored('\nUpdate Successfull!', 'green'))
        sys.exit(0)
    else:
        print(colored('\nUpdate Failed, Please Check The Logs For Details', 'red'))
        sys.exit(1)
