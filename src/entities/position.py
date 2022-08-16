from config import TOP_ROW


class Position:
    """A class to represent position object. This is object represents
    current game state by using bitboard presentation.

    Attributes:
        bitboard: list of two 64 bit integers
        heights: list of integers each representing bit number at the board
    """

    def __init__(self, bitboard, heights):
        """Constructs all the necessary attributes for the position object.

        Bitboards is list of two 64 bit. One for player and one for opponent.
        Each location on a board is indicated by the bit number.
        0-bit is empty and 1-bit is reserved.

        Heights is list of integers each representing bit number of the
        first free row for each column.

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

        Args:
            bitboard: list of two 64 bit integers
            heights: list of integers each representing bit number at the board
        """
        self.bitboard = bitboard
        self.heights = heights

    def get_bitboard(self):
        return self.bitboard

    def get_heights(self):
        return self.heights

    def get_params(self):
        """Copies and returns object parameters.

        Returns:
            list: Returns list of copied objec parameters.
        """

        bitboard = self.bitboard.copy()
        heights = self.heights.copy()
        return [bitboard, heights]

    def make_move(self, col, player_index):
        """Makes a move according to column index and updates
        heights list and current players bitboard.

        Args:
            col (int): Column index
            player_index (int): Player index (0 = first player, 1 = second player)
        """

        move = 1 << self.heights[col]
        self.heights[col] += 1
        self.bitboard[player_index] ^= move

    def get_available_columns(self):
        """Returns available columns where to put coins ranked by middlest column
        order. TOP_ROW corresponds bit numbers of 6, 13, 20, 27, 34, 41 and 48 which
        are located right above the top-most game board row. If bit operation results
        value of 1, it means that the current column is already full and it will be
        left out from the available columns.

        Returns:
            list: List of available column indexes ranked in order
        """

        cols = []
        column_order = [3, 2, 4, 1, 5, 0, 6]

        for col in column_order:
            if (TOP_ROW & (1 << self.heights[col])) == 0:
                cols.append(col)
        return cols
