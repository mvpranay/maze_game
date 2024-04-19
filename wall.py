import pygame
from constants import * 

class Wall:

    def __init__(self, direction):

        if direction == "left" or direction == "right":
            image = pygame.image.load("imgs/v_wall.png")
            self.image = pygame.transform.scale(image, (WALL_THICKNESS, PLAYER_VIEW_SIZE))
            
        elif direction == "up" or direction == "down":
            image = pygame.image.load("imgs/h_wall.png")
            self.image = pygame.transform.scale(image, (PLAYER_VIEW_SIZE, WALL_THICKNESS))

    