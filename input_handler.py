from typing import Callable
from pygame import event as events


class InputHandler:
    def __init__(self, event_handlers: dict[int, Callable[[], None]]) -> None:
        self.event_handlers = event_handlers

    def check_events(self) -> None:
        """
        Check for events and call the appropriate event handler.
        """

        for event in events.get():
            if event.type in self.event_handlers:
                self.event_handlers[event.type]()
