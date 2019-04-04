import pygame
import math
import time
import sys
import random
pygame.init()
pygame.font.init()



#font
font = pygame.font.SysFont('times new roman', 30, True)

#window stuff

windowWidth = 1500
windowHeight = 700
win = pygame.display.set_mode((windowWidth , windowHeight))
  

#bounds
tileSize = 30
tileWidth = 30 #amount of tiles across
tileHeight = 22 #amount of tiles height

height = tileSize * tileHeight
width = tileSize * tileWidth
#creature bound
boundXMin = 50
boundYMin =50
boundXMax = 500
boundYMax = 500



#debug String
debug = ""
debugging = False

#status only changes after clicking
#this is the text displayed after clicking something
status = ""

#pause bool
pause = False

#image bank
pausebtn = pygame.image.load('Images/pause.png')
playbtn = pygame.image.load('Images/play.png')
ffbtn = pygame.image.load('Images/ff.png')
doubleFFbtn = pygame.image.load('Images/doubleff.png')


class creature(object):


    def __init__(self):
        self.alive = True
        self.id = 0
        self.color = (0,0,255)
        self.x = random.randint(50, 950)
        self.y = random.randint(50,750)
        self.facing = random.randint(0,360)
        self.speed = 20
        self.size = 10 #radius/width


    #eating function
    def eat(self):
        currentTile = onTile((self.x,self.y))
        #if the current tile exists
        if currentTile != -1:
            nutrivalue = currentTile.nutrivalue
            currentTile.nutrivalue -=50
            if currentTile.nutrivalue < 0:
                currentTile.nutrivalue = 0


    def getpos(self,clicks):
        clickx = clicks[0]
        clicky = clicks[1]
        if(( clickx >= self.x - self.size and clickx <= self.x+ self.size ) and ( clicky >= self.y -10 and clicky <= self.y + self.size )):
            return True

    def move(self):
        speed = 8 #increase this variable slows the character down
        #if the creature is in these bounds
        if self.x in range(50,width) and self.y in range(50,height):
            

            
            self.facing += random.randrange(-5, 5)

            #checks if the direction is above 360 and fixes it
            if (self.facing > 360):
                self.facing -= 360

            #checks if the direction is negative and fixes it
            if (self.facing < 0):
                self.facing += 360

            '''     90
                    |
                x   |   x
         180--------+-------0/360
                    |
                x   |
                    270

            '''

            #if the facing is more than 270
            if (self.facing > 270):
                    
                #incerase x by 
                        #-270 gets it into the first quadrant
                        #divide it by speed to increment it
                self.x += (self.facing - 270)/speed
                self.y += (self.facing - 360)/speed


                '''     90
                        |
                        |    
            180--------+-------0/360
                        |
                    x   |
                        270

                '''

            #if facing is more than 180 and less than 270
            elif (self.facing > 180):
                self.x += (self.facing - 270)/speed
                self.y += (180 - self.facing)/speed

                '''     90
                    x   |
                        |    
            180--------+-------0/360
                        |
                    x   |   x
                        270

                '''

            elif (self.facing > 90):
                self.x += (90 - self.facing)/speed
                self.y += (180 - self.facing)/speed

            else:
                self.x += (90 - self.facing)/speed
                self.y += (self.facing)/speed

            self.x = int(self.x)
            self.y = int(self.y)
            
            #goes here if not in bounds
        else:
            #if out of bounds in x 
            if not(self.x in range(50,width)):

                #if out of bounds to the right
                if(self.x >= width):
                    self.facing = abs(self.facing - 180)
                    #if out of bounds to the left
                elif(self.x <= 0):
                    self.facing = abs(self.facing + 180) -360
            
                
                #if out of bounds y 
            if not(self.y in range(50,height)):

                #if out of bounds y
                if(self.y >= height - 50):
                    self.facing = abs(self.facing + 180) - 360
                elif(self.y <= 50):
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
            
        

    #draws a creature's eyes
    def drawEye(self,eyeX,eyeY):
        speed = 4
        eyeColor = (255,0,100)

         

        '''     90
                |
            x   |   x
        180--------+-------0/360
                |
            x   |
                270

        '''

        #if the facing is more than 270
        if (self.facing > 270):
                
            #incerase x by 
                    #-270 gets it into the first quadrant
                    #divide it by speed to increment it
            eyeX += (self.facing - 270)/speed
            eyeY += (self.facing - 360)/speed


            '''     90
                    |
                    |    
        180--------+-------0/360
                    |
                x   |
                    270

            '''

        #if facing is more than 180 and less than 270
        elif (self.facing > 180):
            eyeX += (self.facing - 270)/speed
            eyeY += (180 - self.facing)/speed

            '''     90
                x   |
                    |    
        180--------+-------0/360
                    |
                x   |   x
                    270

            '''

        elif (self.facing > 90):
            eyeX += (90 - self.facing)/speed
            eyeY += (180 - self.facing)/speed

        else:
            eyeX += (90 - self.facing)/speed
            eyeY += (self.facing)/speed

        eyeX = int(eyeX)
        eyeY = int(eyeY)

        pygame.draw.circle(win,eyeColor,(eyeX,eyeY),2,2)


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

            #if the game is paused, don't move
            if(not pause):
                self.choice()


            pygame.draw.circle(win,self.color,(self.x,self.y),10,10)# draws the actual creature itself
            self.drawEye(self.x,self.y)




