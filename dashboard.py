from pygame import Surface
from settings import DASHBOARD_RES, GRID_HEIGHT, STATE_COLORS
from button import Button


class Dashboard:
    def __init__(self, game) -> None:
        self.game = game
        self.surface: Surface = Surface(DASHBOARD_RES)
        self.buttons: list[Button] = [
            Button(self, (10, 10, 25, 25), STATE_COLORS['start'], lambda: setattr(self, 'state', 'start')),
            Button(self, (100, 10, 25, 25), STATE_COLORS['border'], lambda: setattr(self, 'state', 'border')),
            Button(self, (200, 10, 25, 25), STATE_COLORS['end'], lambda: setattr(self, 'state', 'end')),
            Button(self, (300, 10, 25, 25), STATE_COLORS['empty'], lambda: setattr(self, 'state', 'empty')),
            Button(self, (400, 10, 75, 25), STATE_COLORS['visited'], lambda: self.game.grid.path_finder.selected_algorithm(self.game.grid.path_finder)),
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
