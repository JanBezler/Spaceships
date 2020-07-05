import pygame as pg
import sys
import time
from rocket import Rocket
from bullet import Bullet
from enemy import Enemy
from collision import Collision
from os import path
from os import system

class Game(object):
    def __init__(self):
        # Configuracja
        self.max_tps= 100.0
        self.res=(1080,720)
        # Inicjalizacja
        self.screen = pg.display.set_mode((0,0),pg.FULLSCREEN)
        #self.screen = pg.display.set_mode((1000,750))

        pg.init()
        pg.display.set_caption("Game")
        self.tps_clock= pg.time.Clock()
        self.tps_delta= 0.0
        self.bulletsList = list()
        self.enemyList=list()
        img_dir = path.join(path.dirname(__file__), "img/")
        eeg_dir = path.join(path.dirname(__file__), "img/eeg/")
        sound_dir = path.join(path.dirname(__file__), "sound/")

        diff = open("diff.txt","r")
        self.diff = diff.read()
        diff.close()

        self.tomekr=pg.image.load(eeg_dir+"TTr.png")
        self.tomekl=pg.image.load(eeg_dir+"TTl.png")
        self.eship=pg.image.load(img_dir+"eship.png")
        self.pship=pg.image.load(img_dir+"pship.png")
        self.bullimg=pg.image.load(img_dir+"bullet.png")
        self.background=pg.image.load(img_dir+"background2.jpg")
        self.jeden=pg.image.load(eeg_dir+"1ka.png")
        self.eeglist = [pg.image.load(eeg_dir+"en1.png"),pg.image.load(eeg_dir+"en2.png"),pg.image.load(eeg_dir+"en3.png"),
                        pg.image.load(eeg_dir+"en4.png"),pg.image.load(eeg_dir+"en5.png"),pg.image.load(eeg_dir+"en6.png"),
                        pg.image.load(eeg_dir+"en7.png"),pg.image.load(eeg_dir+"en8.png"),pg.image.load(eeg_dir+"en9.png"),
                        pg.image.load(eeg_dir+"en10.png")]

        self.explist = [pg.image.load(img_dir+"expl1.png"),pg.image.load(img_dir+"expl2.png"),
                            pg.image.load(img_dir+"expl3.png"),pg.image.load(img_dir+"expl4.png"),
                            pg.image.load(img_dir+"expl5.png"),pg.image.load(img_dir+"expl6.png"),
                            pg.image.load(img_dir+"expl7.png"),pg.image.load(img_dir+"expl8.png")]

        self.expsound = pg.mixer.Sound(sound_dir+"bum.wav")
        self.shootsound = pg.mixer.Sound(sound_dir+"shoot.wav")
        self.rocketexpsound = pg.mixer.Sound(sound_dir+"rocketbum.wav")
        self.lbsb = pg.mixer.Sound(eeg_dir+"lbsb.wav")
        pg.mixer.music.load(sound_dir+"soundtrack.mp3")
        pg.mixer.music.play(-1)

        self.green=(80,180,30)
        self.orange=(230,70,10)
        self.white=(255,255,255)
        self.tom = 0

        self.player= Rocket(self)
        self.bullet= Bullet(self,self.player)
        self.enemy = Enemy(self,self.player,self.bullet)
        self.collision = Collision(self, self.player, self.bullet, self.enemy)



        while True:
            # Obsluga zdarzen
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pg.KEYDOWN and event.key == pg.K_r:
                    system("Start.exe")
                    sys.exit(0)
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    in_bullet = Bullet(self, self.player)
                    in_bullet.shoot()
                    self.bulletsList.append(in_bullet)
                elif event.type == pg.KEYDOWN and event.key == pg.K_q:
                    in_enemy = Enemy(self,self.player,self.bullet)
                    in_enemy.enemymake()
                    self.enemyList.append(in_enemy)

            if self.diff == "Easy":
                self.enemies = 5 + int(time.process_time()/9)
            elif self.diff == "Medium":
                self.enemies = 7 + int(time.process_time()/6.5)
            elif self.diff == "Hard":
                self.enemies = 9 + int(time.process_time()/5)

            # Taktowanie
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1/self.max_tps:
                self.tick()
                self.tps_delta -= 1/self.max_tps

            # Renderowanie
            if self.tom == 1:
                self.screen.fill((0, 0, 0))
            elif self.tom == 0:
                self.screen.fill((0, 0, 0))
                #self.screen.blit(self.background,(0,0))
            self.draw()
            pg.display.flip()


    def tick(self):
        for item in self.bulletsList:
            item.tick()

        self.player.tick()
        self.collision.tick()

        for item in self.enemyList:
            item.tick()

        if self.player.pressed[pg.K_t] and self.player.pressed[pg.K_y]:
            if self.tom == 0:
                self.lbsb.play()
            self.tom = 1

        if len(self.enemyList) < self.enemies:
            in_enemy = Enemy(self, self.player, self.bullet)
            in_enemy.enemymake()
            self.enemyList.append(in_enemy)

    def draw(self):
        for item in self.bulletsList:
            item.draw()
        for item in self.enemyList:
            item.draw()

        self.player.draw()
        self.collision.draw()

if __name__ == "__main__":
    Game()