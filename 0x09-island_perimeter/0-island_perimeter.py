def island_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # For each land cell
                if r == 0 or grid[r-1][c] == 0:  # Check the cell above
                    perimeter += 1
                if r == rows-1 or grid[r+1][c] == 0:  # Check the cell below
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:  # Check the cell to the left
                    perimeter += 1
                if c == cols-1 or grid[r][c+1] == 0:  # Check the cell to the right
                    perimeter += 1

    return perimeter


