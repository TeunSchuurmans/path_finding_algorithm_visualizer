from pygame import font, Surface, Rect
from pygame.rect import RectType


class Label:
    def __init__(self, text: str, color: tuple[int, int, int], pos: tuple[float, float]) -> None:
        """
        A label that displays text.
        :param text:
        :param color:
        :param pos:
        """
        self.text: str = text
        self.color: tuple[int, int, int] = color
        self.pos = self.x, self.y = pos
        self.font = font.SysFont('Arial', 24)

    @property
    def text_surface(self) -> Surface:
        """
        Get the text surface.
        :return:
        """
        return self.font.render(self.text, True, self.color)

    @property
    def text_rect(self) -> Rect | RectType:
        """
        Get the rectangle of the text surface.
        :return:
        """
        return self.text_surface.get_rect(center=(self.x, self.y))

    def update_text(self, text: str) -> None:
        """
        Update the text.
        :param text:
        :return:
        """
        self.text = text