import pygame
from entities.coin import Coin
from entities.grid import Grid


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
        self._cell_size = width / 20
        self._start_x = width / 2 - 3 * self._cell_size
        self._start_y = height / 2 - 2.5 * self._cell_size
        self.all_sprites = pygame.sprite.Group()
        self.grids = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self._init_sprites()

    def _init_sprites(self):
        """Initialises all sprites
        """


        for i in range(6):
            for j in range(7):
                grid = Grid(self._start_x + j * self._cell_size,
                            self._start_y + i * self._cell_size,
                            self._cell_size)
                self.grids.add(grid)
        self.grids.add(grid)
        self.all_sprites.add(self.grids)

    def draw_new_token(self, row_number, col_number, player_number):
        YELLOW = (255,204,0)
        RED = (255,0,0)
        color = RED
        if player_number == 2:
            color = YELLOW
        coin = Coin(self._board, self._start_x + col_number * self._cell_size,
                    self._start_y + row_number * self._cell_size,
                    self._cell_size, color)
        self.coins.add(coin)
        self.all_sprites.add(coin)