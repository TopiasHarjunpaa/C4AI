import pygame


class ClockService:
    """A class to represent clock service which tracks time.

    Attributes:
        fps: Framerate
    """

    def __init__(self, fps):
        """Constructs framerate attribute for the clock object.

        Args:
            fps (int): Framerate
        """

        self._clock = pygame.time.Clock()
        self._fps = fps

    def tick(self):
        """Updates the clock.
        Runtime is limited up to framerate.
        """

        self._clock.tick(self._fps)

    def get_ticks(self):
        """Gets the time in milliseconds.

        Returns:
            milliseconds (int): Returns the number of milliseconds since the pygame inited.
        """

        return pygame.time.get_ticks()
