import pygame
pygame.init()
from menu import Menu, Gameover
from game import Game

class Main:

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('assets/sounds/dbsound.ogg')
    pygame.mixer.music.play(-1)

    def __init__(self, sizex, sizey, title):
        self.window = pygame.display.set_mode([sizex,sizey])
#        self.title = pygame.display.set_caption("Dragonball Z")

        self.menu = Menu("assets/imenu.png")
        self.game = Game()
        self.gameover = Gameover("assets/losegame.png")

        self.loop = True
        self.fps = pygame.time.Clock()

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if not self.menu.change_scene:
                self.menu.events(events)
            elif not self.game.change_scene:
                self.game.gohan.move_gohan(events)
            else:
                self.gameover.events(events)
#-------------------------------------------------
    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        elif not self.gameover.change_scene:
            self.gameover.draw(self.window)
        else:
            self.menu.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.gohan.life = 3
            self.game.score = 0
#-----------------------------------------
    def update(self):
        while self.loop:
            self.fps.tick(60)
            self.events()
            self.draw()
            pygame.display.update()
#---------------------------------------------------

game = Main(1920,1072,"Dragonball Z")
game.update()
