#!/usr/bin/python3
"""
This module contains the function `island_perimeter`,
which calculates the perimeter
of an island in a 2D grid
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    The grid is a 2D list where each cell can either be:
    - 0, representing water
    - 1, representing land

    The island is represented by 1's in the grid,
    and the task is to calculate
    the total perimeter of the land cells (1's),
    which is defined by the number
    of adjacent water cells (0's) or the grid boundary.

    Args:
    grid (list of list of ints): A 2D grid representing
    the map. Each element
    is either 0 (water) or 1 (land).

    Returns:
    int: The perimeter of the island.
    perimeter = 0
    """

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:  # If the cell is land
                # Check four directions: up, down, left, right
                if i == 0 or grid[i - 1][j] == 0:  # Check up
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:  # Check down
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Check left
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:  # Check right
                    perimeter += 1

    return perimeter
