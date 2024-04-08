from cell import Cell
from random import choice

def binary_tree(size):
    cells = []
    for row_no in range(size):
        row = []
        for col_no in range(size):
            row.append(Cell(row_no, col_no))
        cells.append(row)

    # carve walls in the right or down direction
    for row_no in range(size):
        for col_no in range(size):
            if row_no == size-1 and col_no == size-1:
                continue
            # carve only down 
            if col_no == size-1:
                cell = cells[row_no][col_no]
                adj_cell = cells[row_no+1][col_no]
                cell.break_down_wall()
                adj_cell.break_up_wall()
            # carve only right
            elif row_no == size - 1:
                cell = cells[row_no][col_no]
                adj_cell = cells[row_no][col_no+1]
                cell.break_right_wall()
                adj_cell.break_left_wall()
            else:
                dir = choice(["right","down"])
                if dir == "right":
                    cell = cells[row_no][col_no]
                    adj_cell = cells[row_no][col_no + 1]
                    cell.break_right_wall()
                    adj_cell.break_left_wall()
                else:
                    cell = cells[row_no][col_no]
                    adj_cell = cells[row_no+1][col_no]
                    cell.break_down_wall()
                    adj_cell.break_up_wall()
    return cells

  