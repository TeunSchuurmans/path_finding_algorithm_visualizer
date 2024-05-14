from tile import Tile
from settings import NUM_ROWS, NUM_COLUMNS, GRID_RES, TILE_SIZE
from pygame import Surface
from pathfinding import PathFinder, dijkstra, a_star


class Grid:
    def __init__(self, game) -> None:
        self.game = game
        self.path_finder = PathFinder(self, [dijkstra, a_star])
        self.tiles: dict[tuple[int, int], Tile] = {}
        self.surface: Surface = Surface(GRID_RES)
        self.start: tuple[int, int] = (-1, -1)
        self.end: tuple[int, int] = (-1, -1)
        self.init_tiles()

    def update(self) -> None:
        self.check_tiles_state()

    def draw(self) -> None:
        self.game.screen.blit(self.surface, (0, 0))

    def init_tiles(self) -> None:
        for col in range(NUM_COLUMNS):
            for row in range(NUM_ROWS):
                pos = (col * TILE_SIZE, row * TILE_SIZE)
                self.tiles[(col, row)] = Tile(pos=pos, grid=self)

    def check_tiles_state(self) -> None:
        for tile in self.tiles.values():
            if tile.state != tile.prev_state:
                tile.update()
                tile.update_prev_state()
