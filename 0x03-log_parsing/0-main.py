#!/usr/bin/python3
"""Log parsing"""


import sys


def compute_statistics():
    """Reads stdin line by line and computes metrics."""
    
    total_size = 0
    status_counts = {}

    try:
        for line_num, line in enumerate(sys.stdin, start=1):
            # Parse the line
            parts = line.strip().split()
            if len(parts) < 7:
                continue
            
            ip_address = parts[0]
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update total file size
            total_size += file_size

            # Update status code counts
            if status_code.isdigit():
                status_counts.setdefault(int(status_code), 0)
                status_counts[int(status_code)] += 1

            # Print statistics every 10 lines
            if line_num % 10 == 0:
                print("File size:", total_size)
                for code in sorted(status_counts):
                    print(code, ":", status_counts[code])

        # Print final statistics
        print("File size:", total_size)
        for code in sorted(status_counts):
            count = status_counts[code]
            print(f"{code}: {count}")

    except KeyboardInterrupt:
        # Handle keyboard interrupt (CTRL + C)
        pass

if __name__ == '__main__':
    compute_statistics()
