#!/usr/bin/python3

"""Island function"""


def island_perimeter(grid):
    """_summary_

    Args:
        grid (2D array): list of list of integers

    Returns:
        int: perimeter of the island
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter
