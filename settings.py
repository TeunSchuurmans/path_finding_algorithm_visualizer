# screen settings
WIDTH: float = 1600
HEIGHT: float = 900
RES: tuple[float, float] = WIDTH, HEIGHT
FPS: float = 144

# grid settings
GRID_WIDTH: float = WIDTH
GRID_HEIGHT: float = HEIGHT
NUM_ROWS: int = 14
NUM_COLUMNS: int = 9

# tile settings
TILE_SIZE: tuple[int, int] = (100, 100)

# color settings
STATE_COLORS: dict[str, tuple[int, int, int]] = {
    'empty': (255, 255, 255)
}

