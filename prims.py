from random import choice, shuffle
from cell import Cell

def prims(size):

    vec_dirs = {"up":(-1,0),"down":(1,0),"right":(0,1),"left":(0,-1)}
    opp_dirs = {"up":"down","down":"up","left":"right","right":"left"}

    cells = []
    for row_no in range(size):
        row = []
        for col_no in range(size):
            row.append(Cell(row_no, col_no))
        cells.append(row)

    V = []
    V.append(cells[0][0])

    def valid_coords(row, col):
        return 0 <= row < size and 0 <= col < size
    
    # set of cells not currently in V, but adjacent to cells in V
    def find_frontier(V):
        cell_coords = [(cell.row,cell.col) for cell in V]
        shuffle(cell_coords)

        # also store in what direction was the cell found in 
        frontier = {}
        
        for coords in cell_coords:

            row,col = coords
            for vec_dir in vec_dirs.keys():

                adj_row = row + vec_dirs[vec_dir][0]
                adj_col = col + vec_dirs[vec_dir][1]

                # if the adjacent cell is valid and not in V, 
                # add it to frontier along with the direction it was found in
                if valid_coords(adj_row, adj_col) and (adj_row,adj_col) not in cell_coords:
                    adj_cell = cells[adj_row][adj_col]
                    frontier[adj_cell] = vec_dir

        return frontier

    # keep doing this until frontier is empty
    frontier = find_frontier(V)
    
    while frontier != {}:
        frontier_cells = [cell for cell in frontier.keys()]
        chosen_one = choice(frontier_cells)
        dir = frontier[chosen_one]
        opp = opp_dirs[dir]

        # find coords of cell in V
        row = chosen_one.row + vec_dirs[opp][0]
        col = chosen_one.col + vec_dirs[opp][1]
        cell = cells[row][col]

        # break walls
        eval(f"chosen_one.break_{opp}_wall()")
        eval(f"cell.break_{dir}_wall()")

        # add the cell to V
        V.append(chosen_one)
        frontier = find_frontier(V)

    return cells