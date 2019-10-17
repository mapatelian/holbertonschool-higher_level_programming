#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """Read n lines of a text file
        Args:
            filename (str): name of the file to be read
            nb_lines: number of lines to read
    """
    lines = 0
    linesread = 0

    with open(filename, encoding='utf-8') as filie:
        for linie in filie:
            lines += 1

    if nb_lines == 0 or nb_lines is None or nb_lines > lines:
        nb_lines = lines

    with open(filename, encoding='utf-8') as filie:
        for linie in filie:
            print(linie, end='')
            linesread += 1
            if linesread == nb_lines:
                break
