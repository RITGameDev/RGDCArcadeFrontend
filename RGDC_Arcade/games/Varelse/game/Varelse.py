"""
Varelse
By Dakota Madden-Fong
More Info in the Readme
"""
import pygame
import time
import random
print ("""Incoming Message From the Hegemon Command Station:
You, Brother, Have been Chosen to Defend the People
of the World from the Evil Space Buggers. Good Luck!
""")

name = "Joey"

pygame.init()
pygame.display.set_caption('Varlese')
start=time.time()
pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(),10)
clandestine = False
screenW=700
screenH=500
screen=pygame.display.set_mode((screenW,screenH))
pygame.mixer.init()
laser=pygame.mixer.Sound("data/laser.wav")
ex=pygame.mixer.Sound("data/ex.wav")
music=pygame.mixer.Sound("data/music.wav")
done=False
pos = (0,0)
toggle = 0
bn = 0
score = 0

enemy_images=["data/sa.png","data/sa2.png","data/sa3.png"]
class Sprite:
        def __init__(self,image_path="data/sa.png"):
                self.direction=1
                self.slowness=1
                self.x=0
                self.y=0
                self.image=pygame.image.load(image_path)
                self.image=pygame.transform.scale(self.image,(30,30))
                self.width=30
                self.height=30
        def update(self):
                if random.randint(1,750) == 1:
                        enemybullet = Enemybullet()
                        sprite_list.append(enemybullet)
                        enemybullet.x=self.x+15
                        enemybullet.y=self.y+30
                if toggle%self.slowness==0:
                        if self.x<0:
                                self.direction=1
                        elif self.x>screenW-self.width:
                                self.direction=-1
                        if self.y<screenH+150: #change to 'screenH-150' if want bad guys to stop going L/R before end
                                self.x+=self.direction
                        self.y+=.1
                if self.y > screenH+self.width:
                        sprite_list.remove(self)

class Alien(Sprite):
        def __init__(self,x,y,slowness):
                Sprite.__init__(self,enemy_images[random.randrange(0,len(enemy_images))])
                self.x=x
                self.y=y
                self.slowness=slowness
                sprite_list.append(self)
                self.alien=True

class Rectangle:
        def __init__(self,x,y,width,height):
                self.left = x
                self.top = y
                self.bottom = y+height
                self.right = x+width
def rectangular_intersection(rect1,rect2):
        return not (rect1.right < rect2.left or rect1.left > rect2.right or rect1.bottom < rect2.top or rect1.top > rect2.bottom)

class Player(Sprite):
        global cheat
        def __init__(self):
                Sprite.__init__(self,"data/p.png")
                self.image=pygame.transform.scale(self.image,(30,30))
                self.x=screenW/2
                self.y=screenH-80
                self.width =30
                self.height=30
                self.speedx=0
                self.speedy=0
        def update(self):
                self.x=self.x+self.speedx
                self.y=self.y+self.speedy
                if self.x < 0:
                        self.x-=self.speedx
                if self.x > screenW-30:
                        self.x-=self.speedx
                for sprite in sprite_list:
                        if sprite != self and not hasattr(sprite,"bullet"):
                                self_rectangle = Rectangle(self.x,self.y,self.width,self.height)
                                other_rectangle=Rectangle(sprite.x,sprite.y,sprite.width,sprite.height)
                                if rectangular_intersection(self_rectangle,other_rectangle)and clandestine== False:
                                                global done
                                                done=True

class Bullet(Sprite):
        def __init__(self):
                Sprite.__init__(self,"data/b.png")
                self.image=pygame.transform.scale(self.image,(8,12))
                self.width=8
                self.height=12
                self.bullet = True
                laser.play()
        def update(self):
                global bn, score
                kill_list = []
                self_rectangle = Rectangle(self.x,self.y,self.width,self.height)
                for sprite in sprite_list:
                        if hasattr(sprite,"alien"):
                                other_rectangle=Rectangle(sprite.x,sprite.y,sprite.width,sprite.height)
                                if rectangular_intersection(self_rectangle,other_rectangle):
                                        kill_list.append(sprite)
                                        ex.play()
                                        if self not in kill_list:
                                                kill_list.append(self)
                                                bn-=1
                        if hasattr(sprite,"enemybullet"):
                                other_rectangle=Rectangle(sprite.x,sprite.y,sprite.width,sprite.height)
                                if rectangular_intersection(self_rectangle,other_rectangle):
                                        kill_list.append(sprite)
                                        if self not in kill_list:
                                                kill_list.append(self)
                                                bn-=1
                if self.y < 0:
                        kill_list.append(self)
                        bn-=1
                for sprite in kill_list:
                        if sprite in sprite_list:
                                sprite_list.remove(sprite)
                                if hasattr(sprite,"alien"):
                                        score+=100
                self.y-=1

