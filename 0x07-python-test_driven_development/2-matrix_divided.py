#!/usr/bin/python3
def matrix_divided(matrix, div):
    lenMat = len(matrix)
    len1st = len(matrix[0])
    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise ("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if lenMat <= 1:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(lenMat):
        if len(matrix[i]) <= 1:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[i]) != len1st:
            raise TypeError("Each row of the matrix must have the same size")
        for k in matrix[i]:
            if isinstance(k, int) is False and isinstance(k, float) is False:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(k / 3, 2) for k in i] for i in matrix]
