"""
This command-line program opens files and counts the number of unique
characters in the file as well as in the input string..
Author: Viazovik.A
"""

import argparse
from argparse import Namespace

from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=100)
def unique_characters(text):
    if not isinstance(text, str):
        return "Invalid input, only strings expected!"
    unique_symbol = [key for (key, value) in Counter(text).items()
                     if value == 1]
    return len(unique_symbol)


def create_parser() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=argparse.FileType('r'),
                        help="Specify the file!")
    parser.add_argument("-t", "--text", type=str,
                        help="Enter a string!")
    return parser.parse_args()


def count_symbols(parameters: Namespace):
    list_of_unique_characters = []
    if parameters.file:
        list_of_unique_characters.append('file:')
        for line in parameters.file:
            list_of_unique_characters.append(str(unique_characters(line)))
    if parameters.text:
        list_of_unique_characters.append('text:')
        list_of_unique_characters.append(str(unique_characters(
            parameters.text)))
    return ' '.join(list_of_unique_characters)


def cli():
    parsed_parameters = create_parser()
    result = count_symbols(parsed_parameters)
    return result


if __name__ == '__main__':
    print(cli())