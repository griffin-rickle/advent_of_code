import util


def search(ary: list[int], index: int) -> int:
    cell_val = ary[index]
    counter = index - 1
    while counter >= 0:
        if ary[counter] >= cell_val:
            return False
        counter -= 1
    return True


def is_visible(row_idx: int, col_idx: int, grid: list[list[int]]) -> list[list[int]]:
    if search(grid[row_idx], col_idx) is True or search(grid[row_idx][::-1], len(grid[row_idx]) - col_idx - 1) is True or search([row[col_idx] for row in grid], row_idx) is True or search([row[col_idx] for row in grid][::-1], len(grid) - row_idx - 1) is True:
        return 1
    else:
        return 0


def get_visible_map(grid: list[list[int]]) -> list[list[int]]:
    mapped_grid: list[list[int]] = []
    for row_idx, row in enumerate(grid):
        visible_row: list[int] = []
        for col_idx, cell in enumerate(row):
            visible_row.append(is_visible(row_idx, col_idx, grid))
        mapped_grid.append(visible_row)
    return mapped_grid

lines = util.get_day_input(8)
grid = [[*line] for line in lines]
grid = [[int(cell) for cell in row] for row in grid]

base_visible = len(grid) * len(grid[0])
print(sum([sum([cell for cell in row]) for row in get_visible_map(grid)]))
# print(get_visible_map(grid))
