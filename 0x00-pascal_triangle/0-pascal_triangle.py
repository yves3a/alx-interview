#!/usr/bin/python3
"""
Module that provides a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list of lists: Pascal's triangle as a list of rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
