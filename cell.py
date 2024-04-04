class Cell:
    def __init__(self,x,y):
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
