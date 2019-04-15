import run
import pygame as pg
import sys

class Menu(object):
    def __init__(self):
        self.screen = pg.display.set_mode((0,0),pg.FULLSCREEN)
        pg.font.init()
        pg.display.set_caption("Main Menu")
        pg.font.init()
        self.click = (0,0)
        self.size = self.screen.get_size()
        self.pos = (self.size[0] / 2, self.size[1] / 2)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    run.Game()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.click = pg.mouse.get_pos()
                    if (self.click[0] > self.circlee.bottomleft[0]) and (
                        self.click[0] < self.circlee.bottomright[0]) and (
                        self.click[1] > self.circlee.topleft[1]) and (
                        self.click[1] < self.circlee.bottomright[1]):
                            self.diffile = open("diff.txt", "w")
                            self.poziom = "Easy"
                            self.diffile.write(self.poziom)
                            self.diffile.close()

                    if (self.click[0] > self.circlem.bottomleft[0]) and (
                        self.click[0] < self.circlem.bottomright[0]) and (
                        self.click[1] > self.circlem.topleft[1]) and (
                        self.click[1] < self.circlem.bottomright[1]):
                            self.diffile = open("diff.txt", "w")
                            self.poziom = "Medium"
                            self.diffile.write(self.poziom)
                            self.diffile.close()

                    if (self.click[0] > self.circleh.bottomleft[0]) and (
                        self.click[0] < self.circleh.bottomright[0]) and (
                        self.click[1] > self.circleh.topleft[1]) and (
                        self.click[1] < self.circleh.bottomright[1]):
                            self.diffile = open("diff.txt", "w")
                            self.poziom = "Hard"
                            self.diffile.write(self.poziom)
                            self.diffile.close()

            self.screen.fill((0, 0, 0))

            myfont = pg.font.SysFont('Comic Sans MS', 80)
            textsurface = myfont.render("Gooood Spaceable", True, (222, 132, 50))
            self.screen.blit(textsurface, (self.pos[0] - 356, self.pos[1] - 200))

            myfont = pg.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render("Press <space> to play!", True, (50, 180, 130))
            self.screen.blit(textsurface, (self.pos[0]-170,self.pos[1]+100))

            self.circlee = pg.draw.circle(self.screen,(59,170,70),(int(self.pos[0]-80),int(self.pos[1]-30)),20)
            self.circlem = pg.draw.circle(self.screen,(200,200,20),(int(self.pos[0]-20),int(self.pos[1]-30)),20)
            self.circleh = pg.draw.circle(self.screen,(170,70,80),(int(self.pos[0]+40),int(self.pos[1]-30)),20)

            diffread = open("diff.txt", "r")
            diffread = diffread.read()

            myfont = pg.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render("Difficulty: "+str(diffread), True, (200, 160, 220))
            self.screen.blit(textsurface, (self.pos[0]-140 , self.pos[1] ))

            myfont = pg.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render("Use <w,s,a,d> or <arrows> to move and <space> to shoot!", True, (50, 100, 130))
            self.screen.blit(textsurface, (self.pos[0] - 390, self.pos[1] + 60))

            pg.display.flip()

menu = Menu()