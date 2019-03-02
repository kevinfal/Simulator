import pygame
import math
import time
import random
#initializes pygame
pygame.init()
#always necessary at beginning of program


#window
#what we draw on
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")
#sets label of windown to "First Game"

#sprite lists

walkRight = [pygame.image.load('tom_right.png')]
walkLeft = [pygame.image.load('tom_left.png')]
boxImg = pygame.image.load('box.png')
char = [pygame.image.load('tom_standing.png')]
bg = [pygame.image.load('bg.png')]

projectileIMG = pygame.image.load('slime_projectile.png')

#clockSpeed
clock = pygame.time.Clock()
rate = 30


#score
score = 0

#kill Count
killCount = 0


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.jumpFlag = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

        #health
        self.health = 4

        #hitbox stuff
        self.hitbox = (self.x + 15, self.y +20, 37, 30)
#character attributes for movement

#wherever it says man in these functions can be replaced with self
#I screwed it up, should be def draw(self, window):

    def draw(window):
        if man.walkCount +1 >= rate:
            man.walkCount = 0

        if not(man.standing):

                if man.left:
                    win.blit(walkLeft[0], (man.x,man.y))
                    man.walkCount +=1
                elif man.right:
                    win.blit(walkRight[0], (man.x,man.y))
                    man.walkCount += 1
        else:
            if man.right:
                win.blit(walkRight[0], (man.x, man.y))
            else:
                win.blit(walkLeft[0], (man.x, man.y))
         #pygame.draw.(shape)(window, color)
        #hitbox stuff
        man.hitbox = (man.x + 15, man.y +20, 37, 30)
        #to adjust
        # (self.x + #shift left/right , self.y + #shift up/down  , width, height)
        #pygame.draw.rect(win, (255,0,0) , man.hitbox, 2)
