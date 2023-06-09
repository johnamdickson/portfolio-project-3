from time import sleep
from os import system
from termcolor import colored, cprint


def print_error_message(string, delay):
    """
    Function to print off error message with
    steps to clear screen, print in color and
    delay prior to clearing again.
    """
    system('clear')
    cprint(string, 'white', 'on_red', ['bold'])
    sleep(delay)
    system('clear')
    return


def format_data_strings(string, colour):
    """
    Function to format data points that will be
    highlighted blue for feedback to user.
    """
    return colored(string, colour, None, ['bold'])
