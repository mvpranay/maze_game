import pygame
from maze import generate_maze
from binary_tree import binary_tree
from prims import prims
from main_menu import main_menu
from end_screen import end_screen
from player import Player
from constants import *
from time import sleep

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

BG_IMAGE = pygame.image.load('imgs/possible_background.jpg')
BG_IMAGE = pygame.transform.scale(BG_IMAGE, ((N_CELLS + 2*HALF) * PLAYER_VIEW_SIZE,) * 2)
CELL_IMAGE = pygame.image.load('imgs/tile.png')
CELL_IMAGE = pygame.transform.scale(CELL_IMAGE, (PLAYER_VIEW_SIZE, PLAYER_VIEW_SIZE))

OPENING_IMAGE = pygame.image.load('imgs/opening_screen.png')
OPENING_IMAGE = pygame.transform.scale(OPENING_IMAGE, (WIDTH, HEIGHT))

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
    
    start_row = (player.row - HALF)
    start_col = (player.col - HALF)

    direction = player.getMovingDirection()
    move_tick = player.getMoveTick()
    if direction is not None:
        MAX_MOVE_TICKS = eval(f'MAX_MOVE_TICKS_{direction.upper()}')
        correction_term = move_tick / MAX_MOVE_TICKS * PLAYER_VIEW_SIZE
    else:
        correction_term = 0

    bg_x = -(start_col + HALF) * PLAYER_VIEW_SIZE
    bg_y = -(start_row + HALF) * PLAYER_VIEW_SIZE

    if direction == "right":
        bg_x -= correction_term
    elif direction == "left":
        bg_x += correction_term
    elif direction == "up":
        bg_y += correction_term
    elif direction == "down":
        bg_y -= correction_term

    # display the background
    rect = (bg_x, bg_y, BG_SIZE, BG_SIZE)
    screen.blit(BG_IMAGE, rect)
    mud_x = bg_x
    mud_y = bg_y + (HALF) * PLAYER_VIEW_SIZE
    pygame.draw.rect(screen, MUD_COLOR, (mud_x, mud_y, BG_SIZE * 2, (BG_SIZE - mud_y + bg_y) * 2))

    for row_no in range(player.row - HALF - 1, player.row + HALF + 2):
        for col_no in range(player.col - HALF - 1, player.col + HALF + 2):

            if valid_coords(row_no, col_no):

                cell = cells[row_no][col_no]
                cell_y = (row_no - start_row) * PLAYER_VIEW_SIZE
                cell_x = (col_no - start_col) * PLAYER_VIEW_SIZE

                # adjust correction based on correction term
                if direction == "right":
                    cell_x -= correction_term
                elif direction == "left":
                    cell_x += correction_term
                elif direction == "up":
                    cell_y += correction_term
                elif direction == "down":
                    cell_y -= correction_term
                
                # draw the cell
                screen.blit(CELL_IMAGE, (cell_x, cell_y, PLAYER_VIEW_SIZE, PLAYER_VIEW_SIZE))
                # pygame.draw.rect(screen, MUD_COLOR, (cell_x, cell_y, PLAYER_VIEW_SIZE, PLAYER_VIEW_SIZE))

                # draw walls
                if cell.up:
                    rect = (cell_x, cell_y - WALL_THICKNESS // 2, PLAYER_VIEW_SIZE, WALL_THICKNESS)
                    pygame.draw.rect(screen, STONE_COLOR, rect)
                    # screen.blit(cell.up_wall.image, rect)
                if cell.right:
                    rect = (cell_x + PLAYER_VIEW_SIZE - WALL_THICKNESS // 2, cell_y, WALL_THICKNESS, PLAYER_VIEW_SIZE)
                    pygame.draw.rect(screen, STONE_COLOR, rect)
                    # screen.blit(cell.right_wall.image, rect)
                if cell.left:
                    rect = (cell_x - WALL_THICKNESS // 2, cell_y, WALL_THICKNESS, PLAYER_VIEW_SIZE)
                    pygame.draw.rect(screen, STONE_COLOR, rect)
                    # screen.blit(cell.left_wall.image, rect)
                if cell.down:
                    rect = (cell_x, cell_y + PLAYER_VIEW_SIZE - WALL_THICKNESS // 2, PLAYER_VIEW_SIZE, WALL_THICKNESS)
                    pygame.draw.rect(screen, STONE_COLOR, rect)
                    # screen.blit(cell.down_wall.image, rect)

    # display player
    cell_y = (player.row - start_row) * PLAYER_VIEW_SIZE
    cell_x = (player.col - start_col) * PLAYER_VIEW_SIZE
    gap = (PLAYER_VIEW_SIZE - PLAYER_SIZE) // 2
    rect = (cell_x + gap, cell_y + gap, PLAYER_SIZE, PLAYER_SIZE)

    screen.blit(player.image, rect)
                
    pygame.display.update()

def opening_screen(screen):
    screen.fill(BLACK)
    rect = (0, 0, WIDTH, HEIGHT)
    screen.blit(OPENING_IMAGE, rect)
    pygame.display.update()
    sleep(3)
    return

def run_game(level_clicked):
    if level_clicked == "Easy":
        cells = binary_tree(N_CELLS)
    elif level_clicked == "Medium":
        cells = prims(N_CELLS)
    elif level_clicked == "Hard":
        cells = generate_maze(N_CELLS)
        
    player = Player()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and checkValidMove(player,"up",cells) and not player.isMoving():
                    player.move_up()
                elif event.key == pygame.K_DOWN and checkValidMove(player,"down",cells) and not player.isMoving():
                    player.move_down()
                elif event.key == pygame.K_LEFT and checkValidMove(player,"left",cells) and not player.isMoving():
                    player.move_left()
                elif event.key == pygame.K_RIGHT and checkValidMove(player,"right",cells) and not player.isMoving():
                    player.move_right()

        # check game over 
        if player.completed_maze():
            run = False
        player.update()
        display(screen, cells, player)
        clock.tick(FPS)
    
    return 


if __name__ == "__main__":
    opening_screen(screen)

    CONTINUE = True
    while CONTINUE:
        # main menu
        level_clicked = main_menu(screen)

        # run_game
        run_game(level_clicked)

        # end screen
        CONTINUE = end_screen(screen)
