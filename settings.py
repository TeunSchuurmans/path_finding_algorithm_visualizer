from math import ceil, floor

# screen settings
WIDTH: float = 1000
HEIGHT: float = 600
RES: tuple[float, float] = WIDTH, HEIGHT
FPS: float = 144

# grid and tile settings
GRID_HEIGHT: float = HEIGHT * 0.85
GRID_WIDTH: float = WIDTH
GRID_RES: tuple[float, float] = GRID_WIDTH, GRID_HEIGHT
NUM_ROWS: int = 30
TILE_SIZE: int = floor(GRID_HEIGHT / NUM_ROWS)
NUM_COLUMNS: int = ceil(GRID_WIDTH / TILE_SIZE)

# dashboard settings
DASHBOARD_HEIGHT: float = HEIGHT - GRID_HEIGHT
DASHBOARD_WIDTH: float = WIDTH
DASHBOARD_RES: tuple[float, float] = DASHBOARD_WIDTH, DASHBOARD_HEIGHT

# color settings
STATE_COLORS: dict[str, tuple[int, int, int]] = {
    'empty': (255, 255, 255),
    'start': (0, 255, 0),
    'end': (255, 0, 0),
    'border': (0, 0, 0),
    'visited': (0, 0, 255),
}
