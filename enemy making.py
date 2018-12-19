import pygame
import sys, os, random
from pygame.locals import *

animation=['walking1.png', 'walking2.png','standing.png']
objects=[] #collidable objects on screen
BLACK = (0 ,0, 0)


class Man:
    def __init__(self,):
        """ The constructor of the class """
        self.image = pygame.image.load('standing.png')
        self.image = pygame.transform.scale(self.image, (200,50))
        #self.border =(500 ,500, 5, 20)
        self.x = 250
        self.y = 250
        self.rect = self.image.get_rect()
        


    def walking(self):
        for number in range(0,3):
            if number == 3:
                number=0
            self.image = pygame.image.load(animation[number])
            self.image = pygame.transform.scale(self.image, (200,50))
            self.draw(screen)
            pygame.display.update()
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
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (100,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.draw(screen)

    def draw(self, surface):
        """ Draw on surface """
        surface.blit(self.image,(self.rect.x, self.rect.y))



pygame.init()
#Makes a world grid to use to navigate where the player is and what should change based on that

screen = pygame.display.set_mode((1000, 600))
BackGround = Background('background.png', [0,0])
man = Man() # create an instance
#for spawn in range (1,3):
#    random.randint((man.self.x)+                                                                                                                                                                                                           

        
skullfish= Enemy(400,400,'skullfish.png')
#objects.append(
clock= pygame.time.Clock()
screen_rect = screen.get_rect()

running = True
while running:
    screen.fill((255,255,255)) # fill the screen with white
    screen.blit(BackGround.image, BackGround.rect)
    x,y = pygame.mouse.get_pos()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False
    man.handle_keys() # handle the keys
    man.draw(screen) # draw the man to the screen
    skullfish.draw(screen)
    pygame.display.update() # update the screen
    clock.tick(60)
