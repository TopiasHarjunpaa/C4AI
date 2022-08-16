import math
from config import ROWS, COLUMNS


class HeuristicService:
    """A class to represent Heuristic calculation services."""

    def __init__(self, bitboard):
        """Constructs all the necessary attributes for the Heuristic service object."""
        self._bb_service = bitboard

    def _count_values(self, loc, player_number):
        """Counts the total score for line of connect. Line of connect is a 4 cells long list
        of cell values (0, 1, 2) which can be in any directions at the game grid
        (horizontal, vertical, both diagonals). If:

        Player has 4 coins at line of connect - player wins ie. big score
        Player has 3 coins and one empty at line of connect - player gets good score
        Player has 2 coins and 2 empty at line of connect - player gets little score

        Args:
            loc (list): Line of connect ie. line which contains 4 grid cell values in any directions
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            int: Returns total value for single line of connect
        """

        value = 0
        opponent_number = player_number % 2 + 1
        multipliers = {0: math.inf, 1: 10, 2: 2}
        for k, val in multipliers.items():
            if loc.count(player_number) == 4 - k and loc.count(0) == k:
                value += val
            if loc.count(opponent_number) == 4 - k and loc.count(0) == k:
                value -= val
        return value

    def _get_positional_values(self, grid, player_number):
        """Calculates positional values from the game situation
        from one of the players perspective. This means method is used
        as a part for the heuristic value calculation. Positional values
        means that the placement of the coin will get better values if placed
        close to the middle column of the game grid. Middle column gives highest
        points and closest side columns gives less points. Other columns will not
        give any additional points.

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            int: Returns total value from the positional points.
        """

        value = 0
        center_col = [row[3] for row in grid]
        side_cols = [row[2] for row in grid] + [row[4] for row in grid]
        value += center_col.count(player_number) * 2
        value += side_cols.count(player_number) * 1
        return value

    def _get_vertical_values(self, grid, player_number):
        """Calculates sum of heuristic values from vertical directions.
        This method loops through the game grid and creates all possible
        four cell long lists in vertical directions. Heuristic values
        will be calculated using _count_values method from each of the lists
        and the values will added to the total value.

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            int: Returns total value from the vertical direction.
        """

        total_value = 0
        for col in range(COLUMNS):
            col = [row[col] for row in grid]
            for row in range(ROWS - 3):
                loc = col[row:row + 4]
                total_value += self._count_values(loc, player_number)
        return total_value

    def _get_horizontal_values(self, grid, player_number):
        """Calculates sum of heuristic values from horizontal directions.
        This method loops through the game grid and creates all possible
        four cell long lists in horizontal directions. Heuristic values
        will be calculated using _count_values method from each of the lists
        and the values will added to the total value.

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            int: Returns total value from the horizontal direction.
        """

        total_value = 0
        for row in range(ROWS):
            row = grid[row]
            for col in range(COLUMNS - 3):
                loc = row[col:col + 4]
                total_value += self._count_values(loc, player_number)
        return total_value

    def _get_inc_diagonal_values(self, grid, player_number):
        """Calculates sum of heuristic values from increasing diagonal directions.
        This method loops through the game grid and creates all possible
        four cell long lists in increasing diagonal directions. Heuristic values
        will be calculated using _count_values method from each of the lists
        and the values will added to the total value.

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            int: Returns total value from the increasing diagonal direction.
        """

        total_value = 0
        for row in range(3, ROWS):
            for col in range(COLUMNS - 3):
                loc = [grid[row-i][col+i] for i in range(4)]
                total_value += self._count_values(loc, player_number)
        return total_value

    def _get_dec_diagonal_values(self, grid, player_number):
        """Calculates sum of heuristic values from decreasing diagonal directions.
        This method loops through the game grid and creates all possible
        four cell long lists in decreasing diagonal directions. Heuristic values
        will be calculated using _count_values method from each of the lists
        and the values will added to the total value.

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            int: Returns total value from the decreasing diagonal direction.
        """

        total_value = 0
        for row in range(ROWS - 3):
            for col in range(COLUMNS - 3):
                loc = [grid[row+i][col+i] for i in range(4)]
                total_value += self._count_values(loc, player_number)
        return total_value

    def calculate_heuristic_value(self, grid, player_number):
        """Calculates total heuristic value (score) from the game grid.
        This value includes values from each directions and
        from the positional values.

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            int: Returns total heuristic value (score) from the game grid.
        """

        score = 0
        score += self._get_vertical_values(grid, player_number)
        score += self._get_horizontal_values(grid, player_number)
        score += self._get_inc_diagonal_values(grid, player_number)
        score += self._get_dec_diagonal_values(grid, player_number)
        score += self._get_positional_values(grid, player_number)
        return score

    def calculate_heuristic_value_w_bbs(self, position, player_index):
        """Calculates heuristic value for the player from the certain game situation.
        Player will get one point per each open 3 connect and reduce one point per each
        open 3 connect from opponent. Player will get additional 3 points for each coin
        placed in the middle column.

        Args:
            position (Position): Bitboard presentation (Position object)
            player_index (int): Player index (0 = first player, 1 = second player)

        Returns:
            int: Returns total heuristic value (score) from the game board.
        """

        return self._bb_service.calculate_heuristic_value(position, player_index)
