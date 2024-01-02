#!/usr/bin/python3


"""Method that determines if a given data set
represents a valid UTF-8 encoding"""


def validUTF8(data):
    """_summary_

    Args:
        data (int): integer numbers

    Returns:
        boolean: True or false depending on if valid or not
    """
    n_byte = 0

    for num in data:
        binary = format(num, '#010b')[-8:]
        if n_byte == 0:
            for bit in binary:
                if bit == '0':
                    break
                n_byte += 1
            if n_byte == 0:
                continue
            if n_byte > 4 or n_byte == 1:
                return False
        else:
            if not (binary[0] == '1' and binary[1] == '0'):
                return False
        n_byte -= 1

    return n_byte == 0
