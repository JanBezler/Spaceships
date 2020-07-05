import time
import pygame as pg

class Collision(object):

    def __init__(self,game,player,bullet,enemy):
        self.game = game
        self.player = player
        self.bullet = bullet
        self.enemy = enemy
        self.score = 0
        self.tm = 0
        self.gmover=False

    def check_collision(self, arrow):
        if not self.gmover:
            try:
                for item in self.game.enemyList:
                    if (arrow.arrow.center[0] > item.foe.bottomleft[0]) and (
                        arrow.arrow.center[0] < item.foe.bottomright[0]) and (
                        arrow.arrow.center[1] > item.foe.topleft[1]) and (
                        arrow.arrow.center[1] < item.foe.bottomright[1]):
                            self.game.expsound.play()
                            self.coords=item.foe.center
                            self.game.bulletsList.remove(arrow)
                            self.game.enemyList.remove(item)
                            self.score+=1
                            self.i=-1


            except AttributeError:
                pass
            except IndexError:
                pass
            except ValueError:
                pass

    def tick(self):
        if not self.gmover:
            try:
                for item in self.game.enemyList:
                    if (self.player.pos[0] > item.foe.bottomleft[0]) and (
                        self.player.pos[0] < item.foe.bottomright[0]) and (
                        self.player.pos[1] > item.foe.topleft[1]) and (
                        self.player.pos[1] < item.foe.bottomright[1]):
                            self.game.rocketexpsound.play()
                            self.coords = item.foe.center
                            self.game.enemyList.remove(item)
                            self.i = -1
                            self.gmover=True
                            self.yourtime=str(int(time.process_time() * 100) / 100)

            except AttributeError:
                pass
            except IndexError:
                pass
            except ValueError:
                pass

    def draw(self):
        myfont = pg.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(('Score: '+str(self.score)), True, (230, 230, 100))
        self.game.screen.blit(textsurface, (10, 10))

        myfont = pg.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render("Time: " + str(int(time.process_time() * 100) / 100), True, (180, 240, 110))
        self.game.screen.blit(textsurface, (10, 50))

        myfont = pg.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render("Enemies: " + str(self.game.enemies), True, (100, 200, 210))
        self.game.screen.blit(textsurface, (10, 90))

        if self.gmover:
            pg.draw.rect(self.game.screen, (100, 10, 10),
                        pg.Rect(0, 0, self.game.screen.get_size()[0], self.game.screen.get_size()[1]))

            myfont = pg.font.SysFont('Comic Sans MS', 100)
            textsurface = myfont.render("GAME OVER", True, (30, 0, 10))
            self.game.screen.blit(textsurface, (self.game.screen.get_size()[0]/2-300, self.game.screen.get_size()[1]/2-160))

            myfont = pg.font.SysFont('Comic Sans MS', 26)
            textsurface = myfont.render("Press <Esc> to exit or <r> to try again", True, (10, 2, 5))
            self.game.screen.blit(textsurface,
                                  (self.game.screen.get_size()[0]/2-230, self.game.screen.get_size()[1]/2-30))

            myfont = pg.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render(('Your score: ' + str(self.score)), True, (230, 230, 100))
            self.game.screen.blit(textsurface, (self.game.screen.get_size()[0]/2-110, self.game.screen.get_size()[1]/2+100))

            myfont = pg.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render("Your time: " + self.yourtime, True, (180, 240, 110))
            self.game.screen.blit(textsurface, (self.game.screen.get_size()[0]/2-105, self.game.screen.get_size()[1]/2+140))

        if not self.gmover:
            try:
                if int(time.process_time() * 10) > self.tm:
                    self.tm += 0.8
                    self.i+=1

                self.game.screen.blit(self.game.explist[self.i],(self.coords[0]-50,self.coords[1]-50))

            except AttributeError:
                pass
            except IndexError:
                pass
