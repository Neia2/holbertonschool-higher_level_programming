#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integers in a matrix.

    Args:
        matrix (list of list of int): 2-dimensional array of integers.

    Returns:
        list of list of int: New matrix with squared values.
    """
    # Criação de uma nova matriz com os valores ao quadrado
    new_matrix = [
        [element ** 2 for element in row]
        for row in matrix
    ]
    return new_matrix
