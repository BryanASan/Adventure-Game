import pygame
import sys, os, random , math, time


ScreenHeight= 800
ScreenWidth= 1400
objects=[]
Inventory=[]
BLACK = (0 ,0, 0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE= (255,255,255)
YELLOW= (200,200,0)
velocity = 2
FootstepsSound= pygame.mixer.Sound('Footsteps.wav')
EnemyHitSound=  pygame.mixer.Sound('D:/WinPython/EnemyHit.wav')
PlayerSwordSwingGruntSound=  pygame.mixer.Sound('D:/WinPython/PlayerSwordSwingGrunt.wav')

class Player(pygame.sprite.Sprite):
    def __init__(self,colour):
        super().__init__()
        pygame.draw.circle(screen, colour, [400,250],40)
        self.radius = 40
        self.x= 400
        self.y=250
        self.rect= pygame.Rect(self.x,self.y, 40,40)
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
        FootstepsSound.play()
        pygame.draw.circle(screen, BLUE, [self.x,self.y],40)
        
        #pygame.display.update()

    def draw(self):
        pygame.draw.circle(screen, self.colour, [self.x, self.y],40)


    def get_rect(self):
        return pygame.Rect(self.x, self.y, 40,40) #returns rectangle hitbox of player

class Enemy(Player):
    def __init__(self,colour,x,y, velocity, vicinity):
        super().__init__(colour)
        pygame.draw.circle(screen, colour, [x,y], 40)
        self.x=x
        self.y=y
        self.rect= pygame.Rect(self.x, self.y, 40, 40)
        self.health= 5
        self.visible= True
        self.vicinity= vicinity
        
    def move_towards_player(self,player):
        if collide_circle(player, slime,1) == False:
            pass
        else:
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

    def draw(self):
        if self.visible:
            pygame.draw.circle(screen, self.colour, [self.x, self.y],40)
            pygame.draw.rect(screen, RED, (self.x-20, self.y-60,50,10))
            pygame.draw.rect(screen, GREEN, (self.x-20, self.y-60, 50- (5*(5-self.health)),10))

    def hit(self):
        if sword in Inventory:
            if self.health >0:
                self.health -=1
                EnemyHitSound.play()
            else:
                self.visible= False
        


def collide_circle(circle1, circle2, extra):
    if extra==1 :
        xDif = circle1.x - circle2.x
        yDif = circle1.y - circle2.y
        distance = math.sqrt(xDif**2 + yDif**2)
        if distance < circle1.radius+(circle2.radius+circle2.vicinity):
            return True
        else:
            return False
    else:
        xDif = circle1.x - circle2.x
        yDif = circle1.y - circle2.y
        distance = math.sqrt(xDif**2 + yDif**2)
        if distance < circle1.radius+circle2.radius:
            slime.hit()
            return True
            
        else:
            return False


class Sword():
    def __init__(self,x,y):
        pygame.draw.circle(screen, YELLOW, (x,y),10)
        self.visible= True
        self.radius=10
        self.x=x
        self.y=y

    
    def draw(self):
        if self.visible:
            pygame.draw.circle(screen, YELLOW, (self.x,self.y),10)

    def pick_up(self):
        if collide_circle(player, sword,0):
            self.visible= False
            Inventory.append(sword)
        else:
            pass



def draw_all():
    for number in range (0, len(objects)):
        objects[number].draw()
        pygame.display.update

pygame.init()
screen = pygame.display.set_mode((1400,800))
screen.fill((255,255,255))   
player = Player(BLUE)
slime = Enemy(RED,500,500,1, 200)
sword = Sword(1000,700)
clock= pygame.time.Clock()

objects.append(player)
objects.append(slime)
objects.append(sword)

collidable_objects = pygame.sprite.Group()
collidable_objects.add(slime)

running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running= False
    player.handle_keys()
    #slime will only move towards player if they are not touching
    if not(collide_circle(player,slime,0)):
        slime.move_towards_player(player)
    sword.pick_up()
    draw_all()
    pygame.display.update()
