#!/usr/bin/python3

"""
Script that reads standard input line by line and computes metrics
"""

import sys


def print_status(code_dict, total_size):
    """
    Prints the computed metrics.
    :param code_dict: a dictionary containing status codes
    as keys and their count as values
    :param total_size: total size of the processed file
    """
    print("File size: {:d}".format(total_size))
    for code in sorted(code_dict.keys()):
        if code_dict[code] != 0:
            print("{}: {:d}".format(code, code_dict[code]))


# Dictionary to store count of status codes
status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
        "404": 0, "405": 0, "500": 0
        }

count = 0
total_size = 0

try:
    for line in sys.stdin:
        if count % 10 == 0 and count != 0:
            print_status(status_codes, total_size)

        items = line.split()
        count += 1

        try:
            total_size += int(items[-1])
        except ValueError:
            pass

        try:
            if items[-2] in status_codes:
                status_codes[items[-2]] += 1
        except IndexError:
            pass

    print_status(status_codes, total_size)

except KeyboardInterrupt:
    print_status(status_codes, total_size)
    raise
