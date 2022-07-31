from config import ROWS, COLUMNS


class SituationService:
    """A class to represent services for checking
    different game scenarios
    """

    def __init__(self, board):
        self._board = board

    def get_game_grid(self):
        return self._board.grid

    # Update docstring
    def check_column_available(self, grid, col_number):
        """Checks if certain column is available to put next game coin.

        Args:

            col_number (int): Index of column in game grid matrix

        Returns:
            int: Index of first available row ie. where coin will be dropped in.
        """

        for row_number in reversed(range(ROWS)):
            if grid[row_number][col_number] == 0:
                return row_number
        return -1

    # Rename and update docstring
    def get_available_columns(self, grid):
        """Gets all available columns to put next game coin.

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
        if len(self.get_available_columns(grid)) == 0:
            return True
        return False

    # Update docstring
    def check_win(self, grid, player_number):
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