class Enemybullet(Sprite):
        def __init__(self):
                Sprite.__init__(self,"data/eb.png")
                self.image=pygame.transform.scale(self.image,(8,12))
                self.width=8
                self.height=12
                self.enemybullet = True
        def update(self):
                kill_list = []
                if self.y > screenH:
                        kill_list.append(self)
                for sprite in kill_list:
                        if sprite in sprite_list:
                                sprite_list.remove(sprite)
                self.y+=1

starimg=pygame.image.load ("data/star.jpg").convert()
star=pygame.transform.scale (starimg,(screenW,screenH))
start=time.time()

def draw_frame(alist,toggle):
        global score
        global name
        global start
        pygame.draw.rect(screen,(0,0,0),screen.get_rect())
        screen.blit(star,(0,0))
        times = time.time()-start
        timem = font.render(str(times),True,(255,255,255))
        screen.blit(timem,(10,screenH-20))
        timew = font.render("TIME",True,(255,255,255))
        screen.blit(timew,(10,screenH-40))
        scorenumber = font.render(str(score),True,(255,255,255))
        screen.blit(scorenumber,(10,screenH-60))
        scorem = font.render("SCORE",True,(255,255,255))
        screen.blit(scorem,(10,screenH-80))
        namem = font.render(str(name),True,(255,255,255))
        screen.blit(namem,(10,screenH-100))
        for sprite in alist:
                position = (sprite.x,sprite.y)
                screen.blit(sprite.image,position)
        pygame.display.flip()

def update_sprites():
        global toggle,randomcreation,lastupdate
        toggle=(toggle+1)
        if random.randint(1,250) == 1:
                alien = Alien(random.randint(0,screenW-50),random.randint(50,250),random.randint(1,3))
        for sprite in sprite_list:
                sprite.update()
sprite_list = []
for x in range(5):
        Alien(random.randint(0,screenW-50),random.randint(50,250),random.randint(1,3))

print ("BEGIN\n")
player = Player()
sprite_list.append(player)
music.play()
channel=music.play()
randomcreation=500
lastupdate=time.time()

while not done:
        if not channel.get_busy():
                channel=music.play()
        for event in pygame.event.get():
                if random.randint(1,1000) == 1:
                        alien = Alien(random.randint(0,screenW-50),random.randint(50,250),random.randint(1,3))
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                if bn<5:
                                        bullet = Bullet()
                                        sprite_list.append(bullet)
                                        bullet.x=player.x+11
                                        bullet.y=player.y
                                        bn+=1
                                        alien = Alien(random.randint(0,screenW-50),random.randint(50,250),random.randint(1,3))
                        if event.key==pygame.K_LEFT:
                                player.speedx=-2
                        if event.key==pygame.K_RIGHT:
                                player.speedx=2
                        if event.key==pygame.K_q:
                                clandestine=True
                        if event.key==pygame.K_w:
                                clandestine=False
                if event.type==pygame.KEYUP:
                        if event.key==pygame.K_LEFT:
                                player.speedx=0
                        if event.key==pygame.K_RIGHT:
                                player.speedx=0
                if bn < 0:
                        bn=0
                if event.type == pygame.QUIT:
                        done=True
                if done is True:
                        break
        draw_frame(sprite_list,0)
        update_sprites()

'''print ("SOLDIER:")
print (name)
print ("SCORE:")
print (score)
print ("TIME:")
print (time.time()-start,"\n")'''
pygame.quit()
'''end = None
hile end != "0":
    end = input("Enter 0 to quit: ")
    if end == "0":
            break
print("END")'''
quit
