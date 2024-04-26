from typing import Callable
from pygame import draw


class Button:
    def __init__(
            self,
            dashboard,
            rect: tuple[int, int, int, int],
            color: tuple[int, int, int],
            func: Callable) -> None:
        """
        :param dashboard: the parent Dashboard object
        :param rect: the position and dimensions of the button
        :param color: the color of the button
        :param func: the function to call when the button is tapped
        """

        self.dashboard = dashboard
        self.rect = rect
        self.pos = self.x, self.y = rect[:2]
        self.res = self.width, self.height = rect[2:]
        self.color: tuple[int, int, int] = color
        self.func: Callable = func

    def draw(self) -> None:
        draw.rect(self.dashboard.surface, self.color, self.rect)

        if self.dashboard.selected_button == self:
            border_color: tuple[int, int, int] = (0, 0, 0)
            border_width: int = 2
            draw.rect(self.dashboard.surface, border_color, self.rect, border_width)

    def update(self) -> None:
        pass

    def on_tapped(self) -> None:
        self.func()
