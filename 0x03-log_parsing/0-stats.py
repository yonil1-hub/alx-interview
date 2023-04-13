#!/usr/bin/python3
"""
This script parses a log file and prints
the file size and status code metrics.
"""

import sys


def print_metrics(file_size, status_codes):
    """
    This function prints the file size and status code metrics.
    Args:
        file_size (int): Total file size in bytes.
        status_codes (dict): A dictionary containing counts of
        each HTTP status code.
    """
    print("File size: {}".format(file_size))
    codes_sorted = sorted(status_codes.keys())
    for code in codes_sorted:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    codes_count = {'200': 0, '301': 0, '400': 0, '401': 0,
                   '403': 0, '404': 0, '405': 0, '500': 0}
    file_size_total = 0
    count = 0

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                status_code = parts[-2]
                if status_code in codes_count:
                    codes_count[status_code] += 1
                file_size = int(parts[-1])
                file_size_total += file_size
            except Exception:
                pass

            count += 1
            if count == 10:
                print_metrics(file_size_total, codes_count)
                count = 0

    except KeyboardInterrupt:
        print_metrics(file_size_total, codes_count)
        raise

    print_metrics(file_size_total, codes_count)
