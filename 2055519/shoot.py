#Create your own shooter

from pygame import *
from random import randint
font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255,255,255))
lose = font1.render('YOU LOSE!', True, (100,0,0))
font2  =font.Font(None, 36)
mixer.init()
mixer_music.load('space.ogg')
mixer_music.play()
fire_sound=mixer.Sound('fire.ogg')
img_back="galaxy.jpg"

img_bullet="bullet.png"
img_hero="rocket.png"
img_enemy="ufo.png"
score=0
goal=10
max_lost=0
x_lost=3
class Gamesprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image=transfom.scale(image.load(player_image),(size_x,size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
        def reset(self):
            window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Gamesprite):
    def update(self):
        key=key.get.pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x-=self.speed
        if keys[k_RIGHT] and self.rect.x<5:
            self.rect.x+=self.speed
    def fire(self):
        bullet=Bullet(img_bullet,self.rect.centerx,self.rect.top,15,20,-15)
        bullet.add(bullet)
class Enemy(Gamesprite):
    def update(self):
        self.rect.y+=self.speed
        global lost
        if self.rect.y> win_height:
            self.rect.x=randint(80,win_width-80)
            self.rect.y=0
            lost=lost+1
class Bullet(Gamesprite):
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y<0:
            self.kill()
        win_width=700
        win_height=500
        display.set_caption("Shooter")
        window=display.set.mode((win_width,win_height))
        background=transform.scale(image.load(img_vack),(win_width.win_height))
        ship=Player(img_hero,5,win_height-100,80,100,10)
        monsters=sprite.Group()
        for i in range (1, 6):
            monsters=Enemy(img_enemy,randint(80,win_Width,-80),-40,80,50,randint(1, 5))
            monsters.add(monster)
        bullet=sprite.Group()
        finish = False
        run = True
        while run:
            for e in event.get():
                if e.type==QUIT:
                    run=False
                elif e.type == KEYDOWN:
                    if e.key == K_SPACE:
                        fire_sound.play()
                        ship.fire()
            if not finish:
                window.blit(background,(0, 0))
                text=font2.render("Score:"+str(score),1,(255,255,255))
                text_lose=font2.render("Missed:"+str(lost),1,(255,255,255))
                window.blit(text_lose,(10,50))
                ship.update()
                monsters.update()
                bullets.update()
                ship.reset()
                monsters.draw(Window)
                bullets.draw(window)
                collides=sprite.groupcollide(monsters,bullets,True,True)
                for c in collides:
                    score=score+1
                    monster=Enemy(img_enemy.randint(80,win_Width-80),-40,80,50,randint(1,5))
                    monsters.add(monster)
                if sprite.spritecollide(Ship,monsters,False)or lost>=max_lost:
                    finish = True
                    window.blit(lose,(200,200))
                if score>=goal:
                    finish=True
                    window.blit(win,(200,200))
            display.update()
time.delay(50)