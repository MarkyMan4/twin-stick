class Player:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    SPEED = 1.75

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def move(self, direction):
        if direction == self.UP:
            self.y -= self.SPEED
        if direction == self.RIGHT:
            self.x += self.SPEED
        if direction == self.DOWN:
            self.y += self.SPEED
        if direction == self.LEFT:
            self.x -= self.SPEED
