import pygame as pg
from pygame.math import Vector2
import winsound

class Bullet(object):
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.angle = 180
        self.bullspeed=Vector2(3,3)

    def shoot(self):
        self.points = [Vector2(0, -10), Vector2(2, 5), Vector2(-2, 5)]  # Wierzchołki
        self.angle = int(self.player.vel.angle_to(Vector2(0, 1))) # Obrót
        self.points = [p.rotate(self.angle) for p in self.points]
        self.points = [Vector2(p.x, p.y*-1) for p in self.points]
        self.points = [self.player.pos+p*1.4 for p in self.points]  # Pozycja
        self.vel = Vector2(self.player.vel[0],self.player.vel[1])

        if not (self.vel[0] < self.bullspeed[0] * 3 / 4 and self.vel[0] > -self.bullspeed[0] * 3 / 4 \
                and self.vel[1] < self.bullspeed[1] * 3 / 4 and self.vel[1] > -self.bullspeed[1] * 3 / 4):
            winsound.Beep(400,20)

    def tick(self):

        for i in range(len(self.points)):
            self.points[i] += (self.vel[0] * self.bullspeed[0], self.vel[1] * self.bullspeed[1])

        if self.vel[0]<self.bullspeed[0]*3/4 and self.vel[0]>-self.bullspeed[0]*3/4 \
                and self.vel[1]<self.bullspeed[1]*3/4 and self.vel[1]>-self.bullspeed[1]*3/4:
            self.game.bulletsList.remove(self)

        if self.points[0][0] <= -20:
            self.game.bulletsList.remove(self)
        elif self.points[0][1] <= -20:
            self.game.bulletsList.remove(self)
        elif self.points[0][0] >= self.player.size[0]+20:
            self.game.bulletsList.remove(self)
        elif self.points[0][1] >= self.player.size[1]+20:
            self.game.bulletsList.remove(self)

    def draw(self):
        if self.game.tom == 0:
            #self.arrow = pg.draw.polygon(self.game.screen,self.game.orange,self.points)
            self.arrow = self.game.screen.blit(pg.transform.rotate(self.game.bullimg, self.angle + 270),
                                               (self.points[0][0]-6, self.points[0][1]-2.5))
            self.game.collision.check_collision(self)
        if self.game.tom == 1:
            self.arrow = self.game.screen.blit(pg.transform.rotate(self.game.jeden , self.angle +180),
                              (self.points[0][0] - 30, self.points[0][1] - 30))
            self.game.collision.check_collision(self)