import sys
from typing import Callable
import pygame as pg
from input_handler import InputHandler
from settings import RES, FPS
from grid import Grid


class Game:
    EVENT_HANDLERS: dict[tuple[int, int], Callable] = {}

    def __init__(self):
        self.screen: pg.Surface = pg.display.set_mode(RES)
        self.clock: pg.time.Clock = pg.time.Clock()
        self.input_handler: InputHandler = InputHandler(Game.EVENT_HANDLERS)
        pg.display.set_caption("Pathfinding visualizer")
        self.grid: Grid = Grid(self)

    def draw(self) -> None:
        pass

    def update(self) -> None:
        self.input_handler.check_events()

    def main_loop(self) -> None:
        while True:
            self.update()
            self.draw()
            self.clock.tick(FPS)

    @staticmethod
    def quit() -> None:
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.main_loop()
