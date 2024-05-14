from typing import Callable
from pygame import Surface, Rect


class Button:
    def __init__(
            self,
            rect: tuple[int, int, int, int],
            color: tuple[int, int, int],
            func: Callable) -> None:
        """
        :param rect: the position and dimensions of the button
        :param color: the _color of the button
        :param func: the function to call when the button is tapped
        """

        self._pos = self.x, self.y = rect[:2]
        self._res = self.width, self.height = rect[2:]
        self._rect = Rect(self._pos, self._res)
        self._color: tuple[int, int, int] = color
        self._surface = Surface(self._res)
        self.surface.fill(self._color)
        self._func: Callable = func
        self.is_selected: bool = False

    @property
    def rect(self) -> Rect:
        return self._rect

    @property
    def surface(self) -> Surface:
        surface = Surface(self._res)
        surface.fill(self._color)
        return surface

    def resize(self, width: int, height: int) -> None:
        self.width, self.height = width, height

    def reposition(self, x: int, y: int) -> None:
        self._pos = x, y

    def change_color(self, color: tuple[int, int, int]) -> None:
        self._color = color

    def change_func(self, func: Callable) -> None:
        self._func = func

    def on_tapped(self) -> None:
        self._func()
