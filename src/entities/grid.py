import pygame
from config import BLACK, BLUE


class Grid(pygame.sprite.Sprite):
    """A class to visualize game board cell. Game board has total of 6 x 7 cells.

    Attributes:
        x_coordinate: Spawn location at the x-axis.
        y_coordinate: Spawn location at the y-axis.
        size: side length of the the hollow rectangular grid object.
    """

    def __init__(self, x_coordinate, y_coordinate, size):
        """Constructs all the necessary attributes for the grid object.

        Args:
            x_coordinate (int): Spawn location at the x-axis.
            y_coordinate (int): Spawn location at the y-axis.
            size (int): side length of the hollow rectangular grid object.
        """

        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self._visualize(size)
        self.rect = self.image.get_rect()
        self.rect.center = (x_coordinate, y_coordinate)

    def _visualize(self, size):
        """Creates visualization for the grid object.
        Grid object is blue square and black circle with
        radius 0.45 times of side length of cell size.

        Args:
            size (int): side length of the hollow rectangular grid object.
        """
        pygame.draw.rect(self.image, BLUE, (0, 0, size, size))
        pygame.draw.circle(self.image, BLACK, (size*0.5, size*0.5), size*0.45)
