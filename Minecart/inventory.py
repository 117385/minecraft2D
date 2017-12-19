#Made by Armando Crews 120717

import pygame
import pygame, sys
from pygame.locals import *

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
DIAMOND = 5
LAVA = 6


BLACK = (0, 0, 0 )
BROWN = (153, 76, 0 )
GREEN = (0, 255, 0 )
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

textures = {
        DIRT : pygame.image.load('H:\Minecart\Pictures\dirt.png'),
        GRASS : pygame.image.load('H:\Minecart\Pictures\grass.png'),
        WATER : pygame.image.load('H:\Minecart\Pictures\water.png'),
        COAL : pygame.image.load('H:\Minecart\Pictures\coal.png'),
        DIAMOND : pygame.image.load('H:\Minecart\Pictures\diamond.png'),
        ROCK : pygame.image.load('H:/Minecart/Pictures/rock.png'),
        LAVA : pygame.image.load('H:\Minecart\Pictures\lava.png'),
        
            }

inventory =  {
                DIRT : 0,
                GRASS : 0,
                WATER : 0,
                COAL : 0,
                DIAMOND : 0,
                ROCK : 0,
                LAVA : 0
            }

TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

PLAYER = pygame.image.load('H:\Minecart\Pictures\player.png')
playerPos = [0,0]

import random
resources = [DIRT,GRASS,WATER,COAL,ROCK,DIAMOND,LAVA]
tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]

pygame.init()
(6, 0)
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE + 50))
INVFONT = pygame.font.Font('FreeSansBold.ttf', 18)

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
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1:
                playerPos[0] += 1
            if event.key == K_LEFT and playerPos[0] > 0:
                playerPos[0] -= 1
            if event.key == K_UP and playerPos[1] > 0:
                playerPos[1] -= 1
            if event.key == K_DOWN and playerPos[1] < MAPHEIGHT - 1:
                playerPos[1] += 1
            if event.key == K_SPACE:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                inventory[currentTile] += 1
                tilemap[playerPos[1]][playerPos[0]] = DIRT
                #to place dirt
            if (event.key == K_1):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory [DIRT] > 0:
                        inventory[DIRT] -= 1
                        tilemap[playerPos[1]][playerPos[0]] = DIRT
                        inventory[currentTile] += 1
                #to place grass     
            if (event.key == K_2):
                     
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory [GRASS] > 0:
                        inventory[GRASS] -= 1
                        tilemap[playerPos[1]][playerPos[0]] = GRASS
                        inventory[currentTile] += 1
                #to place water
            if (event.key == K_3):
                     
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory [WATER] > 0:
                        inventory[WATER] -= 1
                        tilemap[playerPos[1]][playerPos[0]] = WATER
                        inventory[currentTile] += 1
                #to place coal
            if (event.key == K_4):
                     
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory [COAL] > 0:
                        inventory[COAL] -= 1
                        tilemap[playerPos[1]][playerPos[0]] = COAL
                        inventory[currentTile] += 1
                #to place rock
            if (event.key == K_5):
                     
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory [ROCK] > 0:
                        inventory[ROCK] -= 1
                        tilemap[playerPos[1]][playerPos[0]] = ROCK
                        inventory[currentTile] += 1

                #to place diamond
            if (event.key == K_6):
                     
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory [DIAMOND] > 0:
                        inventory[DIAMOND] -= 1
                        tilemap[playerPos[1]][playerPos[0]] = DIAMOND
                        inventory[currentTile] += 1
                #to place lava
            if (event.key == K_7):
                     
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory [LAVA] > 0:
                        inventory[LAVA] -= 1
                        tilemap[playerPos[1]][playerPos[0]] = LAVA
                        inventory[currentTile] += 1

                
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,))

    DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))

    placePosition = 10
    for item in resources:
            DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
            placePosition += 30
            textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
            DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
            placePosition += 50

    pygame.display.update()
