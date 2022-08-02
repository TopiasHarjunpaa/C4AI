import pygame
from entities.coin import Coin
from entities.grid import Grid


class Sprites:
    """A class to represent sprites object. This object initialises all sprites.

    Attributes:
        board: Board object
        width: Width of the display.
        heigth: Heigth of the display.
    """

    def __init__(self, board, width, height):
        """Constructs all the necessary attributes for the sprites object and inits all sprites.
        Start X and Y indicates top-left coordinates of the game board at the screen.
        Cell size means side length of the each squared cell of the game board grid.

        Args:
            board (Board): Board object
            width (int): Width of the display.
            heigth (int): Heigth of the display.
        """

        self._board = board
        self._width = width
        self._height = height
        self._cell_size = width / 22
        self._start_x = width / 2 - 3 * self._cell_size
        self._start_y = height / 2 - 1.6 * self._cell_size
        self.all_sprites = pygame.sprite.Group()
        self.grids = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self._init_game_board()

    def _init_game_board(self):
        """Initialises game board and adds to the sprites group
        """

        grid = Grid(self._width, self._height, self._cell_size)
        self.grids.add(grid)
        self.all_sprites.add(self.grids)

    def draw_new_coin(self, row_number, col_number, player_number):
        """Initialises a game coin. First player has red coin and second player has yellow coin.
        Adds each coin to the sprite group.

        Args:
            row_number (int): Game board row number
            col_number (int): Game board column number
            player_number (int): Player number (1 = first player, 2 = second player)
        """

        coin = Coin(self._start_x + col_number * self._cell_size,
                    self._start_y + row_number * self._cell_size,
                    self._cell_size * 0.97, player_number)
        self.coins.add(coin)
        self.all_sprites.add(coin)
