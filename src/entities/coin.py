import pygame


class Coin(pygame.sprite.Sprite):
    """A class to represent coin object at the game board.
    Attributes:
        board: Board object
        x_coordinate: Spawn location at the x-axis.
        y_coordinate: Spawn location at the y-axis.
        size: side length of the round coin object.
    """

    def __init__(self, board, x_coordinate, y_coordinate, size, color):
        """Constructs all the necessary attributes for the coin object.
        Args:
            board (Board): Board object
            x_coordinate (int): Spawn location at the x-axis.
            y_coordinate (int): Spawn location at the y-axis.
            size (int): side length of the round coin object.
            color: color of the token.
        """

        super().__init__()
        self._board = board
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.color = color
        self._visualize(size)
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2(x_coordinate, y_coordinate)
        self.speed = 0 # placeholder for animation
        self.rect.center = (x_coordinate, y_coordinate)

    def drop(self):
        """Placeholder
        """
        pass


    def update(self):
        """Updates location of the coin object.
        """
        pass

    def _visualize(self, size):
        """Creates visualization for the coin object.
        Coin object white borders.
        Args:
            size (int): side length of the round token object.
        """

        pygame.draw.circle(self.image, (255,255,255), (size*0.5, size*0.5), size*0.45)
        pygame.draw.circle(self.image, (self.color),(size*0.5, size*0.5), size*0.43)