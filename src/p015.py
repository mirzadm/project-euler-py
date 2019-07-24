"""Project Euler: Problem 15"""


def update_path_count_map(start_row, start_col, path_count_map):
    """Updates map (if needed) with number of paths from coordinates to origin.

    Args:
        `start_row`, `start_col`: Coordinates. Non-negative integer.
        `path_count_map`: Dictionary of coordinate tuples to number paths.
    Returns:
        Dictionary of coordinate tuples to number paths. 
    """
    if (start_row, start_col) not in path_count_map:     
        if start_row == 0 or start_col == 0:
            path_count_map[start_row, start_col] = 1
            path_count_map[start_col, start_row] = 1

        else:
            path_count_map = update_path_count_map(
                start_row - 1, start_col, path_count_map
            )
            path_count_map = update_path_count_map(
                start_row, start_col - 1, path_count_map
            )
            total = (
                path_count_map[(start_row - 1, start_col)]
                + path_count_map[(start_row, start_col - 1)]
            )
            path_count_map[start_row, start_col] = total
            path_count_map[start_col, start_row] = total
    return path_count_map


def num_paths_in_grid(start_row, start_col):
    """A wrapper function to get number of paths for coordinates."""
    path_count_map = update_path_count_map(start_row, start_col, {})
    return path_count_map[(start_row, start_col)]
