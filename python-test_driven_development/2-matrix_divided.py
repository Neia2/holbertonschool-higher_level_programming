#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists of integers or floats): The input matrix.
        div (int or float): The divisor.

    Returns:
        list of lists of floats: The divided matrix.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    divided_matrix = []
    for row in matrix:
        divided_row = []
        for element in row:
            divided_row.append(round(element / div, 2))
        divided_matrix.append(divided_row)

    return divided_matrix