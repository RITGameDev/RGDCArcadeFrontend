# Pong /// Logan G

# Settings
DEBUGGING = True
RESOLUTION = (800, 600)
TITLE = "Pong"

# Start pygame
import pygame
pygame.init()
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

# Create the display window
screen = pygame.display.set_mode(RESOLUTION)#, pygame.FULLSCREEN)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Constants
WIDTH = RESOLUTION[0]
HEIGHT = RESOLUTION[1]

# Variables
State = "Main Menu"
yourScore = 0
opponentScore = 0
enemyMoveDelay = 0.2
lastEnemyMoveTime = 0

# Objects
from paddle import Paddle
leftPaddle = Paddle((0, 128, 255), (100, HEIGHT / 2))
rightPaddle = Paddle((255, 128, 0), (WIDTH - 100, HEIGHT / 2))
from ball import Ball
ball = Ball((WIDTH / 2, HEIGHT / 2))

# Modules
import math, time

# Start the main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.scancode == 72 or event.scancode == 17: # Up / W
                if State == "Gameplay":
                    moveUp = False
            elif event.scancode == 80 or event.scancode == 31: # Down / S
                if State == "Gameplay":
                    moveDown = False
        elif event.type == pygame.KEYDOWN:
            print("event.scancode: " + str(event.scancode))
            if event.scancode == 1: # Escape
                running = False
            elif event.scancode == 72 or event.scancode == 17: # Up / W
                if State == "Gameplay":
                    moveUp = True
            elif event.scancode == 80 or event.scancode == 31: # Down / S
                if State == "Gameplay":
                    moveDown = True
            elif event.scancode == 57: # Space
                if State == "Main Menu":
                    leftPaddle.position = (leftPaddle.position[0], HEIGHT / 2)
                    rightPaddle.position = (rightPaddle.position[0], HEIGHT / 2)
                    State = "Gameplay"
                    moveUp = False
                    moveDown = False
                    ball.startMoving()

    # Background
    screen.fill((0, 0, 0))

    # Run main code
    try:
        if State == "Main Menu":
            # Show text
            headerText = pygame.font.SysFont('Arial', 28, True, False).render("P O N G", True, (255, 255, 255))
            screen.blit(headerText, [WIDTH / 2 - headerText.get_rect().width / 2, HEIGHT / 2 - 50])
            subheaderText = pygame.font.SysFont('Arial', 20, True, False).render("Press [SPACE] to play", True, (255, 255, 255))
            screen.blit(subheaderText, [WIDTH / 2 - subheaderText.get_rect().width / 2, HEIGHT / 2 + 25])
        elif State == "Gameplay":
            # Move player paddle
            if moveUp: leftPaddle.accelerate(-0.5)
            if moveDown: leftPaddle.accelerate(0.5)
            leftPaddle.friction()
            leftPaddle.move()
            if leftPaddle.position[1] < leftPaddle.size[1] / 2:
                leftPaddle.position = (leftPaddle.position[0], leftPaddle.size[1] / 2)
                leftPaddle.velocity = abs(leftPaddle.velocity)
            if leftPaddle.position[1] > HEIGHT - leftPaddle.size[1] / 2:
                leftPaddle.position = (leftPaddle.position[0], HEIGHT - leftPaddle.size[1] / 2)
                leftPaddle.velocity = -abs(leftPaddle.velocity)

            # Move AI paddle
            if time.time() - lastEnemyMoveTime >= enemyMoveDelay:
                lastEnemyMoveTime = time.time()
                rightPaddle.velocity = max(-5, min(5, (ball.position[1] - rightPaddle.position[1]) / 25))
                print(str(rightPaddle.velocity))
            rightPaddle.friction()
            rightPaddle.move()

            # Move ball
            ball.move()

            # Check collisions with walls
            if ball.position[0] < 0:
                # Opponent scores
                opponentScore += 1
                leftPaddle.position = (leftPaddle.position[0], HEIGHT / 2)
                leftPaddle.velocity = 0
                rightPaddle.position = (rightPaddle.position[0], HEIGHT / 2)
                rightPaddle.velocity = 0
                ball.position = (WIDTH / 2, HEIGHT / 2)
                ball.startMoving()
                continue
            if ball.position[0] > WIDTH:
                # You score
                yourScore += 1
                leftPaddle.position = (leftPaddle.position[0], HEIGHT / 2)
                leftPaddle.velocity = 0
                rightPaddle.position = (rightPaddle.position[0], HEIGHT / 2)
                rightPaddle.velocity = 0
                ball.position = (WIDTH / 2, HEIGHT / 2)
                ball.startMoving()
                continue
            if ball.position[1] - ball.size[1] / 2 < 0:
                # Bounce off top of screen
                ball.position = (ball.position[0], ball.size[1] / 2)
                ball.velocity = (ball.velocity[0], abs(ball.velocity[1]))
            if ball.position[1] + ball.size[1] / 2 > HEIGHT:
                # Bounce off bottom of screen
                ball.position = (ball.position[0], HEIGHT - ball.size[1] / 2)
                ball.velocity = (ball.velocity[0], -abs(ball.velocity[1]))

            # Check collisions with left paddle
            inTop = ball.position[1] + ball.size[1] / 2 >= leftPaddle.position[1] - leftPaddle.size[1] / 2
            inBottom = ball.position[1] - ball.size[1] / 2 <= leftPaddle.position[1] + leftPaddle.size[1] / 2
            inLeft = ball.position[0] + ball.size[0] / 2 >= leftPaddle.position[0] - leftPaddle.size[0] / 2
            inRight = ball.position[0] - ball.size[0] / 2 <= leftPaddle.position[0] + leftPaddle.size[0] / 2
            if inTop and inBottom and inLeft and inRight:
                # Collided with left paddle
                if ball.oldPosition[0] - ball.size[0] / 2 > leftPaddle.position[0] + leftPaddle.size[0] / 2 or ball.oldPosition[0] + ball.size[0] / 2 <= leftPaddle.position[0] - leftPaddle.size[0] / 2:
                    # Collide from the left or right
                    ball.velocity = (-ball.velocity[0], ball.velocity[1] + leftPaddle.velocity / 2)
                if ball.oldPosition[1] - ball.size[1] / 2 > leftPaddle.position[1] + leftPaddle.size[1] / 2 or ball.oldPosition[1] + ball.size[1] / 2 <= leftPaddle.position[1] - leftPaddle.size[1] / 2:
                    # Collide from the top or botton
                    ball.velocity = (ball.velocity[0], -ball.velocity[1] + leftPaddle.velocity / 2)

            # Check collisions with left paddle
            inTop = ball.position[1] + ball.size[1] / 2 >= rightPaddle.position[1] - rightPaddle.size[1] / 2
            inBottom = ball.position[1] - ball.size[1] / 2 <= rightPaddle.position[1] + rightPaddle.size[1] / 2
            inLeft = ball.position[0] + ball.size[0] / 2 >= rightPaddle.position[0] - rightPaddle.size[0] / 2
            inRight = ball.position[0] - ball.size[0] / 2 <= rightPaddle.position[0] + rightPaddle.size[0] / 2
            if inTop and inBottom and inLeft and inRight:
                # Collided with left paddle
                if ball.oldPosition[0] - ball.size[0] / 2 > rightPaddle.position[0] + rightPaddle.size[0] / 2 or ball.oldPosition[0] + ball.size[0] / 2 <= rightPaddle.position[0] - rightPaddle.size[0] / 2:
                    # Collide from the left or right
                    ball.velocity = (-ball.velocity[0], ball.velocity[1] + rightPaddle.velocity / 2)
                if ball.oldPosition[1] - ball.size[1] / 2 > rightPaddle.position[1] + rightPaddle.size[1] / 2 or ball.oldPosition[1] + ball.size[1] / 2 <= rightPaddle.position[1] - rightPaddle.size[1] / 2:
                    # Collide from the top or botton
                    ball.velocity = (ball.velocity[0], -ball.velocity[1] + rightPaddle.velocity / 2)
    except:
        print("[ERROR] " + ' /// '.join((str(errorInfo) for errorInfo in sys.exc_info())))

    # Show paddles
    pygame.draw.rect(screen, leftPaddle.color, (
        leftPaddle.position[0] - leftPaddle.size[0] / 2,
        leftPaddle.position[1] - leftPaddle.size[1] / 2,
        leftPaddle.size[0],
        leftPaddle.size[1]
        ))
    pygame.draw.rect(screen, rightPaddle.color, (
        rightPaddle.position[0] - rightPaddle.size[0] / 2,
        rightPaddle.position[1] - rightPaddle.size[1] / 2,
        rightPaddle.size[0],
        rightPaddle.size[1]
        ))

    # Draw ball
    pygame.draw.rect(screen, (255, 255, 255), (
        ball.position[0] - ball.size[0] / 2,
        ball.position[1] - ball.size[1] / 2,
        ball.size[0],
        ball.size[1]
        ))

    # Show debugging information
    if DEBUGGING:
        screen.blit(pygame.font.SysFont('Courier', 14, True, False).render("State: " + str(State), True, (0, 255, 0)), [0, 0])

    # Update screen
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

# Main loop stopped running, stop pygame
pygame.quit()
