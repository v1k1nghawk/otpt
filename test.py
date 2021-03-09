#!/usr/bin/env python
##############################
# File name: test.py
#
# Purpose:
#   Test program that tries to open a file
#   without notification about what particular
#   file it is trying to open
#
# Args:
#   1 - file path
#
# Programmer: Andrew Art
# Last modified date: 09.03.2021
##############################

###############INCLUDE

import signal
import sys
import time


###############FUNCS

def interrupt_handler(sig, frame):
    """
    Handles termination signal
    """
    print("Script " + sys.argv[0] + " has been terminated")
    sys.exit(0)


def FileCheck(fn):
    """
    Tries to open a file

    Args:
        fn - file path (string)

    Returns:
        Returns 1 if file successfully opened
                0 if failed
    """
    try:
        open(fn, "r")
        return 1
    except IOError:
        print("Error: File does not exist.")
        return 0


###############MAIN

# Apply handler to interrupt signal
signal.signal(signal.SIGINT, interrupt_handler)

print("Script name: ", sys.argv[0])

# Params analyzing
if len(sys.argv) < 2:
    print("Warning: Script did not get filename.")
    sys.exit(0)

file_name = sys.argv[1]

# Infinite loop of trying to open file
while True:
    open_res = FileCheck(file_name)
    print("open result: ", open_res)
    time.sleep(7.5)

