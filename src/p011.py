"""Project Euler: Problem 11."""


def max_adj_prod(grid, num_of_adj):
    """Finds max product of adjacent numbers in a grid.

    Finds max product of `num_of_adj` adjacent numbers in `grid`.
    Adjacency can be horizontal, vertical or diagonal (left or right).

    Args:
        `grid`: A non-empty two dimentional matrix of non-negative integers.
        `num_of_adj`: Positive integer value.
    Returns:
        The value of max product if greater than 0. Otherwise 0.
    Raises:
        ValueError: Invalid `num_of_adj` or empty `grid`.
    """
    rows = len(grid)
    cols = len(grid[0])
    if (num_of_adj > cols and num_of_adj > rows) or num_of_adj < 1:
        raise ValueError('Invalid input argument.')

    max_product = 0
    for i in range(rows):
        for j in range(cols):
            # Horizontal adjacency
            product = grid[i][j]
            if j + num_of_adj <= cols:
                for k in range(1, num_of_adj):
                    product *= grid[i][j + k]
                if product > max_product:
                    max_product = product
            # Vertical adjacency
            product = grid[i][j]
            if i + num_of_adj <= rows:
                for k in range(1, num_of_adj):
                    product *= grid[i + k][j]         
                if product > max_product:
                    max_product = product
            # Diagonal (\) adjacency
            product = grid[i][j]
            if (i + num_of_adj <= rows) and (j + num_of_adj <= cols):
                for k in range(1, num_of_adj):
                    product *= grid[i + k][j + k]            
                if product > max_product:
                    max_product = product
            # Diagonal (/) adjacency
            product = grid[i][j]
            if (i + num_of_adj <= rows) and (j >= num_of_adj - 1):
                for k in range(1, num_of_adj):
                    product *= grid[i + k][j - k]            
                if product > max_product:
                    max_product = product

    return max_product
