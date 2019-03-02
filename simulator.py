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


        def draw(self,win): #takes window as arg

            pass


class carnivore(creature):
    def __init__(self):
        pass

class omnivore(creature):
    def __init__(self):
        pass


class tile(object):
    def __init__(self):
        self.id = 0

    def __init__(self,num):
        self.num = num


#tick rate
rate = 30


run = True

while(run):
clock.tick(rate)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #this is so you can actually close the window
            run = False #breaks loop
