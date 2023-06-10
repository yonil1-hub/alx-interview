#!/usr/bin/python3
"""Log parsing"""


import re


def parse_log_line(line):
    """
    Parses a line of an HTTP request log and extracts relevant information.

    Args:
        line (str): The line of the HTTP request log.

    Returns:
        dict: A dictionary containing the extracted information.
            Keys: 'ip', 'date', 'request', 'status_code', 'file_size'.
    """
    log_regex = (
        r'\s*(?P<ip>\d+\.\d+\.\d+\.\d+)\s*-\s*\[(?P<date>[^\]]+)\]\s*'
        r'"GET /projects/260 HTTP/1.1"\s*(?P<status_code>\d+)\s*(?P<file_size>\d+)'
    )
    match = re.match(log_regex, line)
    if match:
        return match.groupdict()
    else:
        return {}


def print_statistics(total_file_size, status_code_counts):
    """
    Prints the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (int): The total file size.
        status_code_counts (dict): A dictionary containing the counts of each status code.
            Keys: status codes, Values: count of occurrences.
    """
    print(f"File size: {total_file_size}")
    for status_code, count in sorted(status_code_counts.items()):
        print(f"{status_code}: {count}")


def update_metrics(line, total_file_size, status_code_counts):
    """
    Updates the metrics based on a line of the HTTP request log.

    Args:
        line (str): The line of the HTTP request log.
        total_file_size (int): The current total file size.
        status_code_counts (dict): A dictionary containing the counts of each status code.
            Keys: status codes, Values: count of occurrences.

    Returns:
        int: The updated total file size.
    """
    log_info = parse_log_line(line)
    if log_info:
        status_code = log_info['status_code']
        file_size = int(log_info['file_size'])
        total_file_size += file_size
        status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1
    return total_file_size


def run_log_parser():
    """
    Starts the log parser and computes the statistics.
    """
    total_file_size = 0
    status_code_counts = {}

    try:
        line_num = 0
        while True:
            line = input()
            total_file_size = update_metrics(line, total_file_size, status_code_counts)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_code_counts)

    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_code_counts)


if __name__ == '__main__':
    run_log_parser()
