#!/usr/bin/python3
"""
Module that creates a function and returns a list of integers
"""


def pascal_triangle(n):
    """Pascal triangle"""

    triangle = []
    if n <= 0:
        return triangle

    triangle = [[1]]
    for t in range(n - 1):
        line = triangle[-1]
        aux = [1]
        for t in range(len(line) - 1):
            aux.append(line[t] + line[t + 1])
        aux.append(1)
        triangle.append(aux)
    return triangle
