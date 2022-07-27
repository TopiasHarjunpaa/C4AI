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

        available_locations = self._situation.get_available_locations(self._situation.get_game_grid())
        location = random.choice(available_locations)
        return location

    def calculate_next_move(self, grid, player_number):
        max_value = -math.inf
        available_locations = self._situation.get_available_locations(self._situation.get_game_grid())
        targeted_location = available_locations[0]
        for location in available_locations:

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
    
    def calculate_move_minimax(self, grid, player_number):
        return self.minimax(grid, player_number, 6, True)[1]

    def count_values(self, loc, player_number):
        opponent_number = player_number % 2 + 1
        value = 0
        multipliers = {0: 10000, 1: 10, 2: 2}
        for k, v in multipliers.items():
            if loc.count(player_number) == 4 - k and loc.count(0) == k:
                value += v

        if loc.count(opponent_number) == 3 and loc.count(0) == 1:
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
        for col in range(COLUMNS):
            col = [row[col] for row in grid]
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
        for row in range(3, ROWS):
            for col in range(COLUMNS - 3):
                loc = [grid[row-i][col+i] for i in range(4)]
                value += self.count_values(loc, player_number)
        return value

    def get_dec_diagonal_values(self, grid, player_number):
        value = 0
        for row in range(ROWS - 3):
            for col in range(COLUMNS - 3):
                loc = [grid[row+i][col+i] for i in range(4)]
                value += self.count_values(loc, player_number)
        return value

    def heurestic_value(self, grid, player_number):
        score = 0
        score += self.get_vertical_values(grid, player_number)
        score += self.get_horizontal_values(grid, player_number)
        score += self.get_inc_diagonal_values(grid, player_number)
        score += self.get_dec_diagonal_values(grid, player_number)
        score += self.get_positional_values(grid, player_number)
        return score
    
    def minimax(self, grid, player_number, depth, maximizing_player, alpha=-math.inf, beta=math.inf):
        opponent_number = player_number % 2 + 1
       
        if depth == 0:
            return (self.heurestic_value(grid, player_number), None)
        
        if self._situation.check_win(grid, player_number):
            return (math.inf, None)
        
        if self._situation.check_win(grid, opponent_number):
            return (-math.inf, None)
        
        if self._situation.check_draw(grid):
            return (0, None)
        
        available_locations = self._situation.get_available_columns(grid)
        targeted_location = available_locations[0]
        
        if maximizing_player:
            max_value = -math.inf
            
            for location in available_locations:

                # Fix this one later...
                new_grid = []
                for row in grid:
                    new_row = []
                    for col in row:
                        new_row.append(col)
                    new_grid.append(new_row)
                # ...

                new_grid[location[0]][location[1]] = player_number   
                value = self.minimax(new_grid, player_number, depth - 1, False, alpha, beta)[0]

                if value > max_value:
                    max_value = value
                    targeted_location = location
                
                alpha = max(alpha, value)
                if value >= beta:
                    break

            return max_value, targeted_location
        
        else:
            min_value = math.inf
            
            for location in available_locations:

                # Fix this one later...
                new_grid = []
                for row in grid:
                    new_row = []
                    for col in row:
                        new_row.append(col)
                    new_grid.append(new_row)
                # ...

                new_grid[location[0]][location[1]] = opponent_number
                value = self.minimax(new_grid, player_number, depth - 1, True, alpha, beta)[0]
                if value < min_value:
                    min_value = value
                    targeted_location = location
                
                beta = min(beta, value)
                if value <= alpha:
                    break
                
            return min_value, targeted_location
        
