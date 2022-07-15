
import pygame
import time
import random
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((1100,700))
pygame.display.set_caption('Spac Vadré')
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
img1=pygame.image.load("vaderb2.png")
img2=pygame.image.load("vaderb2.png")
img3=pygame.image.load("vaderc1.png")
img=pygame.image.load("space.png")

img = pygame.transform.scale(img,(100,100))
img4=pygame.image.load('bullet.png')
img4 = pygame.transform.scale(img4,(10,35))
img5=pygame.image.load('shoot.png')
img5 = pygame.transform.scale(img5,(10,35))
class invaders:
    def __init__(self,x,y,img):
        self.x=x
        self.y=y
        self.img = img
        self.b_x=x
        self.b_y=y
        self.b_img5 =pygame.transform.scale(img5,(10,35))
    def draw(self):
        screen.blit(self.img,(self.x,self.y))

    def move(self,movex,movey):
        if movex == 'right':
            self.x += 1
        if movex == 'left':
            self.x -= 1
        self.y =movey
        
class player:
    def __init__(self,img):
        self.x=500
        self.y=600
        self.img=img
        self.movex = 0
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
    def move(self):
        self.x += self.movex
        
class bullet:
    def __init__(self, x,y,img, m):
        self.x= x
        self.y= y
        self.img=img
        self.m =m
    def draw(self):
        screen.blit(self.img,(self.x+43,self.y))
    def move(self):
        if self.m == 'up':
            self.y -= 1
        if self.m == 'down':
            self.y += 1
invader1=[]
invader2=[]
invader3=[]
bullet_list=[]
for i in range(0,1024,128):
    print(i)
    invader1.append(invaders(i,20,img1))
    invader2.append(invaders(i,80,img2))
    invader3.append(invaders(i,140,img3))

shoot1=random.choice(invader1)
shoot2=random.choice(invader2)
shoot3=random.choice(invader3)
        
flag =0        
signal =0
movex1=movex2=movex3='left'
movey1=20
movey2=80
movey3=140
space=player(img)
while True:
    pygame.time.wait(10)
    pygame.display.update()
    screen.fill(black)


    space.move()
    space.draw()

   
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                space.movex = -1
            if event.key==K_RIGHT:
                space.movex = 1
            if event.key==K_SPACE:
                bullet_list.append(bullet(space.x,570,img4,'up'))
        if event.type==KEYUP:
            if event.key==K_LEFT:
                space.movex = 0
            if event.key==K_RIGHT:
                space.movex = 0

                
            
    for x in invader1:

        if random.randint(1,3000)==1:
            bullet_list.append(bullet(x.x-20,x.y+40,pygame.transform.flip(img4,False,True),'down'))
        
        x.draw()
        
            
    
        x.move(movex1,movey1)
        
        if x.x <0:
            movex1='right'
            movey1 += 5
            
        if x.x >1000:
            movex1='left'
            movey1 += 5
        
    for x in invader2:
        if random.randint(1,3000)==1:
            bullet_list.append(bullet(x.x-20,x.y+40,pygame.transform.flip(img4,False,True),'down'))
       
        x.draw()
        x.move(movex2,movey2)
        if x.x <0:
            movex2='right'
            movey2 += 5
            
        if x.x >1000:
            movex2='left'
            movey2 += 5

    for x in invader3:
        if random.randint(1,3000)==1:
            bullet_list.append(bullet(x.x-20,x.y+40,pygame.transform.flip(img4,False,True),'down'))
        x.draw()
        x.move(movex3,movey3)
        if x.x <0:
            movex3='right'
            movey3 += 5
            
        if x.x >1000:
            movex3='left'
            movey3 += 5
    
        
    for b in bullet_list:
        if b.m=='down' and b.x in range(space.x-50,space.x+50) and b.y in range(space.y,space.y+50):
            print('collision')
        
        if b.m=='down' and b.y <0:
            bullet_list.remove(b)
        b.move()
        b.draw()
        for a in invader1:
            if b.m=='up' and b.x in range(a.x-20,a.x+20) and b.y in range(a.y,a.y+50):
                if b in bullet_list:
                    bullet_list.remove(b)
                if a in invader1:
                    invader1.remove(a)
        for a in invader2:
            if b.m=='up' and b.x in range(a.x-20,a.x+20) and b.y in range(a.y,a.y+50):
                if b in bullet_list:
                    bullet_list.remove(b)
                if a in invader2:
                    invader2.remove(a)
        for a in invader3:
            if b.m=='up' and b.x in range(a.x-20,a.x+20) and b.y in range(a.y,a.y+50):
                if b in bullet_list:
                    bullet_list.remove(b)
                if a in invader3:
                    invader3.remove(a)




