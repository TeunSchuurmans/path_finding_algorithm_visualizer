from typing import Callable
import pygame as pg
from settings import GRID_WIDTH, GRID_HEIGHT, TILE_SIZE


class InputHandler:
    def __init__(self, game) -> None:
        self.game = game
        self.event_handlers: dict[int, Callable] = {
            pg.QUIT: self.game.quit_game,
            pg.MOUSEBUTTONDOWN: self.mouse_button_down,
        }

    def check_events(self) -> None:
        """
        Check for events and call the appropriate event handler.
        """
        for event in pg.event.get():
            if event.type in self.event_handlers:
                self.event_handlers[event.type]()

    def mouse_button_down(self) -> None:
        """
        Handle the MOUSEBUTTONDOWN event.
        """
        button_down_position: tuple[int, int] = pg.mouse.get_pos()
        grid_surface: tuple[float, float, float, float] = (0, 0, GRID_WIDTH, GRID_HEIGHT)
        if self.is_on_surface(button_down_position, grid_surface):
            index: tuple[int, int] = InputHandler.pos_to_index(button_down_position)
            if index in self.game.grid.tiles:
                self.game.grid.tiles[index].on_tapped('start')

    @staticmethod
    def is_on_surface(coords: tuple[float, float], surface: tuple[float, float, float, float]) -> bool:
        """
        Check if the given coordinates are within the given surface.
        :param coords: the coordinates to check
        :param surface: the surface to check against
        :return: True if the coordinates are within the surface, False otherwise
        """
        x, y = coords
        surface_x, surface_y, surface_width, surface_height = surface
        return surface_x <= x <= surface_x + surface_width and surface_y <= y <= surface_y + surface_height

    @staticmethod
    def pos_to_index(coords: tuple[float, float]) -> tuple[int, int]:
        """
        Convert the given coordinates to the corresponding grid indices.
        coords should be relative to the grid.
        :param coords: the coordinates to convert
        :return: the corresponding grid indices
        """
        x, y = coords
        return int(x / TILE_SIZE), int(y / TILE_SIZE)
