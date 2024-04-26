from constants import *
import pygame

def getImgFromMoveTick(move_tick, direction):
    cum_sum = 0
    IMG_TICK_DICT = eval(f'IMG_TICK_DICT_{direction.upper()}')
    for img_key in sorted(IMG_TICK_DICT.keys()):
        cum_sum += IMG_TICK_DICT[img_key]
        if move_tick < cum_sum:
            return img_key

class Player:
    def __init__(self, start_row=0, start_col=0, end_row=N_CELLS-1, end_col=N_CELLS-1):
        self.row = start_row
        self.col = start_col
        self.end_row = end_row
        self.end_col = end_col

        self.image = RIGHT_IMGS[0]

        self.moving = False
        self.moving_direction = None
        self.move_tick = 0

        self.facing = "right"

    def update(self):
        if self.moving:
            max_move_ticks = eval(f'MAX_MOVE_TICKS_{self.moving_direction.upper()}')
            if self.move_tick == max_move_ticks:
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
                if self.facing == "right":
                    self.image = RIGHT_IMGS[0]
                elif self.facing == "left":
                    self.image = LEFT_IMGS[0]
                return
            
            # animation in progress, set image and increase move_tick
            if self.moving_direction == "right":
                image_list = RIGHT_IMGS
            elif self.moving_direction == "left":
                image_list = LEFT_IMGS
            elif self.moving_direction == "up":
                image_list = UP_IMGS
            elif self.moving_direction == "down":
                image_list = DOWN_IMGS

            self.image = image_list[getImgFromMoveTick(self.move_tick, self.moving_direction)]

            if self.facing == "left" and self.moving_direction != "left": # facing left but moving up or down
                img = pygame.transform.flip(self.image, flip_x=True, flip_y=False)
                self.image = img

            self.move_tick += 1
        else:
            if self.facing == "right":
                self.image = RIGHT_IMGS[0]
            elif self.facing == "left":
                self.image = LEFT_IMGS[0]

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
