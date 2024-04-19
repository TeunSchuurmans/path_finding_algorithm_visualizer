# screen settings
WIDTH: float = 1600
HEIGHT: float = 900
RES: tuple[float, float] = WIDTH, HEIGHT
FPS: float = 144

# grid settings
NUM_ROWS: int = 40
NUM_COLUMNS: int = 40

# tile settings
TILE_SIZE: tuple[int, int] = 20, 20

# color settings
STATE_COLORS: dict[str, tuple[int, int, int]] = {
    'empty': (255, 255, 255)
}

