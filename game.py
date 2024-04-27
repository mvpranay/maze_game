import pygame

from cell import Cell
from wall import Wall
from player import Player

from binary_tree import binary_tree
from prims import prims
from maze import generate_maze

from constants import *

class Game:

    def __init__(self, level, size):

        if level == "Easy":
            self.cells = binary_tree(size)
        elif level == "Medium":
            self.cells = prims(size)
        elif level == "Hard":
            self.cells = generate_maze(size)

        self.player = Player()

        self.time_elapsed = 0
        self.time_offset = pygame.time.get_ticks()
        self.MAX_TIME = MAX_TIME_ALLOWED[level]

        self.clock = pygame.time.Clock()
        
    def obtain_time_offset(self):
        self.time_offset = pygame.time.get_ticks()

    def checkValidMove(self, direction):
        current_cell = self.cells[self.player.row][self.player.col]
        wall_exists = bool(eval(f"current_cell.{direction}"))
        if wall_exists:
            return False
        return True

    def run(self, screen):
        self.obtain_time_offset()
        run = True
        while run:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.try_moving_up()
                    elif event.key == pygame.K_DOWN:
                        self.try_moving_down()
                    elif event.key == pygame.K_LEFT:
                        self.try_moving_left()
                    elif event.key == pygame.K_RIGHT:
                        self.try_moving_right()
                        
            self.update_time()

            if self.completed_maze():
                return True
            
            if not self.check_time():
                return False
                        
            self.player.update()
            self.display(screen)
    
    def update_time(self):
        self.time_elapsed = (pygame.time.get_ticks() - self.time_offset) // 1000

    def try_moving_up(self):
        if not self.player.isMoving() and self.checkValidMove("up"):
            self.player.move_up()

    def try_moving_down(self):
        if not self.player.isMoving() and self.checkValidMove("down"):
            self.player.move_down()
    
    def try_moving_left(self):
        if not self.player.isMoving() and self.checkValidMove("left"):
            self.player.move_left()

    def try_moving_right(self):
        if not self.player.isMoving() and self.checkValidMove("right"):
            self.player.move_right()

    def completed_maze(self):
        return self.player.row == self.player.end_row and self.player.col == self.player.end_col
    
    def check_time(self):
        return self.time_elapsed <= self.MAX_TIME
    
    def display(self, screen):
        screen.fill(BLACK)

        def valid_coords(row, col):
            return 0 <= row < N_CELLS and 0 <= col < N_CELLS
        
        start_row = (self.player.row - HALF)
        start_col = (self.player.col - HALF)

        direction = self.player.getMovingDirection()
        move_tick = self.player.getMoveTick()

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

        for row_no in range(self.player.row - HALF - 1, self.player.row + HALF + 2):
            for col_no in range(self.player.col - HALF - 1, self.player.col + HALF + 2):

                if valid_coords(row_no, col_no):

                    cell = self.cells[row_no][col_no]
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
        cell_y = (self.player.row - start_row) * PLAYER_VIEW_SIZE
        cell_x = (self.player.col - start_col) * PLAYER_VIEW_SIZE
        gap = (PLAYER_VIEW_SIZE - PLAYER_SIZE) // 2
        rect = (cell_x + gap, cell_y + gap, PLAYER_SIZE, PLAYER_SIZE)

        screen.blit(self.player.image, rect)
                    
        # display time left
        # (MAX - t)/MAX * GREEN + t/MAX*RED
        # F1 * GREEN + F2 * RED
        F1 = (self.MAX_TIME - self.time_elapsed) / self.MAX_TIME
        F2 = self.time_elapsed / self.MAX_TIME
        green_comp = (0, F1 * 255, 0)
        red_comp = (F2 * 255, 0, 0)
        color = tuple(map(sum, zip(green_comp, red_comp)))
        font = pygame.font.Font(None, 60)
        text = font.render(f"Time left: {self.MAX_TIME - self.time_elapsed}", True, color)
        text_rect = text.get_rect(topright=(WIDTH - 10, 10))
        screen.blit(text, text_rect)

        pygame.display.update()
