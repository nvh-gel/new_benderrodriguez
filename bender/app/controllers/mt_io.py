""" Handling I/O and logging """
import logging
# import sys

def print_err(message):
    """ print message to console and log to file """
    # print(message, file=sys.stderr)
    # app_logger = logging.getLogger()
    logging.error(message)
    return True


def print_info(message):
    """ print access info message to console and log file """
    # print(message, file=sys.stdout)
    logging.info(message)
    return True
