from time import sleep, time
from pygame import display
from tile import Tile
from typing import Callable


class PathFinder:
    def __init__(self, grid, algorithms: list[Callable]) -> None:
        self.grid = grid
        self.algorithms: list[Callable] = algorithms
        self.selected_algorithm: Callable = self.algorithms[0]

    @staticmethod
    def path_finding_algorithm(function: Callable) -> Callable:
        """
        Decorator to add functionality to all the pathfinding algorithms and measure the time taken to execute them
        :param function:
        :return:
        """

        def wrapper(self) -> None:
            self.clear_visited_tiles()
            start_time: float = time()
            function(self)
            end_time: float = time()
            duration: float = end_time - start_time
            print(f'{function.__name__} took {duration:.2f} seconds')

        return wrapper

    def clear_visited_tiles(self) -> None:
        for tile in self.grid.tiles.values():
            if tile.state == 'visited':
                tile.change_state('empty')

    def visit_tile(self, tile: Tile) -> None:
        """
        Change the state of the tile to visited and update the grid so that the change is reflected on the screen.
        :param tile:
        :return:
        """
        tile.change_state('visited')
        self.grid.update()
        self.grid.draw()
        display.flip()
        sleep(0.1)


@PathFinder.path_finding_algorithm
def dijkstra(pathfinder: PathFinder) -> None:
    pass


@PathFinder.path_finding_algorithm
def a_star(pathfinder: PathFinder) -> None:
    pass
