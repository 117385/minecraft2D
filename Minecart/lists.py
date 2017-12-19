#Made by Armando Crews 120717
import pygame
import pygame, sys
from pygame.locals import *
tilemap = [[1,3,0],[2,2,1],[3,1,2],[0,2,3],[1,2,0]]
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
DIAMOND = 5
LAVA = 6
tilemap = [
	    [GRASS, COAL, DIRT],
	    [WATER, WATER, GRASS],
	    [COAL, LAVA, WATER],
	    [ROCK, GRASS, COAL],
	    [GRASS, WATER, DIAMOND],
           ]
BLACK = (0, 0, 0 )
BROWN = (153, 76, 0 )
GREEN = (0, 255, 0 )
BLUE = (0, 0, 255)
textures = {
	    DIRT : pygame.image.load('dirt.png'),
	    GRASS : pygame.image.load('grass.png'),
	    WATER : pygame.image.load('water.png'),
	    COAL : pygame.image.load('coal.png'),
            DIAMOND : pygame.image.load('diamond.png'),
            ROCK : pygame.image.load('rock.png'),
            LAVA : pygame.image.load('lava.png')
            }

TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

import random
resources = [DIRT,GRASS,WATER,COAL]
tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]

pygame.init()
(6, 0)

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

for rw in range(MAPHEIGHT):
        for cl in range(MAPWIDTH):
                randomNumber = random.randint(0,15)
                if randomNumber == 0:
                        tile = COAL
                elif randomNumber == 1 or randomNumber == 2:
                        tile = WATER
                elif randomNumber >= 3 and randomNumber <= 7:
                        tile = GRASS
                elif randomNumber == 8:
                        tile = DIAMOND
                elif randomNumber >= 9 and randomNumber <= 11:
                        tile = ROCK
                elif randomNumber >= 12 and randomNumber <= 14:
                        tile = LAVA
                else:
                        tile = DIRT
                tilemap[rw][cl] = tile

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,))
	pygame.display.update()













	
