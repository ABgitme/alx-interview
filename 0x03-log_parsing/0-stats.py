#!/usr/bin/python3
import sys
import re
# Initialize variables to track total file size and count of each status code
total_file_size = 0
status_code_counts = {
    code: 0 for code in (200, 301, 400, 401, 403, 404, 405, 500)}
# Regular expression to match the expected input format
line_pattern = re.compile(
    r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_stats():
    """
    Print the current statistics: total file size and status code counts.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


line_count = 0  # Counter to track the number of lines read

try:
    for line in sys.stdin:
        # Check if the line matches the expected format
        match = line_pattern.match(line.strip())
        if not match:
            continue  # Skip lines that don't match the expected format

        # Extract status code and file size from the matched groups
        status_code = int(match.group(1))
        file_size = int(match.group(2))

        # Update total file size and increment status code count if it's valid
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interrupt to print stats before exiting
    pass
finally:
    # Print final stats after the last line or on interrupt
    print_stats()
