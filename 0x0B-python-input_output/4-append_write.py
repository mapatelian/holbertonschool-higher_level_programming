#!/usr/bin/python3
def append_write(filename="", text=""):
    """Appends a string at the end of a UTF-8 encoded text file
        Args:
            filename (str): name of the file
            text (str): string to be appended
        Return: number of characters
    """
    with open(filename, 'a', encoding='utf-8') as filie:
        characters = filie.write(text)
    return characters
