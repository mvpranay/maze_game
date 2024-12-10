from cell import Cell
from random import shuffle

def generate_maze(size):
    cells = []
    for row_no in range(size):
        row = []
        for col_no in range(size):
            row.append(Cell(row_no, col_no))
        cells.append(row)
    
    # to store if a particular cell has been visited before
    explored = [[0 for _ in range(size)] for _ in range(size)]

    def not_explored(__cell: Cell):
        return not explored[__cell.row][__cell.col]
    
    def valid_coords(row,col):
        return 0 <= row < size and 0 <= col < size
    
    def explore(__cell: Cell):
        dirs = ["up", "right", "down", "left"]
        shuffle(dirs)
        for chosen_dir in dirs:
            vec_dirs = {"up":(-1,0),"down":(1,0),"left":(0,-1),"right":(0,1)}
            
            adj_cell_row = __cell.row + vec_dirs[chosen_dir][0]
            adj_cell_col = __cell.col + vec_dirs[chosen_dir][1]
            
            # if adj_cell has valid coords, initialise and go on
            if valid_coords(adj_cell_row, adj_cell_col): 
                adj_cell = cells[adj_cell_row][adj_cell_col]
            else: 
                continue
            
            wall_exists = bool(eval(f"__cell.{chosen_dir}"))
            # if adj cell is valid and a wall exists, then break wall
            if not_explored(adj_cell) and wall_exists:

                # break_walls in that direction for that cell and the opposite direction for the adjacent cell
                opposite_dirs = {"up":"down","down":"up","left":"right","right":"left"}

                eval(f"__cell.break_{chosen_dir}_wall()")
                eval(f"adj_cell.break_{opposite_dirs[chosen_dir]}_wall()")

                # mark the adjacent cell as explored
                explored[adj_cell.row][adj_cell.col] = 1
                # print(adj_cell.row, adj_cell.col)
                explore(adj_cell)
        
    start_cell = cells[0][0]
    explored[0][0] = 1
    explore(start_cell)
    return cells