class projectile(object):
    def __init__(self,x,y,width,height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing
        self.vel = 8 * facing
        #hitbox
        self.hitbox =   self.hitbox = (self.x , self.y , 29, 52)
        #damage
        self.damage = 1

    def draw(self, win):
        win.blit(projectileIMG, (self.x, self.y))
        #hitbox
        self.hitbox = (self.x +5, self.y +2, 23, 30)
        #actual box
       # pygame.draw.rect(win, (255,0,0) , self.hitbox, 2)


class enemy(object):
    walkRight = pygame.image.load('slimey_good.png')
    walkLeft = pygame.image.load('slimey_good.png')
    temp = pygame.image.load('slimey_good.png')
    attack = pygame.image.load('slimey_bad.png')
    def __init__(self,x,y,width,height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        #hitbox stuff
        self.hitbox = (self.x + 5, self.y +15, 50, 30)
        #health
        self.healthMax = 5
        self.health = 5
        self.visible = True


        #alive flag
        self.alive = True
        self.rage = False
        self.rageLoop = 0
    def hit(self):
        global killCount
        #on hit
        if self.health > 0:
            self.health -= 1
        else:
            killCount += 1
            self.visible = False
            print(killCount)

    def draw(self,win):

    #checks if alive then draws
        if self.visible:
            self.move()

            #checks for collisions with projectiles

            if self.rage == True:
                self.walkRight = self.attack
                self.walkLeft = self.attack

                self.rageLoop = 1
                print(self.rageLoop)

                if self.rageLoop  > 0:
                    print("wtf")
                    self.rageLoop = self.rageLoop + 1
                if self.rageLoop > 30:
                    self.Rage = False
                    self.rageLoop = 0

            if self.walkCount + 1 >= 33:
                self.walkCount = 0
                #loops a walking animation if I had one
            if self.vel >0:
                win.blit(self.walkRight, (self.x, self.y))
                self.walkCount +=1

            else:
                win.blit(self.walkLeft, (self.x, self.y))
                self.walkCount +=1

            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
             #Rect((left, top), (width, height))

            #pygame.draw.(shape)(window, color)
            #hitbox stuff
            self.hitbox = (self.x + 5, self.y +15, 50, 30)
            #to adjust
            # (self.x + #shift left/right , self.y + #shift up/down  , width, height)

            #pygame.draw.rect(win, (255,0,0) , self.hitbox, 2)
            #un comment this if you want to check the hitboxes


    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                #opposite direction
                self.vel = self.vel*-1
                self.x += self.vel
                self.walkCount = 0


        else:
            if self.x > self.path[0] - self.vel:
                self.x+= self.vel
            #moving in opposite direction
            else:
                self.vel = self.vel*-1
                self.x += self.vel
                self.walkCount = 0





class box(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 128
        self.height = 128
        self.hitbox = (self.x, self.y)
        self.hitbox = (self.x , self.y, self.width, self.height)

    def draw(self, win):
        win.blit(boxImg ,(self.x , self.y))
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        #collisions with player

#functions

def redrawGameWindow():
    global walkCount

    win.blit(bg[0], (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0)) #text stuff, creates a surface (text)]
    win.blit(text, (300,10))
    man.draw()
    slime.draw(win)
    slime.move()
    box1.draw(win)

    #projectile stuff
    for bullet in bullets:
        bullet.draw(win)

        if facing == -1:
            #pygame.flip(bullet, False, True)
            pygame.transform.flip(projectileIMG,False,True)
    #projectile stuff

    #pygame.draw.(shape)(window, color, (x,y, width , height))
    pygame.display.update() #updates window



#main loop
#like a tick rate, reloads over and over
man = player(300,410, 64, 64)
slime = enemy(100,410, 64,64, 450)
box1 = box(50, 290)
slimeLoop = 0 #slime recussitation loop
shootLoop = 0 # to control fire rate like a timer
bullets = []

font = pygame.font.SysFont('times new roman', 30, True)
#(font, size, bold, italics)

run = True

while run:
    clock.tick(rate)

    #so things don't happen super fast


    if shootLoop > 0:
        shootLoop +=1
    if shootLoop > 15:
        shootLoop = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #this is so you can actually close the window
            run = False #breaks loop


    #slime recussitation
    if not slime.visible and not(slimeLoop > 0):
        slimeLoop = 1
    elif not slime.visible and slimeLoop >0:
        slimeLoop +=1
    if not slime.visible and slimeLoop > 15:
        slimeLoop = 0
        slime.health = slime.healthMax
        slime.visible = True
        slime.x = random.randrange(0,500)
        print("wtf")

    #projectile stuff
    for bullet in bullets:

        #collision for damage
        if bullet.y < slime.hitbox[1] + slime.hitbox[3] and bullet.y > slime.hitbox[1]:
            if bullet.x > slime.hitbox[0] and bullet.x < slime.hitbox[0] + slime.hitbox[2]:
                #slime on damage
                slime.hit()
                score += 1
                bullets.pop(bullets.index(bullet)) #removes bullet from screen


        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            #finds bullet in index of list and removes



    keys = pygame.key.get_pressed()

#updating window
    redrawGameWindow()


#horizontal movement
    #shooting
    if keys[pygame.K_SPACE] and shootLoop == 0:
        #shootLoop limits the bullets fire rate with a cooldown
            if man.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 5:
                bullets.append(projectile((round(man.x + man.width //2)), (round(man.y + man.height//2)) ,64,64, facing))
                shootLoop = 1

    #boundaries + movement
    if keys[pygame.K_LEFT] and man.x >= 0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.stainding = False
    elif keys[pygame.K_RIGHT] and man.x < 450:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True

#vertical movement
    if not(man.jumpFlag):



        if keys[pygame.K_UP]:
            man.jumpFlag = True
            man.right = False
            man.left = False

            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            negative = 1
            if man.jumpCount < 0:
                negative = -1 #allows us to go back down
            man.y -= (man.jumpCount ** 2) /2 *negative
            man.jumpCount -=1
        else:
            man.jumpFlag = False
            man.jumpCount = 10
            #jump is completed



pygame.quit()
