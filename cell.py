class Cell:
    def __init__(self,x,y):
        # x and y refer to cell numbers, not actual coords
        self.x = x
        self.y = y
        # store if a wall exists in a certain direction immediately or not
        self.up = True
        self.right = True
        self.down = True
        self.left = True

    def break_wall(self, up=False, right=False, down=False, left=False):
        self.up = False if up else True
        self.down = False if down else True
        self.right = False if right else True
        self.left = False if left else True

    # these functions don't care if the wall is already broken
    def break_up_wall(self):
        self.up = False

    def break_down_wall(self):
        self.down = False
    
    def break_left_wall(self):
        self.left = False

    def break_right_wall(self):
        self.right = False