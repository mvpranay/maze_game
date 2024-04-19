from constants import *
import pygame

class Player:
    def __init__(self, start_row=0, start_col=0, end_row=N_CELLS-1, end_col=N_CELLS-1):
        self.row = start_row
        self.col = start_col
        self.end_row = end_row
        self.end_col = end_col

        # load images
        self.imgs = []

        for i in range(8):
            img = pygame.image.load(f'imgs/{str(i)}.png')
            img = pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE))
            self.imgs.append(img)
        
        self.image = self.imgs[0]

        self.moving = False
        self.moving_direction = None
        self.move_tick = 0

    def update(self):
        if self.moving:
            if self.move_tick == len(self.imgs):
                # animation ends here, based on moving_direction update the coords of the player in the maze
                if self.moving_direction == "right":
                    self.col += 1
                elif self.moving_direction == "left":
                    self.col -= 1
                elif self.moving_direction == "up":
                    self.row -= 1
                elif self.moving_direction == "down":
                    self.row += 1
                    
                self.moving = False
                self.moving_direction = None
                self.move_tick = 0
                self.image = self.imgs[0]
                return
            
            # animation in progress, set image and increase move_tick
            self.image = self.imgs[self.move_tick]
            self.move_tick += 1
        else:
            self.image = self.imgs[0]

    def isMoving(self):
        return self.moving
    
    def getMoveTick(self):
        return self.move_tick
    
    def getMovingDirection(self):
        return self.moving_direction

    def move_right(self):
        self.moving = True
        self.moving_direction = "right"

    def move_left(self):
        self.moving = True
        self.moving_direction = "left"

    def move_up(self):
        self.moving = True
        self.moving_direction = "up"
    
    def move_down(self):
        self.moving = True
        self.moving_direction = "down"

    def completed_maze(self):
        return self.row == self.end_row and self.col == self.end_col
