#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Standard imports
#
from math import ceil
import textwrap

#
# Third party imports
#

#
# Project imports
#

#
# Functions
#


def limit_char(source_file_to_be_listed):
    """

        Args:
            source_file_to_be_listed: source file to be turn into a list and limited to 80 characters per line

        Returns:
            limited-list

    """

    source = open(source_file_to_be_listed, 'r')
    text = source.read()
    limited_list = textwrap.wrap(text, 80)

    return limited_list


def check_double_spaces(list_spaces_to_be_checked):
    """

        Args:
            list_spaces_to_be_checked: list with potential double spaces to line break

        Returns:
            str_spaces_checked: string with no double spaces

    """

    str_spaces_checked = ""
    double_space = 0

    for line in list_spaces_to_be_checked:
        for char in line:
            if char == ' ':
                if double_space == 1:
                    str_spaces_checked += '\n'
                    double_space = 0
                else:
                    str_spaces_checked += char
                    double_space += 1
            else:
                str_spaces_checked += char
                double_space = 0
        str_spaces_checked += '\n'

    return str_spaces_checked


def calculate_spaces(str_with_no_justification):
    """

        Args:
            str_with_no_justification: base string to calculate the number of spaces we need

        Returns:
            None
            #justified_str: string justified with the right number of spaces in each line

    """
    dest = open('justified_text.txt', 'w')

    number_of_char_needed = 80
    listed = str_with_no_justification.split('\n')

    for entry in listed:
        initial_number_of_char = len(entry)
        print(initial_number_of_char)

        # we need to know how many words there are in entries containing less than 80 char
        if initial_number_of_char < number_of_char_needed:
            number_of_words = 1
            for char in entry:
                if char == ' ':
                    number_of_words += 1
            number_of_spaces = number_of_words - 1

            # we calculate how many spaces we need to get a 80 char line
            spaces_needed = number_of_char_needed - initial_number_of_char
            spaces_recurrence = ceil(spaces_needed / number_of_words)
            spaces_distribution = spaces_needed % number_of_words

            justified_str = add_spaces(entry, spaces_recurrence, spaces_distribution)
            dest.write(justified_str)
            dest.write('\n')
            print(justified_str)
        else:
            justified_str = entry
            dest.write(justified_str)
            dest.write('\n')
            print(justified_str)


def add_spaces(entry_to_be_justified, number_of_spaces_recurrence, number_of_spaces_distribution):
    """

        Args:
            entry_to_be_justified: entry from a list < 80 characters to be justified
            number_of_spaces_recurrence: number of spaces needed
            number_of_spaces_distribution:

        Returns:
            entry_justified: new entry with 80 characters

    """

    entry_justified = ""
    i = 0
    spaces = 0
    once_a_half = 0

    for char in entry_to_be_justified:
        if char == ' ' and i < number_of_spaces_distribution:
            entry_justified += char
            if once_a_half % 2 == 0:
                while spaces < number_of_spaces_recurrence:
                    entry_justified += ' '
                    spaces += 1
                spaces = 0
                i += 1
                once_a_half = 1
            else:
                once_a_half = 0
        else:
            entry_justified += char
    return entry_justified


def main(source):
    limited_list = limit_char(source)
    spaces_check = check_double_spaces(limited_list)
    calculate_spaces(spaces_check)


source_file = input("Nom de ton fichier source : ")

main(source_file)
exit()
