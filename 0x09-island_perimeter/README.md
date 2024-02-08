The task is asking you to write a Python function named island_perimeter that calculates the perimeter of an island in a grid. Here’s a breakdown of the requirements:

The grid is a 2D list (a list of lists) of integers, where each integer is either 0 or 1.
In this grid, 0 represents water and 1 represents land.
Each cell in the grid is a square with a side length of 1.
Cells are connected horizontally or vertically, but not diagonally.
The grid is rectangular, meaning all rows have the same number of cells (width), and all columns have the same number of cells (height). The width and height do not exceed 100.
The grid is completely surrounded by water, meaning the outermost cells are all 0s.
There is only one island (a group of 1s) or nothing (all 0s) in the grid.
The island doesn’t have “lakes”, meaning there are no 0s that are completely surrounded by 1s.