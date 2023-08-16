#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new_matrix = matrix.copy()

    for c in range(len(matrix)):
        new_matrix[c] = list(map(lambda x: x**2, matrix[c]))
        return (new_matrix)
