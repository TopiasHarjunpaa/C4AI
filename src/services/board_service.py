from entities.sprites import Sprites


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

        self.grid = [[0 for row in range(7)] for col in range(6)]
        self._width = width
        self._height = height
        self.sprites = Sprites(self, width, height)
        self.all_sprites = self.sprites.all_sprites
        self.update()

    def reset(self):
        """Resets the object in order to get empty grid
        and sprites
        """

        self.grid = [[0 for row in range(7)] for col in range(6)]
        self.sprites = Sprites(self, self._width, self._height)
        self.all_sprites = self.sprites.all_sprites


    def update(self):
        """Updates all sprite objects.
        """

        self.all_sprites.update()

    def add_coin(self, col_number, player_number):
        """Adds new coin to the game board if there are free slot remaining at the targeted column.
        If free slot is found, creates new coin and updates grid matrix with player number.

        Args:
            col_number (int): Targeted column number of game board to drop coin
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            boolean: Returns true if free slot is found, else returns false.
        """

        for row_number in reversed(range(6)):
            if self.grid[row_number][col_number] == 0:
                self.grid[row_number][col_number] = player_number
                self.sprites.draw_new_coin(
                    row_number, col_number, player_number)
                return True
        return False

    def test_grid(self):
        """Prints current grid matrix
        """
        for row in self.grid:
            print(row)

    def check_win(self, player_number):
        """Checks if the player has won the game ie. gets four connect:
        1. checks for connect in vertical direction
        2. checks for connect in horizontal direction
        3. checks for connect in increasing diagonal direction
        4. checks for connect in decreasing diagonal direction

        Args:
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            boolean: Returns true if player has got four connect, else returns false
        """

        for row in range(3):
            for col in range(6):
                if (self.grid[row][col] == player_number and
                    self.grid[row+1][col] == player_number and
                    self.grid[row+2][col] == player_number and
                        self.grid[row+3][col] == player_number):
                    return True

        for row in range(5):
            for col in range(4):
                if (self.grid[row][col] == player_number and
                    self.grid[row][col+1] == player_number and
                    self.grid[row][col+2] == player_number and
                        self.grid[row][col+3] == player_number):
                    return True

        for row in range(3, 6):
            for col in range(4):
                if (self.grid[row][col] == player_number and
                    self.grid[row-1][col+1] == player_number and
                    self.grid[row-2][col+2] == player_number and
                        self.grid[row-3][col+3] == player_number):
                    return True

        for row in range(3):
            for col in range(4):
                if (self.grid[row][col] == player_number and
                    self.grid[row+1][col+1] == player_number and
                    self.grid[row+2][col+2] == player_number and
                        self.grid[row+3][col+3] == player_number):
                    return True

        return False
