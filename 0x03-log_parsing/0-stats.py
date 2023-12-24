#!/usr/bin/python3

"""Write a script that reads stdin line by line and computes metrics"""

import sys
import signal
import re


def signal_handler(sig, frame):
    """_summary_ : handle keyboard interrupt

    Args:
        sig (_type_): _description_
        frame (_type_): _description_
    """
    print_stats()
    sys.exit(0)


def print_stats():
    """_Print code and number of packets for it
    """
    print("Total file size: File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_codes = {str(i): 0 for i in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

try:
    for line in sys.stdin:
        match = re.search(
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP address
            r' - '
            r'\[(.*?)\]'  # date
            r' "GET /projects/260 HTTP/1.1"'
            r' (\d{3})'  # status code
            r' (\d+)',  # file size
            line
        )
        if match:
            total_size += int(match.group(4))
            if match.group(3) in status_codes:
                status_codes[match.group(3)] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
