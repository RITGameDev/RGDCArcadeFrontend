# RGDC Arcade Machine Frontend

# Import modules
import math

# Trigonometry functions
class Trigonometry():
    def CalculatePosition(self, angle, hypotenuse):
        radians = math.radians(360 - angle)
        distance = [
            -math.sin(radians) * hypotenuse,
            -math.cos(radians) * hypotenuse
        ]
        return distance
