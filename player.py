from constants import *
import pygame

def getImgFromMoveTick(move_tick):
    cum_sum = 0
    for img_index in range(1,8):
        cum_sum += IMG_TICK_DICT[img_index]
        if move_tick < cum_sum:
            return img_index

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

        self.facing = "right"

    def update(self):
        if self.moving:
            if self.move_tick == MAX_MOVE_TICKS:
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
            self.image = self.imgs[getImgFromMoveTick(self.move_tick)]
            self.move_tick += 1
        else:
            self.image = self.imgs[0]

    def isMoving(self):
        return self.moving
    
    def getMoveTick(self):
        return self.move_tick
    
    def getMovingDirection(self):
        return self.moving_direction

    def getFacingDirection(self):
        return self.facing
    
    def move_right(self):
        self.facing = "right"
        self.moving = True
        self.moving_direction = "right"

    def move_left(self):
        self.facing = "left"
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
