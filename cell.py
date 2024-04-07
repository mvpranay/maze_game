class Cell:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        # store if a wall exists in a certain direction immediately or not
        self.up = True
        self.right = True
        self.down = True
        self.left = True

    def break_up_wall(self):
        self.up = False

    def break_down_wall(self):
        self.down = False
    
    def break_left_wall(self):
        self.left = False

    def break_right_wall(self):
        self.right = False