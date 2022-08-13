import pygame
from config import COIN1_PATH, COIN2_PATH


class Coin(pygame.sprite.Sprite):
    """A class to represent coin object at the game board.

    Attributes:
        board: Board object
        x_coordinate: Spawn location at the x-axis.
        y_coordinate: Spawn location at the y-axis.
        size: side length of the round coin object.
    """

    def __init__(self, x_coordinate, y_coordinate, size, player_number):
        """Constructs all the necessary attributes for the coin object.

        Args:
            x_coordinate (int): Spawn location at the x-axis.
            y_coordinate (int): Spawn location at the y-axis.
            size (int): side length of the round coin object.
            color: color of the token.
        """

        super().__init__()

        self.image = pygame.image.load(COIN1_PATH)
        self.image = pygame.transform.scale(self.image, (size, size))
        if player_number == 2:
            self.image = pygame.image.load(COIN2_PATH)
            self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (x_coordinate, y_coordinate)
