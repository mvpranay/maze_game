import pygame
from maze import generate_maze

pygame.init()

WIDTH = 500
HEIGHT = 500
N_CELLS = 10
CELL_WIDTH = WIDTH // N_CELLS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
cells = generate_maze(N_CELLS, screen)

def display(screen, cells, n_cells):
    screen.fill(BLACK)
    for row_no in range(n_cells):
        for col_no in range(n_cells):
            # draw the upper and left wall if they exist
            if row_no == 0 and col_no == 0:
                pygame.draw.rect(screen, RED, (0,0,CELL_WIDTH,CELL_WIDTH),2)
            cell = cells[row_no][col_no]
            top_left_x = col_no * CELL_WIDTH
            top_left_y = row_no * CELL_WIDTH
            if cell.up:
                pygame.draw.line(screen, WHITE, (top_left_x,top_left_y), (top_left_x+CELL_WIDTH,top_left_y),2)
            if cell.left:
                pygame.draw.line(screen, WHITE, (top_left_x,top_left_y), (top_left_x,top_left_y+CELL_WIDTH),2)
            if cell.down:
                pygame.draw.line(screen, WHITE, (top_left_x,top_left_y+CELL_WIDTH), (top_left_x+CELL_WIDTH,top_left_y+CELL_WIDTH),2)
            if cell.right:
                pygame.draw.line(screen, WHITE, (top_left_x+CELL_WIDTH,top_left_y), (top_left_x+CELL_WIDTH,top_left_y+CELL_WIDTH),2)

    pygame.display.update()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display(screen, cells, N_CELLS)

pygame.quit()
