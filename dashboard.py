from pygame import Surface
from settings import DASHBOARD_RES, GRID_HEIGHT
from button import Button


class Dashboard:
    def __init__(self, game) -> None:
        self.game = game
        self.surface: Surface = Surface(DASHBOARD_RES)
        self.buttons: list[Button] = [
            Button(self, (10, 10, 25, 25), (0, 255, 0), lambda: setattr(self, 'state', 'start')),
            Button(self, (100, 10, 25, 25), (50, 50, 50), lambda: setattr(self, 'state', 'border')),
            Button(self, (200, 10, 25, 25), (255, 0, 0), lambda: setattr(self, 'state', 'end')),
            Button(self, (300, 10, 25, 25), (200, 200, 200), lambda: setattr(self, 'state', 'empty')),
        ]
        self.selected_button: Button = None
        self.state = 'empty'

    def draw(self) -> None:
        self.surface.fill((128, 128, 128))
        for button in self.buttons:
            button.draw()
        self.game.screen.blit(self.surface, (0, GRID_HEIGHT))

    def update(self) -> None:
        pass
