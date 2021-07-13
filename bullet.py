import math

class Bullet:
    SPEED = 4

    def __init__(self, from_x, from_y, to_x, to_y, radius):
        self.radius = radius
        self.x = from_x
        self.y = from_y
        self.x_vel, self.y_vel = self.__caclulate_x_and_y_vel(from_x, from_y, to_x, to_y)

    def __caclulate_x_and_y_vel(self, from_x, from_y, to_x, to_y):
        slope = (to_y - from_y) / (to_x - from_x)
        theta = math.atan(slope)

        x_vel = math.cos(theta) * self.SPEED
        y_vel = math.sin(theta) * self.SPEED

        if to_x < from_x:
            x_vel *= -1
            y_vel *= -1

        return x_vel, y_vel

    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel
