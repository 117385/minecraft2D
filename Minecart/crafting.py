#Made by Armando Crews 121217

import pygame
import pygame, sys
from pygame.locals import *

#this is the cloud position
cloudx = -200
cloudy = 0

#this is the bird's position
birdx = -100
birdy = 60

#fog's position
fogx = -200
fogy = 200


DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
ROCK = 4
DIAMOND = 5
LAVA = 6
CLOUD = 7
BIRD = 8
FOG = 9
STONE = 10
SAND = 11

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
        CLOUD : pygame.image.load('H:\Minecart\Pictures\cloud.png'),
        BIRD : pygame.image.load('H:/Minecart/Pictures/bird.png'),
        FOG : pygame.image.load('H:\Minecart\Pictures\cloud.png'),
        STONE : pygame.image.load('H:\Minecart\Pictures\stone.png'),
        SAND : pygame.image.load('H:\Minecart\Pictures\sand.png')
            }

inventory =  {
                DIRT : 0,
                GRASS : 0,
                WATER : 0,
                COAL : 0,
                DIAMOND : 0,
                ROCK : 0,
                LAVA : 0,
                STONE : 0,
                SAND : 0
            }
controls = {
              DIRT      : 49,
              GRASS     : 50,
              WATER     : 51,
              COAL      : 52,
              DIAMOND   : 53,
              ROCK      : 54,
              LAVA      : 55,
              STONE     : 56,
              SAND      : 57
           }


craft = {
             STONE : { ROCK : 2 },
             SAND : { ROCK : 2}     
        }

TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

PLAYER = pygame.image.load('H:\Minecart\Pictures\player.png')
playerPos = [0,0]

import random
resources = [DIRT,GRASS,WATER,COAL,ROCK,DIAMOND,LAVA,STONE,SAND]
tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT) ]

pygame.init()
(6, 0)
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE + 50))
INVFONT = pygame.font.Font('FreeSansBold.ttf', 18)

fpsClock = pygame.time.Clock()
pygame.display.update
fpsClock.tick(24)
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption('M I N E C R A F T --- 2 D')
pygame.display.set_icon(pygame.image.load('H:\Minecart\Pictures\player.png'))



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
    DISPLAYSURF.fill(BLACK)
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
            for key in controls:
                if (event.key == controls[key]):
                        if pygame.mouse.get_pressed()[0]:
                                #if the item can be crafted
                                if key in craft:
                                        canBeMade = True
                                for i in craft[key]:
                                        if craft[key][i] > inventory[i]:
                                                canBeMade = False
                                                break
                                if canBeMade == True:
                                        for i in craft[key]:
                                                inventory[i] -= craft[key][i]
                                                inventory[key] += 1
                                else:
                                    currentTile = tilemap[playerPos[1]][playerPos[0]]
                                    if inventory[key] > 0:
                                        inventory[key] -= 1
                                        inventory[currentTile] += 1
                                        tilemap[playerPos[1]][playerPos[0]] = key
                

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,))

    DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))

        #used to move and display cloud
    DISPLAYSURF.blit(textures[CLOUD],(cloudx,cloudy))
    cloudx+=1
    if cloudx > MAPWIDTH*TILESIZE:
            cloudy = random.randint(0,MAPHEIGHT*TILESIZE)
            cloudx = -200

         #used to move and display bird   
    DISPLAYSURF.blit(textures[BIRD],(birdx,birdy))
    birdx+=5
    if birdx > MAPWIDTH*TILESIZE:
            birdy = random.randint(60,MAPHEIGHT*TILESIZE)
            birdx = -100

        #used to move and display fog
    DISPLAYSURF.blit(textures[FOG],(fogx,fogy))
    fogx+=3
    if fogx > MAPWIDTH*TILESIZE:
            fogy = random.randint(200,MAPHEIGHT*TILESIZE)
            fogx = -200        
            
    placePosition = 10
    for item in resources:
            DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
            placePosition += 10
            textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
            DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
            placePosition += 35

    pygame.display.update()
