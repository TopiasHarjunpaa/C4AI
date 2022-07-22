import pygame


class EventQueueService:
    """A class to represent event and queue services.
    """

    def get(self):
        """Gets events from the queue.

        Returns:
            Eventlist (list): Returns all the messages and removes them from the queue.
        """
        return pygame.event.get()
