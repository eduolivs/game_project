import pygame
from obj import Obj
from game import Game


class Menu:

    def __init__(self, image):

        self.start_screen = Obj(image, 0, 0)

        self.change_scene = False

    def draw(self, window):
        self.start_screen.group.draw(window)


    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True
                print(self.change_scene)


class Gameover(Menu):
    def __init__(self, image):
        super().__init__(image)
