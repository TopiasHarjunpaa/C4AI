import pygame


class Player(pygame.sprite.Sprite):
    """A class to represent player object at the game board.
    Attributes:
        board: Board object
        x_coordinate: Spawn location at the x-axis.
        y_coordinate: Spawn location at the y-axis.
        size: side length of the rectangular player object.
    """

    def __init__(self, board, x_coordinate, y_coordinate, size, color):
        """Constructs all the necessary attributes for the player object.
        Args:
            board (Board): Board object
            x_coordinate (int): Spawn location at the x-axis.
            y_coordinate (int): Spawn location at the y-axis.
            size (int): side length of the rectangular player object.
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
        self.rect.midbottom = (x_coordinate, y_coordinate) # change to center

    def drop(self):
        """Placeholder
        """
        pass


    def update(self):
        """Updates location of the player object.
        """
        pass

    def _visualize(self, size):
        """Creates visualization for the player object.
        Player object white borders.
        Args:
            size (int): side length of the rectangular player object.
        """
        # change shape
        pygame.draw.rect(self.image, (255,255,255), (0, 0, size, size))
        pygame.draw.rect(self.image, (self.color),(3, 3, size - 6, size - 6))