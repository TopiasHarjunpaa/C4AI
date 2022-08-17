from config import ROWS, COLUMNS, FULL_GRID, MID_COL, BORDERS
from entities.position import Position


class BitboardService:
    """A class to represent Bitboard services mainly using binary operations.

        Bitboards is list of two 64 bit. One for player and one for opponent.
        Each location on a board is indicated by the bit number.
        0-bit is empty and 1-bit is reserved.

        6 13 20 27 34 41 48   55 62     Additional row
        +---------------------+
        | 5 12 19 26 33 40 47 | 54 61     top row
        | 4 11 18 25 32 39 46 | 53 60
        | 3 10 17 24 31 38 45 | 52 59
        | 2  9 16 23 30 37 44 | 51 58
        | 1  8 15 22 29 36 43 | 50 57
        | 0  7 14 21 28 35 42 | 49 56 63  bottom row
        +---------------------+

        Bitboard presentation according to the following guide:
        https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md
    """

    def convert_to_position(self, grid):
        """Converts current game grid (list matrix) into the bitboard presentation
        as a Position object.

        Args:
            grid (list): Grid matrix of the game board.

        Returns:
            Position: Bitboard presentation (Position object)
        """

        bitboard = self.convert_to_bitboard(grid)
        heights = self.convert_to_heights(grid)
        return Position(bitboard, heights)

    def convert_to_bitboard(self, grid):
        """Converts current game grid (list matrix) into the bitboard.

        Args:
            grid (list): Grid matrix of the game board.

        Returns:
            list: list of two 64 bit integers
        """

        first_player = '0' * 15
        second_player = '0' * 15
        for col in reversed(range(COLUMNS)):
            first_player += '0'
            second_player += '0'
            for row in range(ROWS):
                if grid[row][col] == 0:
                    first_player += '0'
                    second_player += '0'
                if grid[row][col] == 1:
                    first_player += '1'
                    second_player += '0'
                if grid[row][col] == 2:
                    first_player += '0'
                    second_player += '1'
        return [int(first_player, 2), int(second_player, 2)]

    def convert_to_heights(self, grid):
        """Converts current game grid (list matrix) into the heights.
        Heights is list of integers each representing bit number of the
        first free row for each column.

        Args:
            grid (list): Grid matrix of the game board.

        Returns:
            list: list of integers each representing bit number at the board
        """

        heights = []
        for col in range(COLUMNS):
            height = col * 7 + 6
            for row in reversed(range(ROWS)):
                if grid[row][col] == 0:
                    height = col * 7 + (5 - row)
                    break
            heights.append(height)
        return heights

    def check_win(self, player_bitboard):
        """Checks if the player has won the game ie. gets four connect using binary
        operations. Multipliers are used to determine gap between bit numbers in certain
        direction:

        Gap is 1 when checks for connect in vertical direction
        Gap is 6 when checks for connect in decreasing diagonal direction
        Gap is 7 when checks for connect in horizontal direction
        Gap is 8 when checks for connect in increasing diagonal direction

        Args:
            player_bitboard (int): 64 bit integer representing bitboard of whose win is checked.

        Returns:
            boolean: Returns true if player has got four connect, else returns false
        """

        multipliers = [1, 7, 6, 8]

        for mul in multipliers:
            inter_res = player_bitboard & (player_bitboard >> mul)
            if inter_res & (inter_res >> (2 * mul)) != 0:
                return True
        return False

    def check_draw(self, bitboard):
        """Checks if the game has ended draw.
        Game is draw if game board is full of coins ie. all bits are 1-bits.
        FULL_GRID is 64 bit integer full of 1-bits.

        Args:
            bitboard (int): list of two 64 bit integers

        Returns:
            Boolean: Returns true if game is draw, otherwise returns false.
        """

        if (bitboard[0] | bitboard[1]) == FULL_GRID:
            return True
        return False

    def check_terminal_node(self, position, player_index):
        """Checks if the game situation means that the game has ended.

        Game ends if one of the player has gotten connect four. If the player has won
        the method will return positive value which is 1000 times the number of remaining
        moves for the player. If the opponent has won, the method will return negative value
        which is -1000 times the number of remaining moves for the opponent.
        Game will end as draw if the game board is full and none of the players
        has not won. In this case return value will be 0.

        Game hasn't ended if none of the player has not won and the game board is not
        full. In that case return value will be None.

        Args:
            position (Position): Bitboard presentation (Position object)
            player_index (int): Player index (0 = first player, 1 = second player)

        Returns:
            positive integer, negative integer, 0 or None.
        """

        bitboard = position.get_bitboard()
        opponent_index = (player_index + 1) % 2

        if self.check_win(bitboard[player_index]):
            return (22 - self.count_coins(bitboard[player_index])) * 1000

        if self.check_win(bitboard[opponent_index]):
            return (-22 + self.count_coins(bitboard[opponent_index])) * 1000

        if self.check_draw(bitboard):
            return 0

        return None

    def count_coins(self, player_bitboard):
        """Count number of coins for one of the player. For each players
        bitboard contains 1-bit for each coin placed on the game board.
        Number of coins will be recieved by counting number of 1-bits found
        from player bitboard

        Args:
            player_bitboard (int): 64 bit integer representing bitboard of whose coins are counted.

        Returns:
            int: Number of coins placed on the game board for one player.
        """

        coins = bin(player_bitboard).count('1')
        return coins

    def calculate_heuristic_value(self, position, player_index):
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

        points = 0
        bitboard = position.get_bitboard()
        opponent_index = (player_index + 1) % 2
        player_bb = bitboard[player_index]
        opponent_bb = bitboard[opponent_index]
        points += self.check_three_connect(player_bb, opponent_bb)
        points -= self.check_three_connect(opponent_bb, player_bb)
        points += 3 * bin(bitboard[player_index] & MID_COL).count('1')
        return points

    def check_three_connect(self, player_bitboard, opponent_bitboard):
        """Counts number of open 3 connects for one of the player at the current game
        situation using binary operations. Opponent bitboard will be modified by the
        BORDERS wich contains all the bit numbers outside of the game board as 1-bits ie.
        opponent has "closed the outside areas of board". This prevents counting the bits
        outside of the game board.

        Args:
            player_bitboard (int): 64 bit integer repr. bitboard of whose3 connects are counted.
            opponent_bitboard (int): 64 bit integer repr. bitboard of the opponent.

        Returns:
            int: Count of open 3 connects in all directions.
        """

        count = 0
        multipliers = [1, 7, 6, 8]
        opponent_bitboard = opponent_bitboard | BORDERS
        for mul in multipliers:
            inter_res = player_bitboard & (player_bitboard << mul)
            threes = (inter_res & (inter_res << mul)) << mul
            mask = threes & opponent_bitboard
            threes = threes - mask
            count += bin(threes).count('1')
            inter_res = player_bitboard & (player_bitboard >> mul)
            threes = (inter_res & (inter_res >> mul)) >> mul
            mask = threes & opponent_bitboard
            threes = threes - mask
            count += bin(threes).count('1')
        return count

    def is_symmetrical(self, bitboard):
        """Checks if the game board is symmetrical.
        Compares first and last columns, second first and second last columns
        and third first and third last columns. Returns true if these matches
        in all comparisons for the both bitboards. Otherwise returns false.

        Args:
            bitboard (int): list of two 64 bit integers

        Returns:
            boolean: Returns true if game board is symmetrical, otherwise returns false.
        """

        for i in range(2):
            for j in range(3):
                if ((bitboard[i] >> j * 7) & 0b111111) != ((bitboard[i] >> 42 - j * 7) & 0b111111):
                    return False
        return True

    def get_available_non_losing_columns(self, position, player_index, check_symmetry=False):
        """Checks if the opponent has forced player to put coins into certain
        column in order to prevent opponents victory at the next turn. If so,
        all other columns will lead to lose and can be left out from available
        column list.

        1.  Checks symmetry if game board has been considered symmetrical before new iteration.
            Chooses only left sided columns if game board is found to still be symmetrical.
        2.  Checks available current available columns.
        3.  Loops through available columns.
        4.  Creates new move for each available columns and checks for the victory.
        5.  Adds all columns leading victory to the column list.
        6.  If victories has found, returns only list with columns to prevent victory
            (one column can be saved, multiple columns will lead to lose anyway).
        7.  Normal available columns list can be used if no victories are found.

        Args:
            position (Position): Bitboard presentation (Position object)
            player_index (int): Player index (0 = first player, 1 = second player)
            check_symmetry (bool, optional): True if game board is symmetrical. Defaults to False.

        Returns:
            list: list of column indexes representing available non losing columns
        """

        if check_symmetry:
            available_cols = position.get_available_columns(
                self.is_symmetrical(position.get_bitboard()))
        else:
            available_cols = position.get_available_columns()

        cols = []
        opponent_index = (player_index + 1) % 2
        for col in available_cols:
            board, heights = position.get_params()
            new_position = Position(board, heights)
            new_position.make_move(col, opponent_index)
            if self.check_win(new_position.get_bitboard()[opponent_index]):
                cols.append(col)
        if len(cols) != 0:
            return cols
        return available_cols
