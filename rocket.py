import pygame as pg
from pygame.math import Vector2

class Rocket(object):
    def __init__(self, game):
        self.game=game
        self.speed= 2/10
        self.gravity= 0
        self.resistance= 0.975

        self.size= self.game.screen.get_size()
        self.pos= Vector2(self.size[0]/2,self.size[1]/2)
        self.vel= Vector2(0,0)
        self.acc= Vector2(0,0)

    def add_force(self, force):
        self.acc += force

    def tick(self):
        # Wejście
        self.pressed= pg.key.get_pressed()
        if self.pressed[pg.K_w] or self.pressed[pg.K_UP]:
            self.add_force(Vector2(0,-self.speed))
        if self.pressed[pg.K_s] or self.pressed[pg.K_DOWN]:
            self.add_force(Vector2(0,self.speed))
        if self.pressed[pg.K_a] or self.pressed[pg.K_LEFT]:
            self.add_force(Vector2(-self.speed,0))
        if self.pressed[pg.K_d] or self.pressed[pg.K_RIGHT]:
            self.add_force(Vector2(self.speed,0))

        # Fizyka
        self.vel *= self.resistance
        self.vel -= Vector2(0,-self.gravity)
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

        # Ramka
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
        # Trójkąt

        self.points= [Vector2(0,-10),Vector2(-5,5),Vector2(5,5)]  # Wierzchołki
        self.angle= int(self.vel.angle_to(Vector2(0,1)))  # Obrót
        self.points= [p.rotate(self.angle) for p in self.points]
        self.points= [Vector2(p.x,p.y*-1) for p in self.points]
        self.points= [self.pos+p*2 for p in self.points]  # Pozycja

        if self.game.tom == 0:
            #pg.draw.polygon(self.game.screen,self.game.green,self.points) # Rysowanie Trójkąta
            self.game.screen.blit(pg.transform.rotate(self.game.pship, self.angle),(self.pos[0] - 26, self.pos[1] - 22.5))

        if self.game.tom==1:
            if self.angle >= 180 or self.angle <0:
                self.game.screen.blit(pg.transform.rotate(self.game.tomekl, self.angle + 90),(self.pos[0] - 30, self.pos[1] - 30))
            else:
               self.game.screen.blit(pg.transform.rotate(self.game.tomekr, self.angle - 90),(self.pos[0] - 30, self.pos[1] - 30))