#!/usr/bin/python3
"""
Log parser - computes metrics from log files.
"""

from sys import stdin


def print_statistics(total_size, status_counts):
    """Prints the computed statistics"""
    print(f"Total file size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{code}: {count}")


def compute_metrics():
    """Reads log lines from stdin and computes metrics"""
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    total_size = 0
    line_count = 0

    try:
        for line in stdin:
            parts = line.split()
            if line_count % 10 == 0 and line_count != 0:
                print_statistics(total_size, status_counts)

            try:
                status_code = parts[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except IndexError:
                pass

            try:
                file_size = int(parts[-1])
                total_size += file_size
            except (IndexError, ValueError):
                pass

            line_count += 1

        print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        raise


if __name__ == '__main__':
    compute_metrics()
