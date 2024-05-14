from pygame import Surface
from settings import DASHBOARD_RES, GRID_HEIGHT, STATE_COLORS
from button import Button
from label import Label


class Dashboard:
    def __init__(self, game) -> None:
        self.game = game
        self.surface: Surface = Surface(DASHBOARD_RES)
        self.buttons: list[Button] = [
            Button((10, 10, 25, 25), STATE_COLORS['start'], lambda: setattr(self, 'state', 'start')),
            Button((100, 10, 25, 25), STATE_COLORS['border'], lambda: setattr(self, 'state', 'border')),
            Button((200, 10, 25, 25), STATE_COLORS['end'], lambda: setattr(self, 'state', 'end')),
            Button((300, 10, 25, 25), STATE_COLORS['empty'], lambda: setattr(self, 'state', 'empty')),
            Button((400, 10, 75, 25), STATE_COLORS['visited'], lambda: self.game.grid.path_finder.selected_algorithm(self.game.grid.path_finder)),
        ]
        self.labels: list[Label] = []
        self.child_surfaces: list[any] = [*self.buttons, *self.labels]
        self.selected_button: Button | None = None
        self.state = 'empty'

    def draw(self) -> None:
        self.surface.fill((128, 128, 128))
        self.draw_child_surfaces()
        self.game.screen.blit(self.surface, (0, GRID_HEIGHT))

    def draw_child_surfaces(self) -> None:
        for child_surface in self.child_surfaces:
            self.surface.blit(child_surface.surface, child_surface.rect.topleft)
