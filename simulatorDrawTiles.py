import pygame
import math
import time
import sys
import random
pygame.init()

#window stuff
width = 600
height = 600
win = pygame.display.set_mode((width, height))


class creature(object):
    def __init__(self):
        self.alive = True
        self.id = 0
        self.color = (0,0,255)
        self.x = 0
        self.y = 0

    def draw(self,color): #takes window as arg
        if(self.alive):
            pygame.draw.circle(win,self.color,(50,50),40,40)#



class carnivore(creature):
    def __init__(self):
        pass

class omnivore(creature):
    def __init__(self):
        pass

class herbivore(creature):
    def __init__(self):
        pass
class tile(object):
    def __init__(self,x,y):
        self.id = 0
        self.size = 20
        self.x = x
        self.y = y
        self.nutrivalue = 0

    def draw(self):
        pygame.draw.rect(win, (100, self.nutrivalue, 0), (self.x, self.y, self.size, self.size))

#tick rate
rate = 30
clock = pygame.time.Clock()

run = True

world = []
map = []

def initWorld():


    for y in range(0,height):
        for x in range(0,width):
            if (x%21==0 and y%21==0):
                newTile = tile(x,y)
                newTile.nutrivalue = random.randint(0,255)
                newTile.draw(win)

                map.append(newTile)
                world.append(newTile)



def redrawGameWindow():

    for x in world:
        x.draw()
    pygame.display.update() #updates window



c0 = creature()



while(run):



    clock.tick(rate)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #this is so you can actually close the window
            run = False #breaks loop


    redrawGameWindow()
