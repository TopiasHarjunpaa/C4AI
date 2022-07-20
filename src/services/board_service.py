import pygame
from entities.sprites import Sprites

class BoardService:
    """A class to represent game board services.
    Attributes:
        width: Width of the display.
        height: Heigth of the display.
    """

    def __init__(self, width, height):
        """Constructs all the necessary attributes for the board service object.
        Args:
            width (int): Width of the display.
            height (int): Heigth of the display.
        """

        self.sprites = Sprites(self, width, height)
        self.all_sprites = self.sprites.all_sprites

        #Just for testing
        self.player1 = self.sprites.player1
        self.player2 = self.sprites.player2

        self.update()

    def update(self):
        """To be added
        """

        self.all_sprites.update()
        return self._check_win()


    def _add_token(self):
        """To be added
        """
        self.sprites._draw_new_token()

    def _check_win(self):
        """To be added
        """

        return True