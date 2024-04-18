import pygame as pg


class Game:
    def __init__(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass

    def main_loop(self):
        while True:
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.main_loop()

