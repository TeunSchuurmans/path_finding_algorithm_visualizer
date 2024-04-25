from settings import STATE_COLORS, TILE_SIZE
from pygame import draw


class Tile:
    def __init__(self, pos: tuple, grid) -> None:
        """
        :param grid: the parent Grid object
        """
        self.pos = self.x, self.y = pos
        self.grid = grid
        self.state: str = 'empty'
        self.prev_state: str = 'unassigned'

    @property
    def color(self) -> tuple[int, int, int]:
        return STATE_COLORS[self.state]

    def update(self) -> None:
        self.draw()

    def draw(self) -> None:
        tile_rect: tuple[int, int, int, int] = (self.x, self.y, TILE_SIZE, TILE_SIZE)
        draw.rect(self.grid.surface, self.color, tile_rect)
        border_color: tuple[int, int, int] = (0, 0, 0)
        border_width: int = 1
        draw.rect(self.grid.surface, border_color, tile_rect, border_width)

    def change_state(self, state: str) -> None:
        self.state = state

    def update_prev_state(self) -> None:
        self.prev_state = self.state

    def on_tapped(self, state: str) -> None:
        self.change_state(state)
        if state == 'start':
            if self.grid.start != (-1, -1):
                self.grid.tiles[self.grid.start].state = 'empty'
            self.grid.start = (self.x // TILE_SIZE, self.y // TILE_SIZE)
        elif state == 'end':
            if self.grid.end != (-1, -1):
                self.grid.tiles[self.grid.end].state = 'empty'
            self.grid.end = (self.x // TILE_SIZE, self.y // TILE_SIZE)
