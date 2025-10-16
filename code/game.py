from obj import Obj,Gohan, Text
import random
class Game:
    def __init__(self):
        self.scenario = Obj("assets/scenario.png", 0, 0)
        self.scenario_2 = Obj("assets/scenario.png", 0, -1024)

        self.power = Obj("assets/power1.png", random.randrange(3, 1850), -50)
        self.esfera = Obj("assets/esfera1.png", random.randrange(3, 1850), -50)
        self.gohan =Gohan("assets/gohan1.png", 650, 900)
        self.change_scene = False
        self.score_value = Text(100, "0")
        self.life = Text(100, "3")

    def draw(self, window):
        self.scenario.drawing(window)
        self.scenario_2.drawing(window)
        self.gohan.drawing(window)
        self.power.drawing(window)
        self.esfera.drawing(window)
        self.score_value.draw(window, 10, 10)
        self.life.draw(window, 10, 100)

    def update(self):
        self.move_scenario()
        self.power.anim("power", 18, 5)
        self.esfera.anim("esfera", 10, 3)
        self.gohan.anim("gohan", 8, 5)
        self.move_power()
        self.move_esfera()
        self.gohan.colision(self.power.group, "power")
        self.gohan.colision(self.esfera.group, "esfera")
        self.game_over()
        self.score_value.update_text(str(self.gohan.score_value))
        self.life.update_text(str(self.gohan.life))


    def move_scenario(self):
        self.scenario.sprite.rect[1] += 60
        self.scenario_2.sprite.rect[1] += 60

        if self.scenario.sprite.rect[1] >= 1072:
            self.scenario.sprite.rect[1] = 0
        if self.scenario_2.sprite.rect[1] >= 0:
            self.scenario_2.sprite.rect[1] = -1072

    def move_power(self):
        self.power.sprite.rect[1] += 15

        if self.power.sprite.rect[1] >= 1080:
            self.power.sprite.kill()
            self.power = Obj("assets/power1.png", random.randrange(3, 1850), -50)
    def move_esfera(self):
        self.esfera.sprite.rect[1] += 11

        if self.esfera.sprite.rect[1] >= 1080:
            self.esfera.sprite.kill()
            self.esfera = Obj("assets/esfera1.png", random.randrange(3, 1850), -50)



    def game_over(self):
        if self.gohan.life <= 0:
            self.change_scene = True

