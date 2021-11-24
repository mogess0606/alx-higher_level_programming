#!/usr/bin/python3
# 0-square_matrix_simple.py
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x ** 2, i))for i in matrix])
