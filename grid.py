from tile import Tile
from settings import NUM_ROWS, NUM_COLUMNS, RES
from pygame import Surface


class Grid:
    def __init__(self, game) -> None:
        self.game = game
        self.tiles = {(col, row): Tile(col=col, row=row, grid=self) for col in range(NUM_COLUMNS) for row in range(NUM_ROWS)}
        self.surface = Surface(RES)

    def update(self) -> None:
        self.check_tiles_state()

    def draw(self) -> None:
        self.game.screen.blit(self.surface, (0, 0))

    def check_tiles_state(self) -> None:
        for tile in self.tiles.values():
            if tile.state != tile.prev_state:
                tile.draw()
                tile.update_prev_state()

