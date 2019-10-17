#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file in UTF-8, prints to stdout
        Args:
            filename (str): name of the file
    """
    with open(filename, 'r', encoding='utf-8') as filie:
        for linie in filie:
            print(linie, end='')
