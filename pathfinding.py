from time import sleep, time
from pygame import display
from tile import Tile
from typing import Callable, Any


class PathFinder:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.algorithms: list[Callable] = [self.dijkstra, self.a_star]
        self.selected_algorithm: Callable = self.algorithms[0]

    def path_finding_algorithm(self, function: Callable) -> Callable:
        def wrapper() -> None:
            self.clear_visited_tiles()
            start_time: float = time()
            function()
            end_time: float = time()
            duration: float = end_time - start_time
            print(f'{function.__name__} took {duration:.2f} seconds')

        return wrapper

    @path_finding_algorithm
    def dijkstra(self) -> None:
        pass

    @path_finding_algorithm
    def a_star(self) -> None:
        pass

    def clear_visited_tiles(self) -> None:
        for tile in self.grid.tiles.values():
            if tile.state == 'visited':
                tile.change_state('empty')

    def visit_tile(self, tile: Tile) -> None:
        tile.change_state('visited')
        self.grid.update()
        self.grid.draw()
        display.flip()
        sleep(0.1)
