
import random

class Ball(object):
    def __init__(self, position):
        self.position = position
        self.oldPosition = position
        self.size = (12, 12)
        self.velocity = (0, 0)
        self.rotation = 15

    def startMoving(self):
        newVelX = -4
        if random.random() < 0.5:
            newVelX = 4
        newVelY = -6# random.randint(-3, 3)
        self.velocity = (newVelX, newVelY)

    def move(self):
        self.oldPosition = self.position
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1]
            )
