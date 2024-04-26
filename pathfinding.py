from time import sleep
from pygame import display
from tile import Tile
from typing import Callable


class PathFinder:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.algorithms: list[Callable] = [self.dijkstra, self.a_star]
        self.selected_algorithm: Callable = self.algorithms[0]

    def dijkstra(self) -> None:
        # only runs the algorithm if the start and end tiles are set
        if self.grid.start and self.grid.end != (-1, -1):
            for tile in self.grid.tiles:
                if tile.state == 'start' or 'visited':
                    neighbours: list[Tile] = []
                    for neighbour in neighbours:
                        if neighbour.state == 'empty':
                            self.visit_tile(neighbour)

    def a_star(self) -> None:
        pass

    def visit_tile(self, tile: Tile) -> None:
        tile.change_state('visited')
        self.grid.update()
        self.grid.draw()
        display.flip()
        sleep(0.1)