def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continously
        connected vertically or horizontically  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    islands = 0         # var. for the counts
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                islands += 1
                mark_islands(i, j, grid)
    return islands


def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visisted islands as in-place operation.
    """
    grid[i][j] = '#'      # one way to mark visited ones - suggestion.
    try:
        if grid[i+1][j] == 1:
            mark_islands(i+1, j, grid)
    except:
        pass
    try:
        if i > 0 and grid[i-1][j] == 1:
            mark_islands(i-1, j, grid)
    except:
        pass
    try:
        if grid[i][j+1] == 1:
            mark_islands(i, j+1, grid)
    except:
        pass
    try:
        if j > 0 and grid[i][j-1] == 1:
            mark_islands(i, j-1, grid)
    except:
        pass

