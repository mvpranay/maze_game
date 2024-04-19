import pygame
from constants import * 

class Wall:
    def __init__(self, row, col, direction):
        x = col * CELL_WIDTH
        y = row * CELL_WIDTH
        if direction == "left":
            self.image = pygame.image.load("imgs/v_wall.png")
            self.image = pygame.transform.scale(self.image, (wall_thickness, CELL_WIDTH))
            self.rect = self.image.get_rect()
            self.rect.topleft=(x-wall_thickness//2,y)
        elif direction == "right":
            self.image = pygame.image.load("imgs/v_wall.png")
            self.image = pygame.transform.scale(self.image, (wall_thickness, CELL_WIDTH))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x+CELL_WIDTH-wall_thickness//2,y)
        elif direction == "up":
            self.image = pygame.image.load("imgs/h_wall.png")
            self.image = pygame.transform.scale(self.image, (CELL_WIDTH, wall_thickness))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y-wall_thickness//2)
        elif direction == "down":
            self.image = pygame.image.load("imgs/h_wall.png")
            self.image = pygame.transform.scale(self.image, (CELL_WIDTH, wall_thickness))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y+CELL_WIDTH-wall_thickness//2)
        