import pygame
from config import BOARD0_PATH


class Grid(pygame.sprite.Sprite):
    """A class to visualize game board cell. Game board has total of 6 x 7 cells.

    Attributes:
        width: Width of the display.
        heigth: Heigth of the display.
        size: side length of the game cell.
    """

    def __init__(self, width, height, size):
        """Constructs all the necessary attributes for the grid object.

        Args:
            board (Board): Board object.
            width (int): Width of the display.
            size (int): side length of the game cell.
        """

        super().__init__()
        self.image = pygame.image.load(BOARD0_PATH)
        self.image = pygame.transform.scale(self.image, (8*size, 7*size))
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2 + 0.9 * size)
