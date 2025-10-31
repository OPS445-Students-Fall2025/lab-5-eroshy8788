#!/usr/bin/env python3
# Author ID: eroshy

def read_file_string(file_name):
    """Takes file_name as string for a file name, returns its entire contents as a string"""
    f = open(file_name, 'r')      # open file for reading
    data = f.read()               # read full content
    f.close()                     # close file
    return data                   # return as a string


def read_file_list(file_name):
    """Takes file_name as string for a file name,
    return its entire contents as a list of lines without new-line characters"""
    f = open(file_name, 'r')      # open file for reading
    lines = f.readlines()         # read all lines
    f.close()                     # close file
    cleaned_lines = [line.strip('\n') for line in lines]  # remove newline chars
    return cleaned_lines


if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
