#!/usr/bin/python3
"""Log parsing"""


import sys


def compute_statistics():
    """Reads stdin line by line and computes metrics."""
    total_size = 0
    status_counts = {}

    try:
        for line_num, line in enumerate(sys.stdin, start=1):
            parts = line.strip().split()
            if len(parts) < 7:
                continue
            
            ip_address = parts[0]
            status_code = parts[-2]
            file_size = int(parts[-1])

            total_size += file_size

            if status_code.isdigit():
                status_counts.setdefault(int(status_code), 0)
                status_counts[int(status_code)] += 1

            if line_num % 10 == 0:
                print("File size:", total_size)
                for code in sorted(status_counts):
                    print(code, ":", status_counts[code])

    except KeyboardInterrupt:
        pass

    print("File size:", total_size)
    for code in sorted(status_counts):
        print(code, ":", status_counts[code])

if __name__ == '__main__':
    compute_statistics()
