from math import ceil

# screen settings
WIDTH: float = 1000
HEIGHT: float = 600
RES: tuple[float, float] = WIDTH, HEIGHT
FPS: float = 144

# grid and tile settings
GRID_HEIGHT = HEIGHT * 0.85
GRID_WIDTH = WIDTH
NUM_ROWS = 40
TILE_SIZE: int = int(GRID_HEIGHT / NUM_ROWS)
NUM_COLUMNS: int = ceil(GRID_WIDTH / TILE_SIZE)


# color settings
STATE_COLORS: dict[str, tuple[int, int, int]] = {
    'empty': (255, 255, 255)
}

