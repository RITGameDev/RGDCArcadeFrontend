# RGDC Arcade Machine Frontend
# Game selection screen

scrollwheelButtonSize = [250, 100]

class HomeScreen(object):
    # Initialize
    def __init__(self, pygame, resolution):
        # Attributes
        self.name = "Home"
        self.pygame = pygame
        self.resolution = resolution

        # Scrollwheel
        self.gameButtons = [
            {
                'Position': [250, 250],
                'Target Position': [0, 0],
                'Scale': 1,
                'Target Scale': 1
            },
            {
                'Position': [350, 100],
                'Target Position': [50, 0],
                'Scale': 1.2,
                'Target Scale': 1.2
            }
        ]#use this info to draw each button in draw()
        # when the user presses up or down, change the target position and scale, and change it each frame in update()
        # make sure the left-most buttons are drawn on top (drawn last)

    # Game logic
    def update(self):
        pass

    # Draw things
    def draw(self, screen):
        # Get resolution
        WIDTH = self.resolution[0]
        HEIGHT = self.resolution[1]

        # Background
        screen.fill((0, 0, 0))

        # Scrollwheel buttons
        for i in range(len(self.gameButtons)):
            self.pygame.draw.rect(screen, (255, 255, 255), [self.gameButtons[i]["Position"][0] - (scrollwheelButtonSize[0] / 2), self.gameButtons[i]["Position"][1] - (scrollwheelButtonSize[1] / 2), scrollwheelButtonSize[0], scrollwheelButtonSize[1]])

    # Get keyboard input:
    def keyPress(self, direction, key):
        # A key was pressed down:
        if direction == "down":
            if key == self.pygame.K_UP or key == self.pygame.K_w:
                print("up")
            elif key == self.pygame.K_DOWN or key == self.pygame.K_s:
                print("down")

        # A key was released:
        else:
            pass
