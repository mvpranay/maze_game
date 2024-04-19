import pygame
from maze import generate_maze
from binary_tree import binary_tree
from prims import prims
from player import Player
from constants import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
# cells = generate_maze(N_CELLS)    
# cells = binary_tree(N_CELLS)
cells = prims(N_CELLS)
player = Player(0,0,N_CELLS-1,N_CELLS-1)

def checkValidMove(player: Player, direction, cells):
    current_cell = cells[player.row][player.col]
    wall_exists = bool(eval(f"current_cell.{direction}"))
    if wall_exists:
        return False
    return True

def display(screen, cells, player):
    screen.fill(BLACK)

    def valid_coords(row, col):
        return 0 <= row < N_CELLS and 0 <= col < N_CELLS
    
    half = (PLAYER_VIEW_CELLS - 1) // 2
    start_row = (player.row - half)
    start_col = (player.col - half)
    # print(f"start row {start_row} start col {start_col}")
    for row_no in range(start_row, start_row + 2 * half + 1):
        for col_no in range(start_col, start_col + 2 * half + 1):

            if valid_coords(row_no, col_no):
                cell = cells[row_no][col_no]
                cell_y = (row_no - start_row) * PLAYER_VIEW_SIZE
                cell_x = (col_no - start_col) * PLAYER_VIEW_SIZE
                # draw the cell
                pygame.draw.rect(screen, fill_color, (cell_x, cell_y, PLAYER_VIEW_SIZE, PLAYER_VIEW_SIZE))
                # draw walls
                if cell.up:
                    rect = (cell_x, cell_y - WALL_THICKNESS // 2, PLAYER_VIEW_SIZE, WALL_THICKNESS)
                    screen.blit(cell.up_wall.image, rect)
                if cell.right:
                    rect = (cell_x + PLAYER_VIEW_SIZE - WALL_THICKNESS // 2, cell_y, WALL_THICKNESS, PLAYER_VIEW_SIZE)
                    screen.blit(cell.right_wall.image, rect)
                if cell.left:
                    rect = (cell_x - WALL_THICKNESS // 2, cell_y, WALL_THICKNESS, PLAYER_VIEW_SIZE)
                    screen.blit(cell.left_wall.image, rect)
                if cell.down:
                    rect = (cell_x, cell_y + PLAYER_VIEW_SIZE - WALL_THICKNESS // 2, PLAYER_VIEW_SIZE, WALL_THICKNESS)
                    screen.blit(cell.down_wall.image, rect)

    # display player
    cell_y = (player.row - start_row) * PLAYER_VIEW_SIZE
    cell_x = (player.col - start_col) * PLAYER_VIEW_SIZE
    gap = (PLAYER_VIEW_SIZE - PLAYER_SIZE) // 2
    rect = (cell_x + gap, cell_y + gap, PLAYER_SIZE, PLAYER_SIZE)
    screen.blit(player.image, rect)
                
    pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and checkValidMove(player,"up",cells):
                player.move_up()
            elif event.key == pygame.K_DOWN and checkValidMove(player,"down",cells):
                player.move_down()
            elif event.key == pygame.K_LEFT and checkValidMove(player,"left",cells):
                player.move_left()
            elif event.key == pygame.K_RIGHT and checkValidMove(player,"right",cells):
                player.move_right()

    # check game over 
    if player.completed_maze():
        print("Congrats you won!")
        run = False

    display(screen, cells, player)

pygame.quit()
