import math
import time
from services.heuristic_service import HeuristicService
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
        Several time variables are used to determine timeout limit for the
        AI functions.

        Args:
            situation (Situation): Situation service object
        """
        self._situation = situation
        self._bitboard = situation.bitboard
        self._heuristics = HeuristicService(self._bitboard)
        self._start_time = time.time()
        self._current_time = time.time()
        self._time_limit = 5
        self.counter = 0

        #Temp solution for testing. 1 = matrix, 2 = bitboard.
        self._board_presentation = 1

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

    def calculate_next_move_minimax(self, grid, player_number, depth=8):
        """Calculates next possible move using Minimax algorithm.
        This method is used for the intermediate level of AI.

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)
            depth (int, optional): Depth of the Minimax search. Defaults to 7.

        Returns:
            tuple: Returns column and row indexes of the next move location
        """
        self._board_presentation = 2
        self._time_limit = 20
        self._start_time = time.time()
        result = self._minimax(grid, player_number, depth, True)[1]
        print(time.time() - self._start_time)
        return result

    def _check_timeout(self):
        """Checks if certain time limit has exceeded.

        Returns:
            Boolean: Returns true if the limit has passed. Else returns false.
        """

        if self._time_limit + self._start_time < time.time():
            return True
        return False

    def calculate_next_move_id_minimax(self, grid, player_number):
        """Calculates next possible move using Minimax algorithm
        and iterative deepening. This method is used for the advanced level of AI:

        1.  Uses time limit of 5 seconds and initializes the start time.
        2.  Loops Minimax algorithm starting from depth 1 and ends if time has exceeded
            or if maximum depth has exceeded.
        3.  Keeps track of the heuristic value and move location for each iteration
        4.  Once the loop has ended, returns the last fully completed Minimax results

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)

        Returns:
            tuple: Returns column and row indexes of the next move location
        """

        self._board_presentation = 2
        locations = {}
        self._time_limit = 5
        self._start_time = time.time()
        depth = 1
        max_depth = self._situation.count_free_slots(grid)
        col_order = None

        while not self._check_timeout() and depth < max_depth:
            st = time.time()
            self.counter = 0
            locations[depth] = self._minimax(grid, player_number, depth, True, -math.inf, math.inf, col_order)
            col_order = [value[1] for value in sorted(locations[depth][2], reverse=True)]
            print(f"D: {depth} - Score: {locations[depth][0]} - Loc: {locations[depth][1]} - Order: {col_order}")
            print(f"total number of nodes searched {self.counter}")
            print(f"time spend for iteration: {time.time() - st}")
            depth += 1
        depth -= 1

        if depth == max_depth:
            return locations[depth][1]
        return locations[max(1, depth - 1)][1]

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

        score = self._heuristics.calculate_heuristic_value(grid, player_number)
        return score

    def _check_terminal_node(self, grid, player_number, opponent_number):
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
            opponent_number (int): Opposite for player number (2 = first player, 1 = second player)

        Returns:
            INF, -INF, 0 or None
        """
        #Temp solution for testing. 1 = matrix, 2 = bitboard.
        if self._board_presentation == 2:
            return self._bitboard.check_terminal_situations(grid, player_number)

        if self._situation.check_win(grid, player_number):
            return math.inf

        if self._situation.check_win(grid, opponent_number):
            return -math.inf

        if self._situation.check_draw(grid):
            return 0

        return None

    def _minimax(self, grid, player_number, depth, maximizing_player, 
                alpha=-math.inf, beta=math.inf, col_order=None):
        """Evalutes the most optimal next move using Minimax algorithm
        and fail-soft alpha beta pruning:

        0.  Check if the timer has ended. If so, returns location as a None and -INF value.
        1.  Check the terminal situation ie. when one of the players has won or game it is draw.
            Returns location as a None and values INF, -INF or 0.
        2.  If search has reached depth 0, returns heuristic value and location as a None.
        3.  Search all available locations where to put game coin. Available locations has been
            ranked to start closest to the middle column and ending closest to the side columns.

        4.  For the maximizing player:
            4.1 Sets max heuristic value -INF and loops through all locations to place a game coin
            4.2 For each of the locations, calls minimax algorithm with updated grid, smaller depth
                and sets turn for minimizing player (false).
            4.3 Keeps track of heuristic value and it's location recieved from minimax algorithm
            4.4 Updates the min score for maximizing player if heuristic value is greater than that
            4.5 Ends the loop if heuristic value is greater than maximum score for minimizing player
                ie. no need to investigate remaining branches.
            4.6 Returns maximum heuristic value and it's location

        5.  For the minimizing player:
            5.1 Sets min heuristic value INF and loops through all locations to place a game coin
            5.2 For each of the locations, calls minimax algorithm with updated grid, smaller depth
                and sets turn for maximising player (true).
            5.3 Keeps track of heuristic value and it's location recieved from minimax algorithm
            5.4 Updates the max score for minimizing player if heuristic value is less than that
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
        self.counter += 1
        if self._check_timeout():
            return (-math.inf, None, None)

        terminal_value = self._check_terminal_node(
            grid, player_number, player_number % 2 + 1)

        if terminal_value is not None:
            return (terminal_value, None, None)

        if depth == 0:
            return (self._heuristic_value(grid, player_number), None, None)

        if maximizing_player:
            if col_order is None:
                available_locations = self._situation.get_available_locations_ranked(grid)
            else:
                available_locations = col_order
            
            targeted_location = available_locations[0]
            max_value = -math.inf
            cols = []

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
                    cols.append((beta, location))
                    break
                
                cols.append((value, location))

            return max_value, targeted_location, cols

        available_locations = self._situation.get_available_locations_ranked(grid)
        targeted_location = available_locations[0]
        min_value = math.inf

        for location in available_locations:
            new_grid = self._copy_grid(grid)
            new_grid[location[0]][location[1]] = player_number % 2 + 1
            value = self._minimax(
                new_grid, player_number, depth - 1, True, alpha, beta)[0]

            if value < min_value:
                min_value = value
                targeted_location = location

            beta = min(beta, value)
            if value <= alpha:
                break

        return min_value, targeted_location, None
