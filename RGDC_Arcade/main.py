# RGDC Arcade Machine Frontend

# Settings
DEBUGGING = True
FULLSCREEN = False #Fullscreen can cause errors when running games
                   #Instead, maybe set the resolution to the screen size
                   # and make the window borderless
RESOLUTION = (1280, 720)#(1280, 768)
TITLE = "RGDC Arcade Machine"

# Start pygame
import pygame
pygame.init()
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

# Create the display window
screen = None
print("pygame.display.get_driver(): " + str(pygame.display.get_driver()))
print("pygame.display.Info(): " + str(pygame.display.Info()))
screen = None
if FULLSCREEN:
    screen = pygame.display.set_mode(RESOLUTION, FULLSCREEN)
else:
    screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# Import scripts, modules, and packages
import os, sys
from packages.untangle.untangle import parse as UntangleXML
from scripts.machineStates import MachineState
from scripts.xml import ReadGameData

# Import screens
import scripts.screens.intro
LoadingScreen = scripts.screens.intro.LoadingScreen(pygame, RESOLUTION)
LoadingScreen.draw(screen)
LoadingScreen.print("Loaded intro screen")
import scripts.screens.home
HomeScreen = scripts.screens.home.HomeScreen(pygame, RESOLUTION)
LoadingScreen.print("Loaded game selection screen")
import scripts.screens.screensaver
Screensaver = scripts.screens.screensaver.Screensaver(pygame, RESOLUTION)
LoadingScreen.print("Loaded screensaver")

# Variables
MACHINE_STATE = MachineState.Intro
WIDTH = RESOLUTION[0]
HEIGHT = RESOLUTION[1]

# Fonts
debuggingFont = pygame.font.SysFont('Courier', 14, True, False)

# Get game information
LoadingScreen.print("Gathering game metadata...")
games = []
try:
    for path in os.listdir('games'):
        LoadingScreen.print("Loading metadata from path: /games/" + path + "...")
        newGameData = ReadGameData(UntangleXML, path)
        if newGameData is not None:
            thumbnailFilePath = "games/" + newGameData["Meta"]["Folder Name"] + "/game/" + newGameData["FilePaths"]["Thumbnail"]
            newGameData["Images"]["Thumbnail"] = pygame.image.load(thumbnailFilePath)
            games.append({
                'Path': path,
                'Data': newGameData
                })
            LoadingScreen.print("Loaded metadata for game: " + newGameData["Meta"]["Title"])
except:
    print("[ERROR] Couldn't load game metadata: " + ' /// '.join((str(errorInfo) for errorInfo in sys.exc_info())))
LoadingScreen.print("Finished gathering game metadata")

# Add a button for each game
for i in range(len(games)):
    HomeScreen.addScrollwheelButton(games[i]["Data"], i, len(games))

# Start the main loop
LoadingScreen.print("Starting arcade machine...")
running = True
while running:
    #
    for event in pygame.event.get():
        # When pygame receives a QUIT event, exit the main loop
        if event.type == pygame.QUIT:
            running = False

        # When pygame receives a KEYDOWN or KEYUP event, send it to the current screen
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            try:
                keyDirection = "up"
                if event.type == pygame.KEYDOWN:
                    keyDirection = "down"
                if MACHINE_STATE == MachineState.Intro:
                    LoadingScreen.keyPress(keyDirection, event.key)
                elif MACHINE_STATE == MachineState.Home:
                    HomeScreen.keyPress(keyDirection, event.key)
                elif MACHINE_STATE == MachineState.Screensaver:
                    Screensaver.keyPress(keyDirection, event.key)
            except:
                print("[ERROR] Received event pygame.KEYDOWN or pygame.KEYUP, but there was an error passing event.key to current screen /// " + ' /// '.join((str(errorInfo) for errorInfo in sys.exc_info())))


    # Background - this should be overridden in each screen's draw() method
    screen.fill((0, 0, 255))
    blueScreenText = debuggingFont.render("RIT Game Development Club Arcade Machine", True, (255, 255, 255))
    screen.blit(blueScreenText, [WIDTH - blueScreenText.get_rect().width, 0])
    blueScreenText = debuggingFont.render("(c) 2016", True, (255, 255, 255))
    screen.blit(blueScreenText, [WIDTH - blueScreenText.get_rect().width, 16])

    # Run the current screen's update and draw code
    try:
        if MACHINE_STATE == MachineState.Intro:
            finishedLoading = LoadingScreen.update()
            if finishedLoading: MACHINE_STATE = MachineState.Home
            else: LoadingScreen.draw(screen)
        elif MACHINE_STATE == MachineState.Home:
            userQuit = HomeScreen.update()
            if userQuit:
                break
            HomeScreen.draw(screen)
        elif MACHINE_STATE == MachineState.Screensaver:
            Screensaver.update()
            Screensaver.draw(screen)
    except:
        print("[ERROR] " + ' /// '.join((str(errorInfo) for errorInfo in sys.exc_info())))

    # Show debugging information
    if DEBUGGING:
        screen.blit(debuggingFont.render("MACHINE_STATE: " + str(MACHINE_STATE), True, (0, 255, 0)), [0, 0])
        screen.blit(debuggingFont.render("len(games): " + str(len(games)), True, (0, 255, 0)), [0, 16])

    # Update screen
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

# Main loop stopped running, stop pygame
pygame.quit()
