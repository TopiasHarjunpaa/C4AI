import math
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

    def copy_grid(self, grid):
        """Creates copy of the grid using list comprehension.

        Args:
            grid (list): Grid matrix of the game board.

        Returns:
            list: Returns copied list from the grid
        """

        return [[grid[row][col] for col in range(COLUMNS)] for row in range(ROWS)]

    def check_available_location(self, grid, col_number):
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

        Args:
            grid (list): Grid matrix of the game board.

        Returns:
            list: List of tuples (row index, column index) where coins can be dropped in.
        """

        available_columns = []
        for column in range(COLUMNS):
            row = self.check_available_location(grid, column)
            if row != -1:
                available_columns.append((row, column))
        return available_columns

    def get_available_locations_ranked(self, grid):
        """Similar than get_available_locations -method but also ranks the result
        starting from closest to the middle column and ending to closest to the side
        columns.

        Args:
            grid (list): Grid matrix of the game board.

        Returns:
            list: List of tuples (row index, column index) where coins can be dropped in.
        """

        available_columns = []
        column_order = [3, 2, 4, 1, 5, 0, 6]
        for column in column_order:
            row = self.check_available_location(grid, column)
            if row != -1:
                available_columns.append((row, column))
        return available_columns

    def count_free_slots(self, grid):
        """Counts the number of free slots ie. number of zeros (empty)
        remaining on the current game grid.

        Args:
            grid (list): Grid matrix of the game board.

        Returns:
            int: Returns number of free slots
        """

        free_slots = 0
        for row in grid:
            free_slots += row.count(0)
        return free_slots

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
                line_of_connect = col[row:row + 4]
                if line_of_connect.count(player_number) == 4:
                    return True

        for row in range(ROWS):
            row = grid[row]
            for col in range(COLUMNS - 3):
                line_of_connect = row[col:col + 4]
                if line_of_connect.count(player_number) == 4:
                    return True

        for row in range(3, ROWS):
            for col in range(COLUMNS - 3):
                line_of_connect = [grid[row-i][col+i] for i in range(4)]
                if line_of_connect.count(player_number) == 4:
                    return True

        for row in range(ROWS - 3):
            for col in range(COLUMNS - 3):
                line_of_connect = [grid[row+i][col+i] for i in range(4)]
                if line_of_connect.count(player_number) == 4:
                    return True

        return False

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

    def check_terminal_node(self, grid, player_number):
        """Checks if the game situation means that the game has ended.

        Game ends if one of the player has gotten connect four. In that case
        the method will return value of INF if the winning player is the same
        with player number given for the method. Otherwise the return value will
        be -INF. Game will end as draw if the grid is full and none of the players
        has not won. In this case return value will be 0.

        Game hasn't ended if none of the player has not won and the grid is not
        full. In that case return value will be None.

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            INF, -INF, 0 or None
        """

        if self.check_win(grid, player_number):
            return math.inf

        if self.check_win(grid, player_number % 2 + 1):
            return -math.inf

        if self.check_draw(grid):
            return 0

        return None
