#!/usr/bin/python3
def number_of_lines(filename=""):
    """Counts number of lines
        Args:
            filename (str): name of the file
    """
    lines = 0
    with open(filename) as filie:
        for linie in filie:
            lines += 1
        return lines
