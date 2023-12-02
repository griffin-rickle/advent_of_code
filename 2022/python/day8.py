import util


def search(ary: list[int], index: int) -> int:
    if index == 0:
        return 0
    cell_val = ary[index]
    counter = index - 1
    visibility = 1
    while counter > 0:
        if ary[counter] >= cell_val:
            break
        counter -= 1
        visibility += 1
    return visibility


def get_cell_score(row_idx: int, col_idx: int, grid: list[list[int]]) -> list[list[int]]:
    s_left = search(grid[row_idx], col_idx)
    s_right = search(grid[row_idx][::-1], len(grid[row_idx]) - col_idx - 1)
    s_up = search([row[col_idx] for row in grid], row_idx)
    s_down = search([row[col_idx] for row in grid][::-1], len(grid) - row_idx - 1)

    return s_left * s_right * s_up * s_down

def get_scores(grid: list[list[int]]) -> list[list[int]]:
    mapped_grid: list[list[int]] = []
    for row_idx, row in enumerate(grid):
        visible_row: list[int] = []
        for col_idx, cell in enumerate(row):
            visible_row.append(get_cell_score(row_idx, col_idx, grid))
        mapped_grid.append(visible_row)
    return mapped_grid

lines = util.get_day_input(8)
grid = [[*line] for line in lines]
grid = [[int(cell) for cell in row] for row in grid]

print(max([max(row) for row in get_scores(grid)]))
