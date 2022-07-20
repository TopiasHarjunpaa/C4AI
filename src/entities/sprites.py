import pygame
from entities.player import Player


class Sprites:
    """A class to represent sprites object. This object initialises all sprites.
    Attributes:
        level: Level object
        width: Width of the display.
        heigth: Heigth of the display.
    """

    def __init__(self, board, width, height):
        """Constructs all the necessary attributes for the sprites object and inits all sprites.
        Args:
            board (Board): Board object
            width (int): Width of the display.
            heigth (int): Heigth of the display.
        """

        self._board = board
        self._size = (width, height)
        self.all_sprites = pygame.sprite.Group()

        # Just testing
        self.player1 = Player(self._board, self._size[0]/2,
                             self._size[1] / 4 * 3, self._size[0] / 40, (255,0,0))
        self.player2 = Player(self._board, self._size[0]/2,
                      self._size[1] / 4 * 2, self._size[0] / 40, (255,255,0))

        self._init_sprites()

    def _init_sprites(self):
        """Initialises all sprites
        """

        self.all_sprites.add(self.player1, self.player2)

    def _draw_new_token():
        pass