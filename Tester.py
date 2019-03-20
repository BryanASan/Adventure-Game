import pygame
import sys, os, random , math, time
from pygame.locals import *

ScreenHeight= 800
ScreenWidth= 1400
objects=[]
BLACK = (0 ,0, 0)
BLUE = (0,0,255)
RED = (255,0,0)
velocity = 5

class Player(pygame.sprite.Sprite):
    def __init__(self,colour):
        super().__init__()
        pygame.draw.circle(screen, colour, [400,250],40)
        self.x= 400
        self.y=250
        self.rect= pygame.Rect(self.x,self.y, 40,40)
        self.hspeed=0
        self.vspeed=0
        self.colour=colour

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and self.y < ScreenHeight-40: #down key
            self.y+= velocity
        elif key[pygame.K_UP] and self.y > velocity+40: # up key
            self.y-=velocity
        if key[pygame.K_RIGHT] and self.x < ScreenWidth - 40: # right key
            self.x+=velocity
        elif key[pygame.K_LEFT] and self.x > velocity+ 40:# left key
            self.x-=velocity
        pygame.draw.circle(screen, BLUE, [self.x,self.y],40)
        
        #pygame.display.update()

    def draw(self):
        pygame.draw.circle(screen, self.colour, [self.x, self.y],40)


    def change_speed(self, hspeed, vspeed):
        self.hspeed+=hspeed
        self.vspeed += vspeed


                
    def update(self, collidable):

        self.rect.x +=self.hspeed
        collision_list= pygame.sprite.spritecollide(self,collidable, False)

        for collided_object in collision_list:
            if (self.hspeed > 0): #collision to the right
                self.rect.right = collided_object.rect.left
            elif (self.hspeed <0): #colliison to the left
                self.rect.left = collided_object.rect.right

        self.rect.y +=self.vspeed
        collision_list= pygame.sprite.spritecollide( self, collidable, False)

        for collided_object in collision_list:
            if (self.vspeed>0 ): #Collision down from player
                self.rect.bottom = collided_object.rect.top
            elif ( self.vspeed < 0): #collision above player
                self.rect.top = collided_object.rect.bottom
        
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, 40,40) #returns rectangle hitbox of player
 
class Enemy(Player):
    def __init__(self,colour,x,y, velocity):
        super().__init__(colour)
        pygame.draw.circle(screen, colour, [x,y], 40)
        self.EnemyVelocity= velocity
        self.x=x
        self.y=y
        self.rect= pygame.Rect(self.x, self.y, 40, 40)


    def move_towards_player(self,player):
        difference_in_x= self.x-player.x
        difference_in_y= self.y-player.y
        if difference_in_x<0:
            self.x += 1
        elif difference_in_x>0:
            self.x -= 1
        if difference_in_y<0:
            self.y += 1
        elif difference_in_y>0:
            self.y -= 1
''' centre position1 , centre position2 , radius1 ,radius2
x=centre position difference
y= centre position difference

distance= sqrt((x)**2+(y)**2)
collide if distance < radius1+ radius2 
'''

 

def draw_all():
    for number in range (0, len(objects)):
        objects[number].draw()
        pygame.display.update

pygame.init()
screen = pygame.display.set_mode((1400,800))
screen.fill((255,255,255))   
player = Player(BLUE)
slime = Enemy(RED,500,500,1)
clock= pygame.time.Clock()

objects.append(player)
objects.append(slime)

collidable_objects = pygame.sprite.Group()
collidable_objects.add(slime)

running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                player.change_speed(-5,0)
            if event.key ==pygame.K_RIGHT:
                player.change_speed(5,0)
            if event.key ==pygame.K_UP:
                player.change_speed(0,-5)
            if event.key ==pygame.K_DOWN:
                player.change_speed(0,5)
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_LEFT:
                player.change_speed(5,0)
            if event.key ==pygame.K_RIGHT:
                player.change_speed(-5,0)
            if event.key ==pygame.K_UP:
                player.change_speed(0,5)
            if event.key ==pygame.K_DOWN:
                player.change_speed(0,-5)
    
    player.handle_keys()
    slime.move_towards_player(player)
    player.update(collidable_objects)
    draw_all()
    pygame.display.update()
