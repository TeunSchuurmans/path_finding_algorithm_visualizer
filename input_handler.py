from typing import Callable
import pygame as pg
from settings import GRID_WIDTH, GRID_HEIGHT, TILE_SIZE, DASHBOARD_HEIGHT, DASHBOARD_WIDTH


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
        dashboard_surface: tuple[float, float, float, float] = (0, GRID_HEIGHT, DASHBOARD_WIDTH, DASHBOARD_HEIGHT)

        # Grid tile handling
        if self.is_on_surface(button_down_position, grid_surface):
            index: tuple[int, int] = InputHandler.pos_to_index(button_down_position)
            if index in self.game.grid.tiles:
                self.game.grid.tiles[index].on_tapped(self.game.dashboard.state)

        # Dashboard button handling
        elif self.is_on_surface(button_down_position, dashboard_surface):
            relative_position: tuple[float, float] = (button_down_position[0] - dashboard_surface[0], button_down_position[1] - dashboard_surface[1])
            for button in self.game.dashboard.buttons:
                if self.is_on_surface(relative_position, button.rect):
                    self.game.dashboard.selected_button = button
                    button.on_tapped()

    @staticmethod
    def is_on_surface(coords: tuple[float, float], surface: tuple[float, float, float, float]) -> bool:
        """
        Check if the given coordinates are within the given _surface.
        :param coords: the coordinates to check
        :param surface: the _surface to check against
        :return: True if the coordinates are within the _surface, False otherwise
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
