from config import ROWS, COLUMNS


class SituationService:
    """A class to represent services for checking different
    game scenarios such as checking terminal situations and
    finding available columns on a game grid.
    """

    def __init__(self, board):
        self._board = board

    def get_game_grid(self):
        return self._board.grid

    def check_column_available(self, grid, col_number):
        """Check if certain column has room to put game coin.
        Uses the chosen column number and loops through
        row indexes in reversed order in order to find
        down-most row which value is 0 (empty).

        Args:
            grid (list): Grid matrix of the game board.
            col_number (int): Column index of the game board.

        Returns:
            int: Returns row index if free row has been found. Otherwise returns -1.
        """


        for row_number in reversed(range(ROWS)):
            if grid[row_number][col_number] == 0:
                return row_number
        return -1

    def get_available_locations(self, grid):
        """Gets all available locations where game coin can be placed.
        Loops through all game grid columns using the check_column_available method.
        Adds location (row, col indexes) to the list if the column is not full.

        Returns:
            list: List of tuples (row index, column index) where coins can be dropped in.
        """

        available_columns = []
        for column in range(COLUMNS):
            row = self.check_column_available(grid, column)
            if row != -1:
                available_columns.append((row, column))
        return available_columns

    def check_draw(self, grid):
        """Checks if the game has ended draw.
        Game is draw if game grid is full of coins ie. no
        available columns has been found from the game grid.

        Args:
            grid (list): Grid matrix of the game board.

        Returns:
            Boolean: Returns true if game is draw, otherwise returns false.
        """

        if len(self.get_available_locations(grid)) == 0:
            return True
        return False

    def check_win(self, grid, player_number):
        """Checks if the player has won the game ie. gets four connect:
        1. checks for connect in vertical direction
        2. checks for connect in horizontal direction
        3. checks for connect in increasing diagonal direction
        4. checks for connect in decreasing diagonal direction

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            boolean: Returns true if player has got four connect, else returns false
        """

        for col in range(COLUMNS):
            col = [row[col] for row in grid]
            for row in range(ROWS - 3):
                loc = col[row:row + 4]
                if loc.count(player_number) == 4:
                    return True

        for row in range(ROWS):
            row = grid[row]
            for col in range(COLUMNS - 3):
                loc = row[col:col + 4]
                if loc.count(player_number) == 4:
                    return True

        for row in range(3, ROWS):
            for col in range(COLUMNS - 3):
                loc = [grid[row-i][col+i] for i in range(4)]
                if loc.count(player_number) == 4:
                    return True

        for row in range(ROWS - 3):
            for col in range(COLUMNS - 3):
                loc = [grid[row+i][col+i] for i in range(4)]
                if loc.count(player_number) == 4:
                    return True

        return False
