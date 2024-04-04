from cell import Cell
from random import shuffle

def generate_maze(size):
    cells = []
    for row_no in range(size):
        row = []
        for col_no in range(size):
            row.append(Cell(row_no, col_no))
        cells.append(row)
    
    explored = [[0 for _ in range(size)] for _ in range(size)]

    def not_explored(__cell: Cell):
        return (0 <= __cell.x < size) and (0 <= __cell.y < size) and not explored[__cell.y][__cell.x]
    
    def valid_coords(x,y):
        return 0 <= x < size and 0 <= y < size
    
    def explore(__cell: Cell):
        dirs = ["up", "right", "down", "left"]
        shuffle(dirs)
        for chosen_dir in dirs:
            vec_dirs = {"up":(0,-1),"down":(0,1),"left":(-1,0),"right":(1,0)}
            
            adj_cellx = __cell.x + vec_dirs[chosen_dir][0]
            adj_celly = __cell.y + vec_dirs[chosen_dir][1]
            
            if valid_coords(adj_cellx, adj_celly): # if adj_cell has valid coords, initialise and go on
                adj_cell = cells[adj_celly][adj_cellx]
            else: 
                continue
            
            # if adj cell is valid, then break wall
            if not_explored(adj_cell):

                # break_walls in that direction for that cell and the opposite direction for the adjacent cell
                opposite_dirs = {"up":"down","down":"up","left":"right","right":"left"}

                eval(f"__cell.break_{chosen_dir}_wall()")
                eval(f"adj_cell.break_{opposite_dirs[chosen_dir]}_wall()")

                # mark the adjacent cell as explored
                explored[adj_cell.y][adj_cell.x] = 1
                explore(adj_cell)
        
    start_cell = cells[0][0]
    explore(start_cell)
    return cells


generate_maze(10)