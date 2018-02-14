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

# colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)


