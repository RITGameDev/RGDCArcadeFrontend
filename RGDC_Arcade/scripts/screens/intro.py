# RGDC Arcade Machine Frontend
# Intro/Loading screen

import random

class LoadingScreen(object):
    # Initialize
    def __init__(self, pygame, resolution):
        # Get resolution
        WIDTH = resolution[0]
        HEIGHT = resolution[1]

        # Attributes
        self.name = "Loading"
        self.pygame = pygame
        self.resolution = resolution
        self.loadTime = pygame.time.get_ticks()
        
        # RGDC logo
        self.logo = pygame.image.load("images/rgdc.png")
        self.logoRect = self.logo.get_rect()

        # Console
        numberOfConsoleLines = 10
        self.console = [pygame.font.SysFont('Courier', 14, True, False).render("", True, (255, 255, 255)) for i in range(numberOfConsoleLines)]
        
        # Tell user that the arcade machine is starting to load
        self.print("Loading RGDC Arcade Machine...")

    # Game logic
    def update(self):
        # Clear console over several frames
        self.print("")

        # Go to the game selection screen after 500 milliseconds
        return self.pygame.time.get_ticks() - self.loadTime >= 500

    # Draw things
    def draw(self, screen):
        # Get resolution
        WIDTH = self.resolution[0]
        HEIGHT = self.resolution[1]

        # Draw RGDC logo
        screen.blit(self.logo, [
            (WIDTH / 2) - (self.logoRect.width / 2),
            (HEIGHT / 2) - (self.logoRect.height / 2)
            ])

        # Draw console
        for i in range(len(self.console)):
            screen.blit(self.console[i], [0, HEIGHT - (i + 1) * 16])

    # Print something to the on-screen console
    def print(self, txt):
        # Move lines up
        for i in range(len(self.console) - 1):
            index = len(self.console) - i - 1
            self.console[index] = self.console[index - 1]

        # Print blank line
        if txt == "" or txt == None:
            self.console[0] = self.pygame.font.SysFont('Courier', 14, True, False).render("", True, (255, 255, 255))

        # Print information
        else:
            print("[" + self.name + "] " + str(txt))
            self.console[0] = self.pygame.font.SysFont('Courier', 14, True, False).render(str(txt), True, (255, 255, 255))
