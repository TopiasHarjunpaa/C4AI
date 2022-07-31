import math
from config import ROWS, COLUMNS


class AiService:
    """A class to represent AI services.
    AI service purpose is to determine or calculate which
    move the (computer) player will make.

    Attributes:
        situation: Situation service object.
    """

    def __init__(self, situation):
        """Constructs all the necessary attributes for the AI service object.

        Args:
            situation (Situation): Situation service object
        """
        self._situation = situation

    def _copy_grid(self, grid):
        """Creates copy of the grid using list comprehension.

        Args:
            grid (list): Grid matrix of the game board.

        Returns:
            list: Returns copied list from the grid
        """
        
        return [[grid[row][col] for col in range(COLUMNS)] for row in range(ROWS)]

    def calculate_next_move_basic(self, grid, player_number):
        """Calculates one of the possible moves using heuristic calculation.
        This method is used for the basic level AI:
        
        1.  Search all available locations where to put game coin.
        2.  Loops through all locations places a game coin on that location
            and calculate heurestic values of each move.
        3.  Keeps track of maximum heuristic value and it's location
        4.  Returns location which gives the highest heuristic value

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            tuple: Returns column and row indexes of the next move location
        """

        max_value = -math.inf
        available_locations = self._situation.get_available_locations(grid)
        targeted_location = available_locations[0]
        
        for location in available_locations:
            new_grid = self._copy_grid(grid)
            new_grid[location[0]][location[1]] = player_number
            value = self._heuristic_value(new_grid, player_number)          
            
            if value > max_value:
                max_value = value
                targeted_location = location
        
        return targeted_location

    def calculate_next_move_minimax(self, grid, player_number, depth=6):
        """Calculates next possible move using Minimax algorithm.
        This method is used for the intermediate level of AI.

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)
            depth (int, optional): Depth of the Minimax search. Defaults to 6.

        Returns:
            tuple: Returns column and row indexes of the next move location
        """

        return self._minimax(grid, player_number, depth, True)[1]

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
        multipliers = {0: 10000, 1: 10, 2: 2}
        for k, v in multipliers.items():
            if loc.count(player_number) == 4 - k and loc.count(0) == k:
                value += v

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

    def _heuristic_value(self, grid, player_number):
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

    def _check_terminal_node(self, grid, player_number, opponent_number):
        if self._situation.check_win(grid, player_number):
            return math.inf

        if self._situation.check_win(grid, opponent_number):
            return -math.inf

        if self._situation.check_draw(grid):
            return 0
        
        return None

    def _minimax(self, grid, player_number, depth, maximizing_player, alpha=-math.inf, beta=math.inf):
        """Evalutes the most optimal next move using Minimax algorithm and fail-soft alpha beta pruning:

        1.  Check the terminal situation ie. when one of the players has won or game it is draw.
            Returns location as a None and values INF, -INF or 0.
        2.  If search has reached depth 0, returns heuristic value and location as a None.
        3.  Search all available locations where to put game coin.          
        
        4.  For the maximizing player:
            4.1 Sets maximum heuristic value -INF and loops through all locations to place a game coin
            4.2 For each of the locations, calls minimax algorithm with updated grid, smaller depth
                and sets turn for minimizing player (false).
            4.3 Keeps track of heuristic value and it's location recieved from minimax algorithm
            4.4 Updates the minimum score for maximizing player if heuristic value is greater than that
            4.5 Ends the loop if heuristic value is greater than maximum score for minimizing player
                ie. no need to investigate remaining branches.
            4.6 Returns maximum heuristic value and it's location
        
        5.  For the minimizing player:
            5.1 Sets minimum heuristic value INF and loops through all locations to place a game coin
            5.2 For each of the locations, calls minimax algorithm with updated grid, smaller depth
                and sets turn for maximising player (true).
            5.3 Keeps track of heuristic value and it's location recieved from minimax algorithm
            5.4 Updates the maximum score for minimizing player if heuristic value is less than that
            5.5 Ends the loop if heuristic value is less than minimum score for maximizing player
                ie. no need to investigate remaining branches.
            5.6 Returns minimum heuristic value and it's location
            
        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)
            depth (int): Depth of the minimax search
            maximizing_player (boolean): True looks for max score and false min score
            alpha (int, optional): Minimum score for maximizing player. Defaults to -INF.
            beta (int, optional): Maximum score for minimizing player. Defaults to INF.

        Returns:
            tuple: Returns tuple which first item is heuristic value of the next move and
            second item contains location coordinates of the next move (row index, col index)
        """

        opponent_number = player_number % 2 + 1
        terminal_value = self._check_terminal_node(grid, player_number, opponent_number)
        
        if terminal_value != None:
            return (terminal_value, None)
        elif depth == 0:
            return (self._heuristic_value(grid, player_number), None)

        available_locations = self._situation.get_available_columns(grid)
        targeted_location = available_locations[0]

        if maximizing_player:
            max_value = -math.inf

            for location in available_locations:
                new_grid = self._copy_grid(grid)
                new_grid[location[0]][location[1]] = player_number
                value = self._minimax(
                    new_grid, player_number, depth - 1, False, alpha, beta)[0]

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
                new_grid = self._copy_grid(grid)
                new_grid[location[0]][location[1]] = opponent_number
                value = self._minimax(
                    new_grid, player_number, depth - 1, True, alpha, beta)[0]
               
                if value < min_value:
                    min_value = value
                    targeted_location = location

                beta = min(beta, value)
                if value <= alpha:
                    break

            return min_value, targeted_location
