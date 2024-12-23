from wall import Wall

class Cell:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        # store if a wall exists in a certain direction immediately or not
        self.up = True
        self.right = True
        self.down = True
        self.left = True
        # store the wall objects in each direction
        self.up_wall = Wall("up")
        self.down_wall = Wall("down")
        self.left_wall = Wall("left")
        self.right_wall = Wall("right")

    def break_up_wall(self):
        self.up = False

    def break_down_wall(self):
        self.down = False
    
    def break_left_wall(self):
        self.left = False

    def break_right_wall(self):
        self.right = False