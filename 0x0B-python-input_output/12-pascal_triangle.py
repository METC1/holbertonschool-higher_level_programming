#!/usr/bin/python3
"""
Calculates pascal triangle of n levels
"""


def pascal_triangle(n):
    """
    Function that returns a list of integers representing
    the Pascal's triangle of n levels
    """

    pascal_triangle = []
    if n > 0:
        for rows in range(0, n):
            row = []
            for cell in range(0, rows + 1):
                if cell == 0 or cell == rows:
                    row.append(1)
                else:
                    prev_row = pascal_triangle[rows - 1]
                    cell_calc = prev_row[cell - 1] + prev_row[cell]
                    row.append(cell_calc)
            pascal_triangle.append(row)
    return pascal_triangle
