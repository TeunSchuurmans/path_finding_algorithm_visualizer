from settings import STATE_COLORS, TILE_SIZE
from pygame import draw


class Tile:
    def __init__(self, col: int, row: int, grid) -> None:
        self.grid = grid
        self.col: int = col
        self.row: int = row
        self.pos: tuple = ()
        self.state: str = 'empty'
        self.prev_state: str = 'unassigned'

    @property
    def color(self) -> tuple[int, int, int]:
        return STATE_COLORS[self.state]

    def update(self) -> None:
        pass

    def draw(self) -> None:
        tile_rect: tuple[int, int, int, int] = (self.col * TILE_SIZE, self.row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        draw.rect(self.grid.surface, self.color, tile_rect)

        # Draw the border
        border_color: tuple[int, int, int] = (0, 0, 0)
        border_width: int = 1
        draw.rect(self.grid.surface, border_color, tile_rect, border_width)

    def change_state(self, state: str) -> None:
        self.state = state

    def update_prev_state(self) -> None:
        self.prev_state = self.state

    def on_tapped(self) -> None:
        pass
