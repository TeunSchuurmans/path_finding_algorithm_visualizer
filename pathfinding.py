from time import sleep, time
from pygame import display
from tile import Tile
from typing import Callable
from settings import NUM_ROWS, NUM_COLUMNS


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

    def get_neighbors(self, tile_index: tuple[int, int]) -> dict[tuple[int, int], Tile]:
        """
        Get the neighbors of the given tile.
        :param tile_index:
        :return:
        """
        neighbors: dict[tuple[int, int], Tile] = {}
        col, row = tile_index

        if col - 1 >= 0:
            neighbors[(col - 1, row)] = self.grid.tiles[(col - 1, row)]
        if col + 1 < NUM_COLUMNS:
            neighbors[(col + 1, row)] = self.grid.tiles[(col + 1, row)]
        if row - 1 >= 0:
            neighbors[(col, row - 1)] = self.grid.tiles[(col, row - 1)]
        if row + 1 < NUM_ROWS:
            neighbors[(col, row + 1)] = self.grid.tiles[(col, row + 1)]

        return neighbors

    def clear_visited_tiles(self) -> None:
        """
        Clear all the visited tiles.
        :return:
        """
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


@PathFinder.path_finding_algorithm
def dijkstra(pathfinder: PathFinder) -> None:
    """
    Dijkstra's algorithm to find the shortest path between two points.
    :param pathfinder:
    :return:
    """
    found: bool = False
    possible: bool = True

    visited_tiles: dict[tuple[int, int], Tile] = {pathfinder.grid.start: pathfinder.grid.tiles[pathfinder.grid.start]}

    if pathfinder.grid.start == (-1, -1):
        print('Start not set')
        return None
    if pathfinder.grid.end == (-1, -1):
        print('End not set')
        return None

    while not found and possible:
        print(len(visited_tiles))
        if len(visited_tiles) == 0:
            possible = False
            print('No path found')
        for index in list(visited_tiles.keys()):

            neighbors: dict[tuple[int, int], Tile] = pathfinder.get_neighbors(index)

            visitable_neighbors = {neighbor_index: neighbor for neighbor_index, neighbor in neighbors.items() if neighbor.state != 'visited' and neighbor.state != 'border'}

            if len(visitable_neighbors) == 0:
                del visited_tiles[index]
            else:
                for neighbor_index, visitable_neighbor in visitable_neighbors.items():
                    if visitable_neighbor.state == 'end':
                        found = True
                        break
                    elif visitable_neighbor.state == 'empty':
                        pathfinder.visit_tile(visitable_neighbor)
                        visited_tiles[neighbor_index] = visitable_neighbor
                        sleep(0.05)


@PathFinder.path_finding_algorithm
def a_star(pathfinder: PathFinder) -> None:
    """
    A* algorithm to find the shortest path between two points.
    :param pathfinder:
    :return:
    """
    found: bool = False
    possible: bool = True

    while not found and possible:
        pass
