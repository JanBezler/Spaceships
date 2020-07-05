import pygame as pg
from pygame.math import Vector2
import random
import time

class Enemy(object):
    def __init__(self, game,player,bullet):
        self.game = game
        self.player=player
        self.bullet=bullet
        self.resistance = 0.998
        self.size = self.game.screen.get_size()
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.tm=0

        self.ranen = int(random.random()*10)
        randpos = int(random.random() * 100)
        if randpos <=6 :   #11
            self.pos = Vector2(self.size[0], self.size[1] / 2)
        elif randpos <=12 : #1
            self.pos = Vector2(0, 0)
        elif randpos <=18 : #16
            self.pos = Vector2(self.size[0]/4, 0)
        elif randpos <=25 : #7
            self.pos = Vector2(self.size[0]/2, self.size[1])
        elif randpos <=31 : #2
            self.pos = Vector2(0, self.size[1]/4)
        elif randpos <= 37: #10
            self.pos = Vector2(self.size[0], self.size[1]/4*3)
        elif randpos <= 43: #6
            self.pos = Vector2(self.size[0]/4, self.size[1])
        elif randpos <= 50: #15
            self.pos = Vector2(self.size[0]/2, 0)
        elif randpos <= 56: #3
            self.pos = Vector2(0, self.size[1]/2)
        elif randpos <= 62: #12
            self.pos = Vector2(self.size[0], self.size[1]/4)
        elif randpos <= 68: #14
            self.pos = Vector2(self.size[0]/4*3, 0)
        elif randpos <= 74: #8
            self.pos = Vector2(self.size[0]/4*3, self.size[1])
        elif randpos <= 81: #4
            self.pos = Vector2(0, self.size[1]/4*3)
        elif randpos <= 87: #13
            self.pos = Vector2(self.size[0], 0)
        elif randpos <= 93: #9
            self.pos = Vector2(self.size[0], self.size[1])
        elif randpos <= 100: #5
            self.pos = Vector2(0, self.size[1])

    def enemymake(self):
        self.points = [Vector2(3, 6), Vector2(0, 7), Vector2(-3, 6), Vector2(-1, -5), Vector2(-0, -6), Vector2(1, -5)]
        self.angle = int(self.vel.angle_to(Vector2(0, 1)))
        self.points = [p.rotate(self.angle) for p in self.points]
        self.points = [Vector2(p.x, p.y * -1) for p in self.points]
        self.points = [self.pos + p * 5 for p in self.points]

    def tick(self):

        if self.game.diff == "Hard":
            self.vel *= self.resistance
            self.vel += self.acc
            self.pos += self.vel*1.8
            self.acc *= 0
        else:
            self.vel *= self.resistance
            self.vel += self.acc
            self.pos += self.vel
            self.acc *= 0

        if int(float(time.process_time())*10) > self.tm+5:
            self.tm=int(float(time.process_time())*10)

            ran1=random.random()
            ran2=random.random()

            if int(random.random()*10)<5:
                ran1*=-1
            if int(random.random()*10)<5:
                ran2*=-1

            self.vel[0] -= ran1
            self.vel[1] -= ran1

        if self.pos.x <= 0:
            self.pos.x = 0
            self.vel[0]=1
            self.vel[1]=0
        if self.pos.y <= 0:
            self.pos.y = 0
            self.vel[0] =0
            self.vel[1] =1
        if self.pos.x >= self.size[0]:
            self.pos.x = self.size[0]
            self.vel[0] =-1
            self.vel[1] =0
        if self.pos.y >= self.size[1]:
            self.pos.y = self.size[1]
            self.vel[0] =0
            self.vel[1] =-1




    def draw(self):
        self.enemymake()
        if self.game.tom==0:
            #self.foe = pg.draw.polygon(self.game.screen, self.game.white, self.points)
            self.foe = self.game.screen.blit(pg.transform.rotate(self.game.eship, self.angle +180),(self.pos[0] - 30, self.pos[1] - 30))
        if self.game.tom==1:
            self.foe = self.game.screen.blit(pg.transform.rotate(self.game.eeglist[self.ranen], self.angle + 90),(self.pos[0] - 30, self.pos[1] - 30))