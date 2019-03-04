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

#bounds

class creature(object):



    def __init__(self):
        self.alive = True
        self.id = 0
        self.color = (0,0,255)
        self.x = random.randint(50, 950)
        self.y = random.randint(50,750)
        self.facing = random.randint(0,360)
    #eating function
    def eat(self):

        currentTile = onTile((self.x,self.y))

        
        #if the current tile exists
        if currentTile != -1:

            nutrivalue = currentTile.nutrivalue
            currentTile.nutrivalue -=50
            if currentTile.nutrivalue < 0:
                currentTile.nutrivalue = 0
        
        

    
    def move(self):
        speed = 20 #increase this variable slows the character down

        #random
        
        chance = random.randint(0,100)
       
        
        if self.x in range(50,width-50) and self.y in range(50,height-50):
            

            
            self.facing += random.randrange(-5, 5)
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
            self.x = int(self.x)
            self.y = int(self.y)
            
        else:
            self.facing = abs(self.facing - 180)
            self.facing += random.randrange(-5, 5)
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
            self.x = int(self.x)
            self.y = int(self.y)
        
    #the creature's decision tree
    def choice(self):

        chance = random.randint(0,100)
        if chance >= 50:
            self.eat()
        else:
            self.move()
    
    #draws the creature onto the screen
    def draw(self):
        if(self.alive):
            self.choice()
            pygame.draw.circle(win,self.color,(self.x,self.y),10,10)#




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

    def getpos(self,clicks):

        clickx = clicks[0]
        clicky = clicks[1]

        if(( clickx >= self.x and clickx <= self.x+self.size ) and ( clicky >= self.y and clicky <= self.y+self.size )):
            return True


#utility functions


def onTile(pos):#accepts tuple as argument, returns tile
    posx = pos[0]
    posy = pos[1]

    tile = -1

    for x in map:#loops through all of the tiles in the map
        if(x.getpos(pos)):#if the click is on a tile
            tile = x

    return tile

    



#tick rate
rate = 30
clock = pygame.time.Clock()

run = True

world = []
map = []
organisms = []
creatures = []



def initWorld():


    #generates the tile map
    for y in range(0,height):
        for x in range(0,width):
            if (x%31==0 and y%31==0):
                newTile = tile(x,y)
                newTile.nutrivalue = random.randint(0,255)
                newTile.draw()

                map.append(newTile)
                world.append(newTile)
    
    for i in range(0,5):
        newCreature = creature()
        creature.x = random.randint(50,width-50)
        creature.y = random.randint(50,height-50)
        creatures.append(newCreature)
        world.append(newCreature)
        organisms.append(newCreature)



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
            for x in map:#loops through all of the tiles in the map
                if(x.getpos(pos)):#if the click is on a tile
                    print(x.nutrivalue)#print the tile's nutritional value




        if event.type == pygame.QUIT:
            #this is so you can actually close the window
            run = False #breaks loop



    redrawGameWindow()
