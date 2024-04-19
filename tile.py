from settings import STATE_COLORS, TILE_SIZE
from grid import Grid
from pygame import draw


class Tile:
    def __init__(self, col: int, row: int, grid: Grid) -> None:
        self.grid: Grid = grid
        self.col: int = col
        self.row: int = row
        self.state: str = 'empty'
        self.prev_state: str = 'unassigned'

    @property
    def color(self) -> tuple[int, int, int]:
        return STATE_COLORS[self.state]

    def update(self) -> None:
        pass

    def draw(self) -> None:
        rectangle: tuple[int, int, int, int] = (self.col * TILE_SIZE[0], self.row * TILE_SIZE[1], TILE_SIZE[0], TILE_SIZE[1])
        draw.rect(self.grid.surface, self.color, rectangle)

    def change_state(self, state: str) -> None:
        self.state = state

    def on_tapped(self) -> None:
        pass