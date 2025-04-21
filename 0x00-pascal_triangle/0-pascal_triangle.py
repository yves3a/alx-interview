#!/usr/bin/python3

def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each row of Pascal's Triangle
    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        
        # Compute the intermediate values of the row
        for j in range(1, i):
            # Each number is the sum of the two numbers above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # End each row with a 1
        row.append(1)

        # Add the completed row to the triangle
        triangle.append(row)

    # Return the full Pascal's Triangle
    return triangle
