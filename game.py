import pygame
import random

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
        self.level  = level
        self.player = Player()

        self.time_elapsed = 0
        self.time_offset = pygame.time.get_ticks()
        self.MAX_TIME = MAX_TIME_ALLOWED[level]

        self.clock = pygame.time.Clock()
        self.carrots = []
        self.spawn_carrots()
        self.energy = 10
        self.energy_tick = 0

        self.total_paused = 0
        self.pause_start = None
        
    def spawn_carrot(self):
        while True:
            row = random.randint(0, N_CELLS - 1)
            col = random.randint(0, N_CELLS - 1)
            if (row, col) not in self.carrots:
                self.carrots.append((row, col))
                return

    def spawn_carrots(self):
        for i in range(N_CARROTS[self.level]):
            self.spawn_carrot()

    def check_carrot(self, row, col):
        return (row, col) in self.carrots
    
    def remove_carrot(self, row, col):
        self.carrots.remove((row, col))

    def obtain_time_offset(self):
        self.time_offset = pygame.time.get_ticks()

    def checkValidMove(self, direction):
        current_cell = self.cells[self.player.row][self.player.col]
        wall_exists = bool(eval(f"current_cell.{direction}"))
        if wall_exists:
            return False
        return True

    def update(self):
        self.update_time()
        moved = self.player.update()
        if moved:
            if self.energy_tick < MAX_ENERGY_TICKS:
                self.energy_tick += 1
            else:
                self.energy_tick = 0
                if self.energy > 0:
                    self.energy -= 1
        if self.check_carrot(self.player.row, self.player.col):
            self.remove_carrot(self.player.row, self.player.col)
            if self.energy < MAX_ENERGY:
                self.energy += 1
                self.spawn_carrot()
        
    def run(self, screen):
        self.obtain_time_offset()
        run = True
        while run:
            self.clock.tick(FPS)
            pause_rect = self.display(screen)

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
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if pause_rect.collidepoint(mouse_pos):
                        self.pause_start = pygame.time.get_ticks()
                        self.pause(screen)
                        self.total_paused += pygame.time.get_ticks() - self.pause_start
                        
            if self.completed_maze():
                return True
            
            if not self.check_time():
                return False
                      
            self.update()
    
    def update_time(self):
        self.time_elapsed = (pygame.time.get_ticks() - self.time_offset - self.total_paused) // 1000

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
                    
                    # draw walls
                    if cell.up:
                        rect = (cell_x, cell_y - WALL_THICKNESS // 2, PLAYER_VIEW_SIZE, WALL_THICKNESS)
                        # pygame.draw.rect(screen, STONE_COLOR, rect)
                        screen.blit(cell.up_wall.image, rect)
                    if cell.right:
                        rect = (cell_x + PLAYER_VIEW_SIZE - WALL_THICKNESS // 2, cell_y, WALL_THICKNESS, PLAYER_VIEW_SIZE)
                        # pygame.draw.rect(screen, STONE_COLOR, rect)
                        screen.blit(cell.right_wall.image, rect)
                    if cell.left:
                        rect = (cell_x - WALL_THICKNESS // 2, cell_y, WALL_THICKNESS, PLAYER_VIEW_SIZE)
                        # pygame.draw.rect(screen, STONE_COLOR, rect)
                        screen.blit(cell.left_wall.image, rect)
                    if cell.down:
                        rect = (cell_x, cell_y + PLAYER_VIEW_SIZE - WALL_THICKNESS // 2, PLAYER_VIEW_SIZE, WALL_THICKNESS)
                        # pygame.draw.rect(screen, STONE_COLOR, rect)
                        screen.blit(cell.down_wall.image, rect)

        gap = (PLAYER_VIEW_SIZE - PLAYER_SIZE) // 2
        # display carrots
        for row, col in self.carrots:
            cell_y = (row - start_row) * PLAYER_VIEW_SIZE
            cell_x = (col - start_col) * PLAYER_VIEW_SIZE
            if direction == "right":
                cell_x -= correction_term
            elif direction == "left":
                cell_x += correction_term
            elif direction == "up":
                cell_y += correction_term
            elif direction == "down":
                cell_y -= correction_term
            screen.blit(CARROT, (cell_x + gap, cell_y + gap, PLAYER_SIZE, PLAYER_SIZE))

        # display golden carrot
        cell_y = (self.player.end_row - start_row) * PLAYER_VIEW_SIZE
        cell_x = (self.player.end_col - start_col) * PLAYER_VIEW_SIZE
        if direction == "right":
            cell_x -= correction_term
        elif direction == "left":
            cell_x += correction_term
        elif direction == "up":
            cell_y += correction_term
        elif direction == "down":
            cell_y -= correction_term
        screen.blit(GOLDEN_CARROT, (cell_x + gap, cell_y + gap, PLAYER_SIZE, PLAYER_SIZE))

        # display player
        cell_y = (self.player.row - start_row) * PLAYER_VIEW_SIZE
        cell_x = (self.player.col - start_col) * PLAYER_VIEW_SIZE
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
        font = pygame.font.Font(None, 40)
        text = font.render(f"Time left: {self.MAX_TIME - self.time_elapsed}", True, color)
        text_rect = text.get_rect(topright=(WIDTH - 10, 10))
        screen.blit(text, text_rect)

        # display pause button 
        pause_text = font.render("Pause", True, (255, 255, 255))
        pause_rect = pause_text.get_rect(topleft=(10, 10))
        screen.blit(pause_text, pause_rect)

        # display energy
        start_x, start_y = pause_rect.topright
        energy_text = font.render(f"| Energy:", True, (255, 255, 255))
        energy_rect = energy_text.get_rect(topleft=(start_x + 10, start_y))
        screen.blit(energy_text, energy_rect)
        for i in range(self.energy):
            start_x, start_y = energy_rect.topright
            start_x += i * (FOOD_SIZE)
            screen.blit(FOOD, (start_x, start_y, FOOD_SIZE, FOOD_SIZE))

        pygame.display.update()
        return pause_rect

    def pause(self, screen):
        resume_text = pygame.font.Font(None, 100).render("Resume", True, WHITE)
        resume_rect = resume_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        resume_hovered = False

        while True:
            screen.fill(BLACK)
            screen.blit(resume_text, resume_rect)

            # Display time remaining
            F1 = (self.MAX_TIME - self.time_elapsed) / self.MAX_TIME
            F2 = self.time_elapsed / self.MAX_TIME
            green_comp = (0, F1 * 255, 0)
            red_comp = (F2 * 255, 0, 0)
            color = tuple(map(sum, zip(green_comp, red_comp)))
            time_text = pygame.font.Font(None, 60).render(f"|Time left: {self.MAX_TIME - self.time_elapsed}", True, color)
            time_rect = time_text.get_rect(topright=(WIDTH - 10, 10))
            screen.blit(time_text, time_rect)

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEMOTION:
                    if resume_rect.collidepoint(event.pos):
                        resume_text = pygame.font.Font(None, 100).render("Resume", True, (0, 255, 0))
                        resume_hovered = True
                    else:
                        resume_text = pygame.font.Font(None, 100).render("Resume", True, (255, 255, 255))
                        resume_hovered = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if resume_hovered:
                        return

            pygame.display.update()