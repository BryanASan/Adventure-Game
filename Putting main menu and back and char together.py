import pygame
import sys, os
import time
import random
from pygame.locals import *



pygame.init()
display_width = 900
display_height = 800
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,128,0)
colour1 = (10,100,20)
colour2 = (14,36,99)
block_color = (53,115,255)

animation=['walking1.png', 'walking2.png','standing.png'] 

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Adventure Man')
clock = pygame.time.Clock()

class Man(object):
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load('standing.png')
        self.image = pygame.transform.scale(self.image, (200,50))
        self.x = 100
        self.y = 100 


    def walking(self):
        for number in range(0,3):
            if number == 3:
                number=0
            self.image = pygame.image.load(animation[number])
            self.image = pygame.transform.scale(self.image, (200,50))
            man.draw(screen)
            pygame.display.update()
            pygame.time.delay(100)
    
    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        #man_pos= pygame.rect.Rect(0,0)
        dist = 100 
        step = dist/2 
        if key[pygame.K_DOWN]:
            newy=self.y+dist
            for i in range (2):
                self.y += step
                self.stay_in_border(self.x, newy)
                self.walking()
                self.stay_in_border(self.x, newy)
        elif key[pygame.K_UP]: # up key
            newy=self.y-dist
            for i in range (2):   
                self.y -= step
                self.stay_in_border(self.x, newy)
                self.walking()# move up
                self.stay_in_border(self.x, newy)
        if key[pygame.K_RIGHT]:
            newx=self.x+dist
            for i in range (2):
                self.x += step
                self.stay_in_border(newx,self.y)
                self.walking()# right key
                self.stay_in_border(newx,self.y)
        elif key[pygame.K_LEFT]:
            newx=self.x-dist
            for i in range (2):
                self.x -= step
                self.stay_in_border(newx,self.y)
                self.walking()# left key
                self.stay_in_border(newx,self.y)

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
        elif self.y >= 500:
            self.y= 500
            pygame.display.update()

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



# x= x location,
#y= y location
#w = button width
#y= button height
#ic =inactive colour(mouse not hovering)
# ac = mouse hovering (active colour)
def button(msg,x,y,width,height,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,width,height))
        if click[0] == 1 and action!= None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,width,height))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(width/2)), (y+(height/2)) )
    gameDisplay.blit(textSurf, textRect)
 
 
#def things_dodged(count):
#    font = pygame.font.SysFont(None, 25)
#    text = font.render("Dodged: "+str(count), True, black)
#    gameDisplay.blit(text,(0,0))
 
#def things(thingx, thingy, thingw, thingh, color):
#    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
#def car(x,y):
#    gameDisplay.blit(carImg,(x,y))
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
    time.sleep(2)
    game_loop()
 
def dead():
    message_display('You died')

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        playbutton= button("Play",200, 200,100,50,green, colour1, game_loop)
        optionbutton= button("Options", 400,200,100,50, red, colour2, game_loop)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Adventure Man", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)        

def game_loop():

    running = True
    while running:
        screen.fill((white)) # fill the screen with white
        screen.blit(BackGround.image, BackGround.rect)
        x,y = pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quit the screen
                running = False
        man.handle_keys() # handle the keys
        man.draw(screen) # draw the man to the screen
        pygame.display.update() # update the screen


pygame.init()
screen = pygame.display.set_mode((1000, 600))
BackGround = Background('background.png', [0,0])
man = Man() # create an instance
clock = pygame.time.Clock()

game_intro()
game_loop()
pygame.quit()
quit()





