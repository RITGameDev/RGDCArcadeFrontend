# RGDC Arcade Machine Frontend
# Screensaver screen

class Screensaver(object):
    # Initialize
    def __init__(self, pygame, resolution):
        # Get resolution
        WIDTH = resolution[0]
        HEIGHT = resolution[1]

        # Attributes
        self.name = "Loading"
        self.pygame = pygame
        self.resolution = resolution

        # RGDC logo
        self.logo = pygame.image.load("images/rgdc.png")
        self.logoRect = self.logo.get_rect()
        self.logoPosition = [
            (WIDTH / 2) - (self.logoRect.width / 2),
            (HEIGHT / 2) - (self.logoRect.height / 2)
            ]
        self.logoDirection = [2, 2]
        self.logoBounds = {
            "Left": 0,
            "Right": WIDTH - self.logoRect.width,
            "Top": 0,
            "Bottom": HEIGHT - self.logoRect.height
            }

    # Game logic
    def update(self):
        # Move logo
        self.logoPosition[0] += self.logoDirection[0]
        self.logoPosition[1] += self.logoDirection[1]

        # Bounce off walls
        if self.logoPosition[0] <= self.logoBounds["Left"]:
            self.logoPosition[0] = self.logoBounds["Left"]
            self.logoDirection[0] = 2
        elif self.logoPosition[0] >= self.logoBounds["Right"]:
            self.logoPosition[0] = self.logoBounds["Right"]
            self.logoDirection[0] = -2
        if self.logoPosition[1] <= self.logoBounds["Top"]:
            self.logoPosition[1] = self.logoBounds["Top"]
            self.logoDirection[1] = 2
        elif self.logoPosition[1] >= self.logoBounds["Bottom"]:
            self.logoPosition[1] = self.logoBounds["Bottom"]
            self.logoDirection[1] = -2

    # Draw things
    def draw(self, screen):
        # Get resolution
        WIDTH = self.resolution[0]
        HEIGHT = self.resolution[1]

        # Draw RGDC logo
        screen.blit(self.logo, self.logoPosition)
