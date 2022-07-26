from entities.sprites import Sprites
from config import ROWS, COLUMNS


class BoardService:
    """A class to represent game board services.

    Attributes:
        width: Width of the display.
        height: Heigth of the display.
    """

    def __init__(self, width, height):
        """Constructs all the necessary attributes for the board service object.
        Game grid has 6 rows and 7 columns and each cell
        will be initialised with the value 0 (empty).

        Args:
            width (int): Width of the display.
            height (int): Heigth of the display.
        """

        self.grid = [[0 for col in range(COLUMNS)] for row in range(ROWS)]
        self._width = width
        self._height = height
        self.sprites = Sprites(self, width, height)
        self.all_sprites = self.sprites.all_sprites
        self.update()

    def reset(self):
        """Resets the object in order to get empty grid
        and sprites
        """

        self.grid = [[0 for col in range(COLUMNS)] for row in range(ROWS)]
        self.sprites = Sprites(self, self._width, self._height)
        self.all_sprites = self.sprites.all_sprites

    def update(self):
        """Updates all sprite objects.
        """

        self.all_sprites.update()

    def add_coin(self, row_number, col_number, player_number):
        """Adds new coin to the game board.
        Creates new coin and updates grid matrix with player number.

        Args:

            col_number (int): Column number of game board to drop coin
            col_number (int): Last free row number of game board at indicated column
            player_number (int): Player number (1 = first player, 2 = second player)
        """

        self.grid[row_number][col_number] = player_number
        self.sprites.draw_new_coin(row_number, col_number, player_number)

    def print_grid(self):
        """Prints current grid matrix
        """
        for row in self.grid:
            print(row)
