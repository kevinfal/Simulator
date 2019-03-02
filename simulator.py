import pygame
import math
import time
import sys

pygame.init()

#window stuff
win = pygame.display.set_mode((600, 600))


class creature(object):
    def __init__(self):

        self.id = id
        self.color = (0,0,255)
    def draw(self,color): #takes window as arg
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
    def __init__(self):
        self.id = 0
        nutriValue = 0



    def __init__(self,num):
        self.num = num


#tick rate
rate = 30
clock = pygame.time.Clock()

run = True

def redrawGameWindow():
    pygame.display.update() #updates window



c0 = creature()


while(run):



    clock.tick(rate)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #this is so you can actually close the window
            run = False #breaks loop


    c0.draw((0,0,255))
    redrawGameWindow()
