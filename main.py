import pygame
from maze import generate_maze
from player import Player

pygame.init()

WIDTH = 750
HEIGHT = 750
N_CELLS = 10
CELL_WIDTH = WIDTH // N_CELLS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
cells = generate_maze(N_CELLS)
player = Player(0,0,N_CELLS-1,N_CELLS-1)

def checkValidMove(player: Player, direction, cells):
    current_cell = cells[player.row][player.col]
    wall_exists = bool(eval(f"current_cell.{direction}"))
    if wall_exists:
        return False
    return True

def display(screen, cells, player):
    screen.fill(BLACK)

    # draw the start and end squares
    pygame.draw.rect(screen, pygame.Color(120,0,0), (0,0,CELL_WIDTH,CELL_WIDTH))
    pygame.draw.rect(screen, pygame.Color(0,120,0), ((N_CELLS-1)*CELL_WIDTH,(N_CELLS-1)*CELL_WIDTH,CELL_WIDTH,CELL_WIDTH))
    
    for row_no in range(N_CELLS):
        for col_no in range(N_CELLS):
            cell = cells[row_no][col_no]
            top_left_x = col_no * CELL_WIDTH
            top_left_y = row_no * CELL_WIDTH
            # draw walls
            if cell.up:
                pygame.draw.line(screen, WHITE, (top_left_x,top_left_y), (top_left_x+CELL_WIDTH,top_left_y),2)
            if cell.left:
                pygame.draw.line(screen, WHITE, (top_left_x,top_left_y), (top_left_x,top_left_y+CELL_WIDTH),2)
            if cell.down:
                pygame.draw.line(screen, WHITE, (top_left_x,top_left_y+CELL_WIDTH), (top_left_x+CELL_WIDTH,top_left_y+CELL_WIDTH),2)
            if cell.right:
                pygame.draw.line(screen, WHITE, (top_left_x+CELL_WIDTH,top_left_y), (top_left_x+CELL_WIDTH,top_left_y+CELL_WIDTH),2)
    
    # draw the player at the center of the cell
    PLAYER_RECT_WIDTH = CELL_WIDTH // 3
    player_x = (player.col + 0.5) * CELL_WIDTH
    player_y = (player.row + 0.5) * CELL_WIDTH
    pygame.draw.rect(screen, BLUE, (player_x-PLAYER_RECT_WIDTH//2,player_y-PLAYER_RECT_WIDTH//2,PLAYER_RECT_WIDTH,PLAYER_RECT_WIDTH))

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
