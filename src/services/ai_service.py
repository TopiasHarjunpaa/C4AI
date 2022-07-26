import random
import math
from config import ROWS, COLUMNS


class AiService:
    """A class to represent AI services.

    Attributes:
        situation: Situation service object.
    """

    def __init__(self, situation):
        """Constructs all the necessary attributes for the AI service object.

        Args:
            situation (Situation): Situation service object
        """
        self._situation = situation

    def calculate_move_randomly(self):
        """Calculates next move randomly.
        Checks first available columns to put coin
        and chooses randomly one of the available columns.

        Returns:
            int: Index of the chosen column.
        """

        available_columns = self._situation.get_available_columns()
        column_number = random.choice(available_columns)[1]
        return column_number

    def calculate_next_move(self, grid, player_number):
        max_value = -math.inf
        available_columns = self._situation.get_available_columns()
        targeted_location = available_columns[0]
        for location in available_columns:

            # Fix this one later...
            new_grid = []
            for row in grid:
                new_row = []
                for col in row:
                    new_row.append(col)
                new_grid.append(new_row)
            # ...

            new_grid[location[0]][location[1]] = player_number
            value = self.heurestic_value(new_grid, player_number)
            if value > max_value:
                max_value = value
                targeted_location = location
        return targeted_location

    def count_values(self, loc, player_number):
        opponent_number = player_number % 2 + 1
        value = 0
        multipliers = {0: 10000, 1: 10, 2: 2}
        for key, value in multipliers.items():
            if loc.count(player_number) == 4 - key and loc.count(0) == key:
                value += value

        if loc.count(opponent_number) == 4 - 1 and loc.count(0) == 1:
            value -= 25

        return value

    def get_positional_values(self, grid, player_number):
        value = 0
        center_col = [row[3] for row in grid]
        side_cols = [row[2] for row in grid] + [row[4] for row in grid]
        value += center_col.count(player_number) * 2
        value += side_cols.count(player_number) * 1
        return value

    def get_vertical_values(self, grid, player_number):
        value = 0
        for i in range(COLUMNS):
            col = [row[i] for row in grid]
            for row in range(ROWS - 3):
                loc = col[row:row + 4]
                value += self.count_values(loc, player_number)
        return value

    def get_horizontal_values(self, grid, player_number):
        value = 0
        for row in range(ROWS):
            row = grid[row]
            for col in range(COLUMNS - 3):
                loc = row[col:col + 4]
                value += self.count_values(loc, player_number)
        return value

    def get_inc_diagonal_values(self, grid, player_number):
        value = 0
        # To be added
        return value

    def get_dec_diagonal_values(self, grid, player_number):
        value = 0
        # To be added
        return value

    def heurestic_value(self, grid, player_number):
        score = 0
        score += self.get_vertical_values(grid, player_number)
        score += self.get_horizontal_values(grid, player_number)
        score += self.get_inc_diagonal_values(grid, player_number)
        score += self.get_dec_diagonal_values(grid, player_number)
        score += self.get_positional_values(grid, player_number)
        return score
