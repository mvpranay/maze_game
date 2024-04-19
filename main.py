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
cells = binary_tree(N_CELLS)
# cells = prims(N_CELLS)
player = Player(0,0,N_CELLS-1,N_CELLS-1)

def checkValidMove(player: Player, direction, cells):
    current_cell = cells[player.row][player.col]
    wall_exists = bool(eval(f"current_cell.{direction}"))
    if wall_exists:
        return False
    return True

def display(screen, cells, player):

    screen.fill(BLACK)
    
    # draw cells in range
    for row_no in range(N_CELLS):
        for col_no in range(N_CELLS):
            if abs(player.row - row_no) <= 5 and abs(player.col - col_no) <=  5:
                cell = cells[row_no][col_no]
                pygame.draw.rect(screen, fill_color, (col_no*CELL_WIDTH,row_no*CELL_WIDTH, CELL_WIDTH, CELL_WIDTH))
                # draw walls
                if cell.up:
                    screen.blit(cell.up_sprite.image, cell.up_sprite.rect)
                if cell.left:
                    screen.blit(cell.left_sprite.image, cell.left_sprite.rect)
                if cell.down:
                    screen.blit(cell.down_sprite.image, cell.down_sprite.rect)
                if cell.right:
                    screen.blit(cell.right_sprite.image, cell.right_sprite.rect)
    
    # draw the player
    screen.blit(player.image, player.rect)

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