class carnivore(creature):
    def __init__(self):
        pass

class omnivore(creature):
    def __init__(self):
        pass

class herbivore(creature):
    def __init__(self):
        pass


#tile class, what makes up the whole map
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



class textBox(object):
 
    def __init__(self,height,width,xy,color):

        

        self.height = height
        self.width = width
        
        self.x = self.xy[0] # to just place it in the reference of the window width
        self.y = self.xy[1]
        self.texts = []
        self.color = (color[0],color[1],color[2]) #list of text that the box will display      

    def draw(self):
        for x in self.texts:
            x.draw()
        pygame.draw.rect(win,(self.color[0],self.color[1],self.color[2]), (self.x, self.y,self.width , self.height))

class text():
    def __init__(self,xy,txt):
        self.x = xy[0]
        self.y = xy[1]
        self.txt = txt
    def draw(self):
        text = font.render((self.txt), 1, (0,0,255))
        win.blit(text,(self.x,self.y))

#creates button from sprite
class button():
    '''
    Keyword arguments:
    xy -- coordinates in form of tuple
    image -- python.image object, sprite
    '''
    def __init__(self,xy,image):

        self.xy = xy
        self.x = xy[0]
        self.y = xy[1]
        self.image = image
        self.size = 64
    def draw(self):
        win.blit(self.image, self.xy)

    def getpos(self,clicks):

        clickx = clicks[0]
        clicky = clicks[1]

        if(( clickx >= self.x and clickx <= self.x+self.size ) and ( clicky >= self.y and clicky <= self.y+self.size )):
            return True


#acts as a collection of buttons that control the rate (time)
#formats it so they're all in alignment
class timeControl():
    '''
    Keyword arguments:
    anchorButton -- Button object, uses this one as anchor
    '''
    def __init__(self,anchorButton):
        self.anchorButton = anchorButton
        self.buttons = [anchorButton]
    '''
    Keyword arguments:
    image -- a image object to add to the collection and creates button
    '''
    def add(self,image):
        #gets the button before on the list and uses that x and y
        addto = len(self.buttons)  - 1
        prev = self.buttons[addto]

        #creates button and appends
        newButton = button((prev.x + 64,prev.y), image)
        self.buttons.append(newButton)


    #draws all of the buttons in its collection
    def draw(self):
        for x in self.buttons:
            x.draw()
            





    
