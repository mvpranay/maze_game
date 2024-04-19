from constants import *
import pygame

class Player:
    def __init__(self, start_row, start_col, end_row, end_col):
        self.row = start_row
        self.col = start_col
        self.end_row = end_row
        self.end_col = end_col
        self.image = pygame.image.load('imgs/player.png')
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.update_rect()

    def update_rect(self):
        self.rect.center = ((self.col + 1/2)*CELL_WIDTH,(self.row + 1/2)*CELL_WIDTH)

    def move_right(self):
        self.col += 1
        self.update_rect()

    def move_left(self):
        self.col -= 1
        self.update_rect()

    def move_up(self):
        self.row -= 1
        self.update_rect()
    
    def move_down(self):
        self.row += 1
        self.update_rect()

    def completed_maze(self):
        return self.row == self.end_row and self.col == self.end_col
