
class Paddle(object):
    def __init__(self, color, position):
        self.color = color
        self.size = (18, 100)
        self.position = position
        self.velocity = 0

    def accelerate(self, amount):
        self.velocity += amount

    def friction(self):
        self.velocity *= 0.97

    def move(self):
        self.position = (self.position[0], self.position[1] + self.velocity)
