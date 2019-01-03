"""Project Euler: Problem 11."""


def grid_max_adjacent_elements_product(grid, adj_size):
    """Finds max product of adjacent numbers in a grid.

    Finds max product of `adj_size` adjacent numbers in `grid`.
    Adjacency can be horizontal, vertical or diagonal (left or right).

    Args:
        `grid`: A non-empty two dimentional matrix of non-negative integers.
        `adj_size`: Positive integer value.
    Returns:
        The value of max product if greater than 0. Otherwise 0.
    Raises:
        ValueError: Invalid `adj_size` or empty `grid`.
    """
    row_size = len(grid)
    col_size = len(grid[0])
    if (adj_size > col_size and adj_size > row_size) or adj_size < 1:
        raise ValueError('Invalid input argument.')

    current_global_max = 0
    for row in range(row_size):
        for col in range(col_size):
            next_local_max = _local_max_product(grid, adj_size, row_size,
                                                col_size, row, col)
            if next_local_max > current_global_max:
                current_global_max = next_local_max
    return current_global_max


def _local_max_product(grid, adj_size, row_size, col_size, row, col):
    products = [0] * 4
    # Horizontal adjacency
    if col + adj_size <= col_size:
        products[0] = grid[row][col]
        for k in range(1, adj_size):
            products[0] *= grid[row][col + k]
    # Vertical adjacency
    if row + adj_size <= row_size:
        products[1] = grid[row][col]
        for k in range(1, adj_size):
            products[1] *= grid[row + k][col]         
    # Diagonal (\) adjacency
    if (row + adj_size <= row_size) and (col + adj_size <= col_size):
        products[2] = grid[row][col]
        for k in range(1, adj_size):
            products[2] *= grid[row + k][col + k]            
    # Diagonal (/) adjacency
    if (row + adj_size <= row_size) and (col >= adj_size - 1):
        products[3] = grid[row][col]
        for k in range(1, adj_size):
            products[3] *= grid[row + k][col - k]            

    return max(products)
