# RGDC Arcade Machine Frontend
# Game selection screen

# Import scripts, packages, modules
import math
from .. import easing
Easing = easing.Easing()
from .. import trigonometry
Trigonometry = trigonometry.Trigonometry()
from .. import gameManager
GameManager = gameManager.GameManager
from .. import gradient

# Screen class
class HomeScreen(object):
    # Initialize
    def __init__(self, pygame, resolution):
        # Get resolution
        self.WIDTH = resolution[0]
        self.HEIGHT = resolution[1]

        # Attributes
        self.name = "Home"
        self.pygame = pygame
        self.resolution = resolution
        self.backgroundColors = [
            [1, 59, 73],
            [16, 34, 38],
            [12, 17, 18],
            [8, 54, 32],
            [17, 43, 30]
        ]
        self.currentBackgroundColorIndex = 0
        self.currentBackgroundColor = self.backgroundColors[self.currentBackgroundColorIndex]

        # Scrollwheel
        self.gameButtons = []
        self.buttonSize = [750, 300]
        self.selectedGameName = ""

    # Create a scrollwheel button
    def addScrollwheelButton(self, data, index, totalButtons):
        # Information about the button
        verticalMargin = 6
        halfwayPoint = math.ceil(totalButtons * 1.0 / 2)
        listIndex = (index + 1) - halfwayPoint
        newPosition = [self.WIDTH / 2, listIndex * (self.buttonSize[1] + verticalMargin) + (self.HEIGHT / 2)]
        newScale = 1
        if listIndex == 0:
            newScale = 1.25
            self.selectedGameName = data["Meta"]["Title"]
        newButton = {
            'Position': newPosition,
            'Target Position': newPosition,
            'Scale': newScale,
            'Target Scale': newScale,
            'Data': data,
            'Order Index': math.floor(-math.fabs(listIndex))
            }

        # Add information to the list of scrollwheel buttons
        self.gameButtons.append(newButton)

    # Change background color
    def changeBackgroundColor(self):
        self.currentBackgroundColor[0] += (self.backgroundColors[self.currentBackgroundColorIndex][0] - self.currentBackgroundColor[0]) * 0.01
        self.currentBackgroundColor[1] += (self.backgroundColors[self.currentBackgroundColorIndex][1] - self.currentBackgroundColor[1]) * 0.01
        self.currentBackgroundColor[2] += (self.backgroundColors[self.currentBackgroundColorIndex][2] - self.currentBackgroundColor[2]) * 0.01
        redEqual = abs(self.currentBackgroundColor[0] - self.backgroundColors[self.currentBackgroundColorIndex][0]) <= 0.01
        greenEqual = abs(self.currentBackgroundColor[1] - self.backgroundColors[self.currentBackgroundColorIndex][1]) <= 0.01
        blueEqual = abs(self.currentBackgroundColor[2] - self.backgroundColors[self.currentBackgroundColorIndex][2]) <= 0.01
        if redEqual and greenEqual and blueEqual:
            self.currentBackgroundColorIndex += 1
            if self.currentBackgroundColorIndex >= len(self.backgroundColors):
                self.currentBackgroundColorIndex = 0

    # Game logic
    def update(self):
        # Change background color
        self.changeBackgroundColor()

        # Change the scale and position of the buttons
        for i in range(len(self.gameButtons)):
            listIndex = (i + 1) - math.ceil(len(self.gameButtons) * 1.0 / 2)
            self.gameButtons[i]["Visible"] = math.fabs(listIndex) <= 2
            self.gameButtons[i]["Position"][0] += (self.gameButtons[i]["Target Position"][0] - self.gameButtons[i]["Position"][0]) * 0.1
            self.gameButtons[i]["Position"][1] += (self.gameButtons[i]["Target Position"][1] - self.gameButtons[i]["Position"][1]) * 0.1
            self.gameButtons[i]["Scale"] += (self.gameButtons[i]["Target Scale"] - self.gameButtons[i]["Scale"]) * 0.1

    # Draw things
    def draw(self, screen):
        # Background
        screen.fill((self.currentBackgroundColor[0], self.currentBackgroundColor[1], self.currentBackgroundColor[2]))

        # Order buttons
        minOrderIndex = 99999
        for i in range(len(self.gameButtons)):
            if self.gameButtons[i]["Order Index"] < minOrderIndex:
                minOrderIndex = self.gameButtons[i]["Order Index"]
        buttonsAtIndex = []
        for i in range(math.floor(math.fabs(minOrderIndex)) + 1):
            buttonsAtIndex.append([])
        for i in range(len(self.gameButtons)):
            buttonsAtIndex[math.floor(math.fabs(self.gameButtons[i]["Order Index"]))].append(i)
        buttonsAtIndex.reverse()
        #print(buttonsAtIndex)

        # Draw buttons
        for j in range(len(buttonsAtIndex)):
            for i in buttonsAtIndex[j]:
                # Shadow
                self.pygame.draw.rect(screen, (0, 0, 0), [
                    self.gameButtons[i]["Position"][0] - ((self.buttonSize[0] * self.gameButtons[i]["Scale"]) / 2),
                    self.gameButtons[i]["Position"][1] - ((self.buttonSize[1] * self.gameButtons[i]["Scale"]) / 2) + 2,
                    self.buttonSize[0] * self.gameButtons[i]["Scale"],
                    self.buttonSize[1] * self.gameButtons[i]["Scale"]
                    ])
                # Top
                self.pygame.draw.rect(screen, ((j + 1) * (255.0 / len(buttonsAtIndex)), (j + 1) * (255.0 / len(buttonsAtIndex)), (j + 1) * (255.0 / len(buttonsAtIndex))), [
                    self.gameButtons[i]["Position"][0] - ((self.buttonSize[0] * self.gameButtons[i]["Scale"]) / 2),
                    self.gameButtons[i]["Position"][1] - ((self.buttonSize[1] * self.gameButtons[i]["Scale"]) / 2),
                    self.buttonSize[0] * self.gameButtons[i]["Scale"],
                    self.buttonSize[1] * self.gameButtons[i]["Scale"]
                    ])
                # Game thumbnail
                tempScaledThumbnail = self.pygame.transform.scale(self.gameButtons[i]["Data"]["Images"]["Thumbnail"], (math.floor(self.buttonSize[1] * self.gameButtons[i]["Scale"] - 20), math.floor(self.buttonSize[1] * self.gameButtons[i]["Scale"] - 20)))
                screen.blit(tempScaledThumbnail, [
                    self.gameButtons[i]["Position"][0] - (self.buttonSize[0] / 2 * self.gameButtons[i]["Scale"]) + 10,
                    self.gameButtons[i]["Position"][1] - (self.buttonSize[1] / 2 * self.gameButtons[i]["Scale"]) + 10
                    ])
                # Game title
                gameTitleSurface = self.pygame.font.SysFont('Arial', 36, True, False).render(self.gameButtons[i]["Data"]["Meta"]["Title"], True, (0, 0, 0))
                screen.blit(gameTitleSurface, [
                    self.gameButtons[i]["Position"][0] - (self.buttonSize[0] / 2 * self.gameButtons[i]["Scale"]) + 10 + tempScaledThumbnail.get_width() + 10,
                    self.gameButtons[i]["Position"][1] - (self.buttonSize[1] / 2 * self.gameButtons[i]["Scale"]) + 10
                    ])
                # Game title
                gameAuthorSurface = self.pygame.font.SysFont('Arial', 18, True, False).render(self.gameButtons[i]["Data"]["Meta"]["Author"], True, (0, 0, 0))
                screen.blit(gameAuthorSurface, [
                    self.gameButtons[i]["Position"][0] - (self.buttonSize[0] / 2 * self.gameButtons[i]["Scale"]) + 12 + tempScaledThumbnail.get_width() + 10,
                    self.gameButtons[i]["Position"][1] - (self.buttonSize[1] / 2 * self.gameButtons[i]["Scale"]) + 48
                    ])

    # Get keyboard input:
    def keyPress(self, direction, key):
        # A key was pressed down:
        if direction == "down":
            rotated = False
            if key == self.pygame.K_UP or key == self.pygame.K_w:
                # Change index of all buttons
                backUpButton = self.gameButtons[len(self.gameButtons) - 1]
                for i in range(len(self.gameButtons) - 1):
                    index = len(self.gameButtons) - i - 1
                    self.gameButtons[index] = self.gameButtons[index - 1]
                self.gameButtons[0] = backUpButton
                rotated = True

            elif key == self.pygame.K_DOWN or key == self.pygame.K_s:
                # Change index of all buttons
                backUpButton = self.gameButtons[0]
                for i in range(len(self.gameButtons) - 1):
                    self.gameButtons[i] = self.gameButtons[i + 1]
                self.gameButtons[len(self.gameButtons) - 1] = backUpButton
                rotated = True

            elif key == self.pygame.K_RETURN:
                print("HI")
                # Get the selected game's metadata
                thisGameData = None
                for button in self.gameButtons:
                    if button["Data"]["Meta"]["Title"] == self.selectedGameName:
                        thisGameData = button["Data"]

                # If the metadata was found, launch the game
                if thisGameData is not None:
                    GameManager.LaunchGame(thisGameData)

            elif key == self.pygame.K_ESCAPE:
                # Quit the arcade machine
                self.pygame.quit()
                return True

            ## Rotate wheel:
            if rotated:
                # Change target position & scale of all buttons
                verticalMargin = 6
                halfwayPoint = math.ceil(len(self.gameButtons) * 1.0 / 2)
                for i in range(len(self.gameButtons)):
                    listIndex = (i + 1) - halfwayPoint
                    self.gameButtons[i]["Order Index"] = math.floor(-math.fabs(listIndex))
                    newPosition = [self.WIDTH / 2, listIndex * (self.buttonSize[1] + verticalMargin) + (self.HEIGHT / 2)]
                    self.gameButtons[i]["Target Position"] = newPosition
                    newScale = 1
                    if listIndex == 0:
                        newScale = 1.25
                        self.selectedGameName = self.gameButtons[i]["Data"]["Meta"]["Title"]
                    self.gameButtons[i]["Target Scale"] = newScale

            # Return FALSE because the user did not quit the arcade machine
            return False

        # A key was released:
        else:
            pass
