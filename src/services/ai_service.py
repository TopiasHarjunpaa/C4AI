import math
import time
from services.heuristic_service import HeuristicService
from services.bitboard_service import BitboardService
from entities.position import Position
from entities.transposition_table import TranspositionTable


class AiService:
    """A class to represent AI services.
    AI service purpose is to determine or calculate which
    move the (computer) player will make.

    Attributes:
        situation: Situation service object.
    """

    def __init__(self, situation):
        """Constructs all the necessary attributes for the AI service object.

        1.  BitboardService is used for the advanced AI's bitboard operations.
        2.  HeuristicService is used for calculation heuristic values.
        3.  TranspositionTable is used for the advanced AI to store game situations.
        4.  Several time variables are used to determine timeout limit for the
            AI functions.
        5.  Time limit is used for iterative deepening and symmetria is for the advanced
            AI to narrow down the search three while the game board is symmetrical.

        Args:
            situation (Situation): Situation service object
        """

        self._situation = situation
        self._bb_service = BitboardService()
        self._heuristics = HeuristicService(self._bb_service)
        self.transposition_table = TranspositionTable()
        self._start_time = time.time()
        self._current_time = time.time()
        self._time_limit = 5
        self.counter = 0
        self.printer = False
        self.symmetry = True

    def _check_timeout(self):
        """Checks if certain time limit has exceeded.

        Returns:
            Boolean: Returns true if the limit has passed. Else returns false.
        """

        if self._time_limit + self._start_time < time.time():
            return True
        return False

    def print_results(self, depth, score, location, time_spend):
        """To print results for debugging purposes

        Args:
            depth (int): Current search depth
            score (int): Heuristic value of certain node
            location (tuple): Location of the move
            time_spend (float)): Time used for certain calculation
        """

        if self.printer:
            print((f"D: {depth} - Score: {score} - Location: {location}"))
            print(f"total number of nodes searched {self.counter}")
            print(f"time spend for iteration: {time_spend}")
            print("")

    def sort_column_order(self, columns):
        """Sorts available column order primarily by heuristic values
        and secondarily by the middle column order (default order)

        Args:
            columns (list): List of available columns

        Returns:
            list: Returns sorted list of available columns
        """

        column_order = []
        default_order = [3, 2, 4, 1, 5, 0, 6]
        values = sorted(set(map(lambda x: x[0], columns)), reverse=True)
        grouped_by_value = [[t[1]
                             for t in columns if t[0] == value] for value in values]
        for cols in grouped_by_value:
            for col in default_order:
                if col in cols:
                    column_order.append(col)
        return column_order

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
            new_grid = self._situation.copy_grid(grid)
            new_grid[location[0]][location[1]] = player_number
            value = self._heuristics.calculate_heuristic_value(
                new_grid, player_number)

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

        start_t = time.time()
        self.counter = 0
        result = self._minimax(grid, player_number, depth, True)
        self.print_results(depth, result[0], result[1], time.time() - start_t)

        return result[1]

    def calculate_next_move_id_minimax(self, grid, player_number, timeout=6, max_depth=42):
        """Calculates next possible move using Minimax algorithm
        and iterative deepening. This method is used for the advanced level of AI:

        1.  Converts game grid into the bitboard presentation (position Object).
        2.  Sets ranked column order from available columns which do not lead to lose
            in a next round. Considers only left handed columns if game board is still symmetrical.
        3.  Uses time limit of 6 seconds and initializes the start time. In order to
            improve performance it is not using hard time limit. Allows next iteration
            if time limit divided by 3 is not exceeded.
        4.  Loops Minimax algorithm starting from depth 1 and ends if time has exceeded
            or if maximum depth has exceeded.
        5.  Keeps track of columns and their heuristic values for each iteration separately.
        6.  Updates column order and depth by one after each iteration.
        7.  Once the loop has ended, returns column number with best heuristic value from
            previous iteration (deepest achieved during time limit).

        Args:
            grid (list): Grid matrix of the game board.
            player_number (int): Player number (1 = first player, 2 = second player)
            timeout (int): Time limit for iterative search
            max_depth (int): Maximum depth for the search. Defaults to 42.

        Returns:
            tuple: Returns column index of the next move location
        """

        position = self._bb_service.convert_to_position(grid)
        player_index = player_number - 1
        self.printer = True
        locations = {}
        self.symmetry = self._bb_service.is_symmetrical(
            position.get_bitboard())
        column_order = self._bb_service.get_available_non_losing_columns(
            position, player_index, self.symmetry)
        self._time_limit = timeout / 3
        self._start_time = time.time()
        start_t = time.time()  # To prevent printing bug when draw
        locations[0] = None, None, None  # When board is full
        depth = 1
        round_number = 43 - self._situation.count_free_slots(grid)
        max_depth = min(43 - round_number, max_depth)

        if self.printer:
            print("")
            print(f"Round number: {round_number}")

        while not self._check_timeout() and depth <= max_depth:
            self.transposition_table.reset()
            start_t = time.time()
            self.counter = 0
            locations[depth] = self._minimax_with_id_and_bb(
                position, player_index, depth, True, -math.inf, math.inf, column_order)
            column_order = self.sort_column_order(locations[depth][2])
            depth += 1
        depth -= 1

        print(f"Table length {len(self.transposition_table.get())}")
        if self.printer:
            if depth == max_depth:
                print(f"Max depth {max_depth} reached.")
            else:
                print(f"Terminated after depth {depth}.")
        self.print_results(
            depth, locations[depth][0], locations[depth][1], time.time() - start_t)

        return locations[depth][1]

    def _minimax_with_id_and_bb(self, position, player_index, depth, maximizing_player,
                                alpha=-math.inf, beta=math.inf, column_order=None):
        """Evalutes the most optimal next move using Minimax algorithm
        and fail-soft alpha beta pruning:

        0.  Check if similar game situation can be found from the transposition table. Returns
            the value stored in transposition table is match is found.
        1.  Check the terminal situation ie. when one of the players has won or game it is draw.
            Returns location as a None and values depending from the terminal situation.
        2.  If search has reached depth 0, returns heuristic value and location as a None.
        3.  Search all columns where to put game coin. Available locations has been
            ranked primarily by heuristic values and secondarily to start closest to the middle
            column and ending closest to the side columns. In addition to that symmetria is used
            to narrow search three if possible.

        4.  For the maximizing player:
            4.1 Sets max heuristic value -INF and loops through all columns to place a game coin
            4.2 For each columns, calls minimax algorithm with updated bitboard
                (new position object), smaller depth and sets turn for minimizing player (false).
            4.3 Stores Minimax result into the transposition table.
            4.4 Keeps track of heuristic value and column index recieved from minimax algorithm
            4.5 Updates the min score for maximizing player if heuristic value is greater than that
            4.6 Ends the loop if heuristic value is greater than maximum score for minimizing player
                ie. no need to investigate remaining branches.
            4.7 Stores column indexes and their heuristic values
            4.8 Returns maximum heuristic value, column and list of columns and heuristic values

        5.  For the minimizing player:
            5.1 Sets min heuristic value INF and loops through all columns to place a game coin
            5.2 For each columns, calls minimax algorithm with updated bitboard
                (new position object), smaller depth and sets turn for maximising player (true).
            5.3 Keeps track of heuristic value and column index recieved from minimax algorithm
            5.4 Updates the max score for minimizing player if heuristic value is less than that
            5.5 Ends the loop if heuristic value is less than minimum score for maximizing player
                ie. no need to investigate remaining branches.
            5.6 Stores column indexes and their heuristic values
            5.7 Returns minimum heuristic value, column and list of columns and heuristic values

        Args:
            position (Position): Bitboard presentation object named as position
            player_index (int): Player index (0 = first player, 1 = second player)
            depth (int): Depth of the minimax search
            maximizing_player (boolean): True looks for max score and false min score
            alpha (int, optional): Minimum score for maximizing player. Defaults to -INF.
            beta (int, optional): Maximum score for minimizing player. Defaults to INF.
            column_order (list, optional): Ranked order of available columns. Defaults to None.

        Returns:
            tuple: Returns tuple which first item is heuristic value of the next move,
            second item contains column index of the next move and third item contains
            list of columns and their heuristic values.
        """

        self.counter += 1

        match = self.transposition_table.check_match(position.get_bitboard())
        if match is not None:
            return match

        terminal_value = self._bb_service.check_terminal_node(
            position, player_index)

        if terminal_value is not None:
            return (terminal_value, None, None)

        if depth == 0:
            return (self._heuristics.calculate_heuristic_value_w_bbs(
                position, player_index), None, None)

        if maximizing_player:
            if column_order is None:
                columns = self._bb_service.get_available_non_losing_columns(
                    position, player_index, self.symmetry)
            else:
                columns = column_order

            column = None
            max_value = -math.inf
            cols = []

            for col in columns:
                board, heights = position.get_params()
                new_position = Position(board, heights)
                new_position.make_move(col, player_index)
                value = self._minimax_with_id_and_bb(new_position, player_index, depth - 1,
                                                     False, alpha, beta)[0]

                self.transposition_table.add(board, value, column)

                if value > max_value:
                    max_value = value
                    column = col

                alpha = max(alpha, value)
                if value >= beta:
                    cols.append((beta, col))
                    break

                cols.append((value, col))

            return max_value, column, cols

        columns = self._bb_service.get_available_non_losing_columns(
            position, player_index, self.symmetry)
        column = None
        min_value = math.inf

        for col in columns:
            board, heights = position.get_params()
            new_position = Position(board, heights)
            new_position.make_move(col, (player_index + 1) % 2)
            value = self._minimax_with_id_and_bb(new_position, player_index, depth - 1,
                                                 True, alpha, beta)[0]

            if value < min_value:
                min_value = value
                column = col

            beta = min(beta, value)
            if value <= alpha:
                break

        return min_value, column, None

    def _minimax(self, grid, player_number, depth, maximizing_player,
                 alpha=-math.inf, beta=math.inf):
        """Evalutes the most optimal next move using Minimax algorithm
        and fail-soft alpha beta pruning:

        0.  Check if the timer has ended. If so, returns location as a None and -INF value.
        1.  Check the terminal situation ie. when one of the players has won or game it is draw.
            Returns location as a None and values INF, -INF or 0.
        2.  If search has reached depth 0, returns heuristic value and location as a None.
        3.  Search all non losing available locations where to put game coin. Available columns has
            been ranked starting closest to middle column and ending closest to side columns.

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
        terminal_value = self._situation.check_terminal_node(
            grid, player_number)

        if terminal_value is not None:
            return (terminal_value, None)

        if depth == 0:
            return (self._heuristics.calculate_heuristic_value(grid, player_number), None)

        available_locations = self._situation.get_available_locations_ranked(
            grid)
        targeted_location = available_locations[0]

        if maximizing_player:
            max_value = -math.inf

            for location in available_locations:
                new_grid = self._situation.copy_grid(grid)
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

        min_value = math.inf

        for location in available_locations:
            new_grid = self._situation.copy_grid(grid)
            new_grid[location[0]][location[1]] = player_number % 2 + 1
            value = self._minimax(
                new_grid, player_number, depth - 1, True, alpha, beta)[0]

            if value < min_value:
                min_value = value
                targeted_location = location

            beta = min(beta, value)
            if value <= alpha:
                break

        return min_value, targeted_location
