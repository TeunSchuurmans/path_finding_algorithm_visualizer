import sys
import pygame as pg
from typing import Callable
from input_handler import InputHandler
from settings import RES, FPS
from grid import Grid


class Game:
    def __init__(self):
        self.screen: pg.Surface = pg.display.set_mode(RES)
        self.clock: pg.time.Clock = pg.time.Clock()
        self.input_handler: InputHandler = InputHandler(self)
        pg.display.set_caption("Pathfinding visualizer")
        self.grid: Grid = Grid(self)

    def draw(self) -> None:
        self.grid.draw()
        pg.display.flip()

    def update(self) -> None:
        self.grid.update()

    def main_loop(self) -> None:
        while True:
            self.input_handler.check_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    @staticmethod
    def quit_game() -> None:
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.main_loop()
