import pygame
import math
import time
import sys
import random
pygame.init()

#window stuff
width = 1000
height = 800
win = pygame.display.set_mode((width, height))


class creature(object):



    def __init__(self):
        self.alive = True
        self.id = 0
        self.color = (0,0,255)
        self.x = 0
        self.y = 0
        self.facing = random.randint(0,360)

    def move():
        
        speed = 20 #increase this variable slows the character down
        self.facing += random.randint(-2, 2)
        if (self.facing > 360):
            self.facing -= 360
        if (self.facing < 0):
            self.facing += 360

        if (self.facing > 270):
            self.x += (self.facing - 270)/speed
            self.y += (self.facing - 360)/speed
        elif (self.facing > 180):
            self.x += (self.facing - 270)/speed
            self.y += (180 - self.facing)/speed
        elif (self.facing > 90):
            self.x += (90 - self.facing)/speed
            self.y += (180 - self.facing)/speed
        else:
            self.x += (90 - self.facing)/speed
            self.y += (self.facing)/speed
                

    def draw(self,color): #takes window as arg
        if(self.alive):
            pygame.draw.circle(win,self.color,(50,50),20,20)#




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
        self.size = 30
        self.x = x
        self.y = y
        self.nutrivalue = 0

    def draw(self):
        pygame.draw.rect(win, (100, self.nutrivalue, 0), (self.x, self.y, self.size, self.size))

    def getpos(clickx,clicky):
        if(( clickx >= self.x and clickx <= self.x+size ) and ( clicky >= self.y and clicky <= self.y+size )):
            return "works"

#tick rate
rate = 30
clock = pygame.time.Clock()

run = True

world = []
map = []

def initWorld():


    for y in range(0,height):
        for x in range(0,width):
            if (x%31==0 and y%31==0):
                newTile = tile(x,y)
                newTile.nutrivalue = random.randint(0,255)
                newTile.draw()

                map.append(newTile)
                world.append(newTile)



initWorld()

def redrawGameWindow():

    for x in world:
        x.draw()
    pygame.display.update() #updates window



c0 = creature()



while(run):



    clock.tick(rate)


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for x in map:
                print(x.getpos(pos))


        if event.type == pygame.QUIT:
            #this is so you can actually close the window
            run = False #breaks loop



    redrawGameWindow()
