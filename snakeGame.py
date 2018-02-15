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

score = 0

# scoreboard
def showScore(choice = 1):
	sFont = pygame.font.SysFont('monaco', 24)
	sSurface = sFont.render('Score: {0}'.format(score), True, black)
	sRect = sSurface.get_rect()
	if choice == 1:
		sRect.midtop = (80, 10)
	else:
		sRect.midtop = (360, 120)
	playSurface.blit(sSurface, sRect)

# Game over function
def gameOver():
	myFont = pygame.font.SysFont('monaco', 72)
	goSurface = myFont.render('Game over!', True, red)
	goRect = goSurface.get_rect()
	goRect.midtop = (360, 10) # (x, y)
	playSurface.blit(goSurface, goRect)
	showScore(0)
	pygame.display.flip()
	time.sleep(5)
	pygame.quit() # for pygame
	sys.exit() # for console

# gameOver()
# time.sleep(10)

# main logic
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('w'):
				changeto = 'UP'
			if event.key == pygame.K_DOWN or event.key == ord('s'):
				changeto = 'DOWN'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT)) # create event

	# validation of direction (can't change direction in the opposite)
	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'

	# moving snake
	if direction == 'RIGHT':
		snakePos[0] += 10
	if direction == 'LEFT':
		snakePos[0] -= 10
	if direction == 'UP':
		snakePos[1] -= 10
	if direction == 'DOWN':
		snakePos[1] += 10

	# Snake body mechanism
	snakeBody.insert(0, list(snakePos))
	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
		score += 1
		foodSpawn = False  #temporarily
	else:
		snakeBody.pop()

	if foodSpawn == False:
		foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
	foodSpawn = True

	playSurface.fill(white)
	# draw snake
	for pos in snakeBody:
		pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

	# draw food
	pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

	# check boundaries
	if snakePos[0] > 710 or snakePos[0] < 0:
		gameOver()

	if snakePos[1] > 450 or snakePos[1] < 0:
		gameOver()

	# check if snake touched itself
	for block in snakeBody[1:]:
		if snakePos[0] == block[0] and snakePos[1] == block[1]:
			gameOver()

	showScore()
	pygame.display.flip()
	fpsController.tick(20)

