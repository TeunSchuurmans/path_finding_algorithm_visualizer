from math import ceil, floor

# screen settings
WIDTH: float = 1000
HEIGHT: float = 600
RES: tuple[float, float] = WIDTH, HEIGHT
FPS: float = 144

# grid and tile settings
GRID_HEIGHT: float = HEIGHT * 0.85
GRID_WIDTH: float = WIDTH
NUM_ROWS: int = 30

TILE_SIZE: int = floor(GRID_HEIGHT / NUM_ROWS)
NUM_COLUMNS: int = ceil(GRID_WIDTH / TILE_SIZE)


# color settings
STATE_COLORS: dict[str, tuple[int, int, int]] = {
    'empty': (255, 255, 255),
    'start': (0, 255, 0),
    'end': (255, 0, 0),
    'border': (0, 0, 0),
}
