#!/usr/bin/python3

"""Function calculates the perimeter of an island"""

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # assuming all land cells have four sides
                perimeter += 4
                
                # check the neighbor cells and subtract shared sides
                if i > 0 and grid[i - 1][j] == 1:  # Check the cell above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check the cell to the left
                    perimeter -= 2
    
    return perimeter
