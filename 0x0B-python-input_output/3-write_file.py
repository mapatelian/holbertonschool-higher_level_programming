#!/usr/bin/python3
def write_file(filename="", text=""):
    """Writes a string to a text file
        Args:
            filename (str): name of the file
            text (str): string to be input
    """
    with open(filename, 'w', encoding='utf-8') as filie:
        characters = filie.write(text)
    return characters
