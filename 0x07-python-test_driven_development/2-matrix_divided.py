#!/usr/bin/python3
"""Defining a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Return new matrix containing the elements of `matrix` divided by `div`.

    Args:
        matrix (list): A 2-D list of ints or  floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If matrix is not a list contains non-integers nor floats.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    """
    if(not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    row1 = matrix[0]
    if not all(len(row) == len(row1) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
