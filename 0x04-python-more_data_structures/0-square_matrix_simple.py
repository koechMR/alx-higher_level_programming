#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(
        lambda row: list(map(lambda elem: elem ** 2, row)),
        matrix
    ))
    return new_matrix
