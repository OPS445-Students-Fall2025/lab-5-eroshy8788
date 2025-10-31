#!/usr/bin/env python3
# Author ID: eroshy

def add(number1, number2):
    try:
        # Try to convert both to integers
        result = int(number1) + int(number2)
        return result
    except Exception:
        return 'error: could not add numbers'


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        return lines
    except Exception:
        return 'error: could not read file'


if __name__ == '__main__':
    print(add(10, 5))                # works
    print(add('10', 5))              # works
    print(add('abc', 5))             # exception
    print(read_file('seneca2.txt'))  # works
    print(read_file('file10000.txt'))# exception
