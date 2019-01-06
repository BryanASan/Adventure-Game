import pygame
import sys, os, random , math
from pygame.locals import *


animation=['walking1.png', 'walking2.png','standing.png']
objects=[] #collidable objects on screen
BLACK = (0 ,0, 0)


class Man:
    def __init__(self,):
        """ The constructor of the class """
        self.image = pygame.image.load('standing.png')
        self.image = pygame.transform.scale(self.image, (200,50))
        self.x = 400
        self.y = 250
        self.rect = self.image.get_rect()
        


    def walking(self):
        for number in range(0,3):
            if number == 3:
                number=0
            self.image = pygame.image.load(animation[number])
            self.image = pygame.transform.scale(self.image, (200,50))
            Draw_all(objects)
            pygame.time.delay(100)
            
    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 100
        step = dist/2
        if key[pygame.K_DOWN]:  # down key
            newy=self.y+dist
            for i in range (2):
                self.y += step
                self.stay_in_border(self.x, newy)
                self.walking()
                self.stay_in_border(self.x, newy)
        elif key[pygame.K_UP]: # up key
            newy=self.y-dist
            for i in range (2): #does the walk and its animation twice
                self.y -= step
                self.stay_in_border(self.x, newy)
                self.walking()
                self.stay_in_border(self.x, newy)
        if key[pygame.K_RIGHT]: # right key
            newx=self.x+dist
            for i in range (2):
                self.x += step
                self.stay_in_border(newx,self.y)
                self.walking()
                self.stay_in_border(newx,self.y)
        elif key[pygame.K_LEFT]:# left key
            newx=self.x-dist
            for i in range (2):
                self.x -= step
                self.walking()
                self.stay_in_border(newx, self.y)

    def stay_in_border(self,x,y):
        if self.x <= 0:
            self.x= 0
            pygame.display.update()
        elif self.x >= 1000:
            self.x= 1000
            pygame.display.update()
        elif self.y <= 10:
            self.y= 10
            pygame.display.update()
        elif self.y >= 570:
            self.y= 570
            pygame.display.update()

##    def spawn_enemies_away(self,x,y):
##        if self.x <= 100:
##            enemy_co= self.x+100
##            
##            
##        elif self.x >= 1000:
##            self.x= 1000
##
##        elif self.y <= 10:
##            self.y= 10
##
##        elif self.y >= 570:
##            self.y= 570

        
        

    def draw(self, surface):
        """ Draw on surface """
        surface.blit(self.image, (self.x, self.y))

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image,( 1000, 600))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Enemy(pygame.sprite.Sprite):
    '''
    Spawn an enemy
    '''
    def __init__(self,x,y,img, velocity):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (60,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.draw(screen)
        self.velocity= velocity

    def draw(self, surface):
        """ Draw on surface """
        surface.blit(self.image,(self.rect.x, self.rect.y))

    def move_towards_player(self, player):
        # finds normalised direction vector (dx, dy) between enemy and player
        if self.rect.x != player.x and self.rect.y != player.y:            
            if self.rect.x <= player.x and self.rect.y <= player.y:
                dx, dy = player.x - self.rect.x +40, player.y - self.rect.y-10 
                print("Apple")
            elif self.rect.x <= player.x and self.rect.y >= player.y:
                dx, dy = player.x - self.rect.x +40, player.y - self.rect.y-10
                print("Banana")
            elif self.rect.x >= player.x and self.rect.y <= player.y:
                dx, dy = player.x - self.rect.x +40, player.y - self.rect.y-10
                print("Cherry")
            elif self.rect.x >= player.x and self.rect.y >= player.y:
                dx, dy = player.x - self.rect.x +40, player.y - self.rect.y -10
                print("Date")
            elif self.rect.x == player.x and self.rect.y >=player.y:
                dx, dy= player.x - self.rect.x +40 , player.y - self.rect.y -10
                print ("Elderberry")
            elif self.rect.x == player.x and self.rect.y <=player.y:
                dx, dy= player.x - self.rect.x +40 , player.y - self.rect.y -10
                print("Fig")
            elif self.rect.x <= player.x and self.rect.y ==player.y:
                dx, dy= player.x - self.rect.x +40, player.y - self.rect.y -10
                print("Grapes")
            elif self.rect.x >= player.x and self.rect.y ==player.y:
                dx, dy= player.x - self.rect.x +40 , player.y - self.rect.y -10
                print("Honeydew Melon")
            else:
                dx, dy= player.x , player.y
                print("Indian Plum")
        else:
            dx,dy= player.x , player.y
            
        Draw_all(objects)   
        dist = math.hypot(dx, dy)
        if dist==0:
            dist=dist+1
        dx, dy = dx / dist, dy / dist
        # moves along this normalised vector towards the player at current speed
        
        self.rect.x += dx * self.velocity
        pygame.time.delay(50)
        self.rect.y += dy * self.velocity
        pygame.time.delay(50)
        print(self.rect.x, self.rect.y)
        print(player.rect.x, player.rect.x)

class Alien(Enemy): #Takes all methods and attributes of parent class without changes
    pass

#This function is to make all the 'things' (man, enemies, trees etc) not disappear as the man is moving
def Draw_all(things):
    for number in range (0, len(objects)):
        objects[number].draw(screen)
        pygame.display.update()

pygame.init()
#Makes a world grid to use to navigate where the player is and what should change based on that
worldgrid = []
row_coord= 0
column_coord=0
for row in range(1,5):
    row_coord= row
    for column in range (1,5):
        column_coord= column
        worldgrid.append((row_coord,column_coord))

current_coord=worldgrid[3] #sets the start point as coordinates (1,4) on the worldgrid

screen = pygame.display.set_mode((1000, 600))
background = Background('background.png', [0,0])
man = Man() #creates a instance
alien= Alien(400,400,'alien.png',10)
clock= pygame.time.Clock()
screen_rect = screen.get_rect()


#Here I'm adding all the 'things' into a list- this will be used to check for collisions and for updating the screen
objects.append(man)
objects.append(alien)


running = True
while running:
    screen.fill((255,255,255)) # fill the screen with white
    screen.blit(background.image, background.rect)
    x,y = pygame.mouse.get_pos()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False
    man.handle_keys() # handle the keys
    man.draw(screen) # draw the man to the screen
    alien.draw(screen)
    pygame.display.update() # update the screen
    alien.move_towards_player(man)
    clock.tick(60)
