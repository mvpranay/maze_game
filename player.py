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

    def move_right(self):
        self.col += 1

    def move_left(self):
        self.col -= 1

    def move_up(self):
        self.row -= 1
    
    def move_down(self):
        self.row += 1

    def completed_maze(self):
        return self.row == self.end_row and self.col == self.end_col
