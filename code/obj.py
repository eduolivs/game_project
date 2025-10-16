import pygame


class Obj:

    def __init__(self, image, x, y):

        pygame.mixer.init()
        self.sound_pts = pygame.mixer.Sound('assets/sounds/powercathsound.ogg')
        self.sound_hit = pygame.mixer.Sound('assets/sounds/hitsound.ogg')

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y


        self.frame = 1
        self.tick = 0

    def drawing(self, window):
        self.group.draw(window)

    def anim(self, image, tick, frames):
        self.tick += 1
        if self.tick >= 5:
            self.tick = 0
            self.frame += 1


        if self.frame == frames:
            self.frame = 1

        self.sprite.image = pygame.image.load("assets/" + image + str(self.frame) + ".png")

class Gohan(Obj):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        self.life = 3
        self.score_value = 0
    def move_gohan(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] -100
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] -100


    def colision(self, group, name):

        name = name
        colison = pygame.sprite.spritecollide(self.sprite, group, True)

        if name == "esfera" and colison:
            self.score_value += 1
            self.sound_hit.play()
        elif name == "power" and colison:
            self.life -= 1
            self.sound_pts.play()


class Text:
    def __init__(self, size, text):
        self.font = pygame.font.SysFont("Arial", size)
        self.render = self.font.render(text , True, (255, 255, 0))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def update_text(self, atutext):
        self.render = self.font.render(atutext , True, (255, 255, 0))
