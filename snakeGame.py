# Snake game using PyGame

import pygame
import sys, random, time

# returns tuple with (tasks completed, errors)
check_errors = pygame.init()

if check_errors[1] > 0:
	# exit
	print ("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
	sys.exit(-1)
else:
	print ("(+) PyGame successfully initialized.")

# Screen - the main window
playSurface = pygame.display.set_mode((720, 460))
# set title
pygame.display.set_caption('Snake game')

# Colors
red = pygame.Color(255, 0, 0) # gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) # score
white = pygame.Color(255, 255, 255) # background
brown = pygame.Color(165, 42, 42) # food

# FPS constroller
fpsController = pygame.time.Clock()

snakePos = [100, 50] # [x, y]
snakeBody = [[100, 50], [90, 50], [80, 50]]
foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True
direction = 'RIGHT'
changeto = direction

# Game over function
def gameOver():
	myFont = pygame.font.SysFont('monaco', 72)
	goSurface = myFont.render('Game over!', True, red)
	goRect = goSurface.get_rect()
	goRect.midtop = (360, 10) # (x, y)
	playSurface.blit(goSurface, goRect)
	pygame.display.flip()

gameOver()
# time.sleep(10)
