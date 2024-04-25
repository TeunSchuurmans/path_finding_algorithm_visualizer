from pygame import Surface
from settings import DASHBOARD_RES, GRID_HEIGHT


class Dashboard:
    def __init__(self, game) -> None:
        self.game = game
        self.surface: Surface = Surface(DASHBOARD_RES)

    def draw(self) -> None:
        self.surface.fill((255, 0, 0))
        self.game.screen.blit(self.surface, (0, GRID_HEIGHT))

    def update(self) -> None:
        pass
