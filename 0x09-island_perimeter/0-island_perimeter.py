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

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
