"""Project Euler: Problem 15"""


def num_paths_through_grid(start_row, start_col):
    if start_row == 0 and start_col == 0:
        return 0
    num_paths_map = {}
    _num_paths_through_grid(start_row, start_col, num_paths_map)
    return num_paths_map[(start_row, start_col)]


def _num_paths_through_grid(start_row, start_col, num_paths_map={}):
    if start_row == 0 or start_col == 0:
        num_paths_map[start_row, start_col] = 1
    elif (
        (start_row, start_col) not in num_paths_map
        and (start_col, start_row) not in num_paths_map
    ):
        num_paths_through_grid(start_row - 1, start_col, num_paths_map)
        num_paths_through_grid(start_row, start_col - 1, num_paths_map)
        num_paths_map[start_row, start_col] = (
            num_paths_map[(start_row - 1, start_col)]
            + num_paths_map[(start_row, start_col - 1)]
        )
