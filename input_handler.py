from typing import Callable
from pygame import event as events


class InputHandler:
    def __init__(self, event_handlers: dict[[tuple[int, int]], Callable[[], None]]) -> None:
        self.event_handlers = event_handlers

    def check_events(self) -> None:
        """
        Check for events and call the appropriate event handler.
        """

