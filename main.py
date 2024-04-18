import pygame as pg
from input_handler import InputHandler
from settings import EVENT_HANDLERS, RES, FPS


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.input_handler = InputHandler(EVENT_HANDLERS)
        pg.display.set_caption("Pathfinding visualizer")

    def draw(self):
        pass

    def update(self):
        self.input_handler.check_events()

    def main_loop(self):
        while True:
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.main_loop()
