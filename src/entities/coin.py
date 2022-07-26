import pygame
from config import WHITE


class Coin(pygame.sprite.Sprite):
    """A class to represent coin object at the game board.

    Attributes:
        board: Board object
        x_coordinate: Spawn location at the x-axis.
        y_coordinate: Spawn location at the y-axis.
        size: side length of the round coin object.
    """

    def __init__(self, x_coordinate, y_coordinate, size, color):
        """Constructs all the necessary attributes for the coin object.

        Args:
            x_coordinate (int): Spawn location at the x-axis.
            y_coordinate (int): Spawn location at the y-axis.
            size (int): side length of the round coin object.
            color: color of the token.
        """

        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.color = color
        self._visualize(size)
        self.rect = self.image.get_rect()
        self.rect.center = (x_coordinate, y_coordinate)

    def _visualize(self, size):
        """Creates visualization for the coin object.
        Coin object is colored circle with white borders and
        radius 0.45 times of side length of cell size.

        Args:
            size (int): side length of the round token object.
        """

        pygame.draw.circle(self.image, WHITE,
                           (size*0.5, size*0.5), size*0.45)
        pygame.draw.circle(self.image, (self.color),
                           (size*0.5, size*0.5), size*0.43)
