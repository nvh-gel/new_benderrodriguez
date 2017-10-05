""" Handling I/O and logging """
import sys


def print_stderr(message):
    """ print message to stderr stream """
    print(message, file=sys.stderr, flush=True)