class mainBox(textBox):
    #this constructor is for the main text box
    def __init__(self):
        
        
        self.height = 620
        self.width = 520
        self.texts = [] #list of text that the box will display
        self.x = windowWidth - (self.width + 25) # to just place it in the reference of the window width
        self.y = 70
        self.mainText = text((self.x,self.y) ,"Status: " + status)
        self.components = []


    def draw(self):

        self.mainText = text((self.x,self.y) ,"Status: " + status)
    #rect(Surface, color, Rect, width=0)
    #Draws a rectangular shape on the Surface. The given Rect is the area of the rectangle.
    #The width argument is the thickness to draw the outer edge. If width is zero then the rectangle will be filled

    #this rectangle is the background for the text
        pygame.draw.rect(win,(255,255,255), (self.x, self.y,self.width , self.height))
        for x in self.texts:
            x.draw()
        self.mainText.draw()






#utility functions


def onTile(pos):#accepts tuple as argument, returns tile

    tile = -1

    for x in map:#loops through all of the tiles in the map
        if(x.getpos(pos)):#if the click is on a tile
            tile = x

    return tile

    



#tick rate
rate = 30
originRate = rate
clock = pygame.time.Clock()

run = True

#collections of objects 
#i.e world has everything, map has tiles, organisms has living things ect
world = []
map = []
organisms = []
creatures = []

ui = []


#makes main box
box = mainBox()
world.append(box)

play = button((950,0),playbtn)
control = timeControl(play)
control.add(pausebtn)
control.add(ffbtn)
control.add(doubleFFbtn)

ui.append(control)
world.append(control)


#initializes everything pretty much
def initWorld():


    #generates the tile map
    for y in range(0,tileSize*tileHeight):#I want 30 tiles accross, and tiles are 30 wide so 30 * 30
        for x in range(0,tileSize * tileWidth): #same as above but i was 25 tiles going down
            if (x%31==0 and y%31==0):
                newTile = tile(x,y)
                newTile.nutrivalue = random.randint(0,255)
                newTile.draw()

                map.append(newTile)
                world.append(newTile)

    #generates creatures
    for i in range(0,5):
        newCreature = creature()
        newCreature.id = i
        creature.x = random.randint(boundXMin,boundXMax)
        creature.y = random.randint(boundYMin,boundYMax)

        creatures.append(newCreature)
        world.append(newCreature)
        organisms.append(newCreature)







#creates the world
initWorld()

def redrawGameWindow():

    #draw bg
    pygame.draw.rect(win,(0,0,0), (0, 0,windowWidth , windowHeight))
    
    for x in world:
        x.draw()
    
    if debugging:
        
        debugText = font.render(debug,1,(0,0,255))
        win.blit(text, (500,500))

    #things that need to update (like creature movement n stuff)



    pygame.display.update() #updates window

while(run):

    
    #gets keys pressed
    keys = pygame.key.get_pressed()

    #ticks if not paused
    if(not pause):
        clock.tick(rate)

    for event in pygame.event.get():

        #on click
        if event.type == pygame.MOUSEBUTTONUP:
            
            #checks if the click is on a tile
            
            pos = pygame.mouse.get_pos()
            for x in map:#loops through all of the tiles in the map
                if(x.getpos(pos)):#if the click is on a tile
                    status = "Nutrivalue: " +str(x.nutrivalue)#print the tile's nutritional value\
            for x in organisms:
                if x.getpos(pos):
                    status = "Creature: " + str(x.id)
            
            #time control check
            for x in control.buttons:
                if x.getpos(pos):
                    if x.image == pausebtn:#if the click is on the pause button
                        pause = True

                    if x.image == playbtn:#if the click is on the play button
                        rate = originRate
                        pause = False

                    if x.image == ffbtn:#click on fast forward button
                        rate = originRate*2

                    if x.image == doubleFFbtn: #click on double fast forward button
                        rate = math.pow(originRate,2)

            redrawGameWindow()
            #end tile check

        #on space press
        if keys[pygame.K_SPACE]:
            pause = not pause
            

        #if the user clicks exit
        if event.type == pygame.QUIT:
            #this is so you can actually close the window
            run = False #breaks loop

    if not pause:
        redrawGameWindow()

    
