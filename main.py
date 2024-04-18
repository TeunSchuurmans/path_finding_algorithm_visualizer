import pygame as pg
from input_handler import InputHandler
from settings import EVENT_HANDLERS


class Game:
    def __init__(self):
        self.input_handler = InputHandler(EVENT_HANDLERS)

    def draw(self):
        pass

    def update(self):
        self.input_handler.check_events()

    def main_loop(self):
        while True:
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.main_loop()
