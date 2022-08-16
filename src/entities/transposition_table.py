class TranspositionTable:
    """A class to represent Transposition table.
    Transposition table is used to store game situations
    in order to prevent calculating certain nodes multiple times
    during the Minimax search.
    """

    def __init__(self):
        """Initializes dictionary to store game situations.
        """

        self._t_table = {}

    def get(self):
        return self._t_table

    def add(self, board, value, col):
        """Adds game situation to the transposition table.

        Args:
            board (list): list of two 64 bit integers
            value (int): Heuristic value of the chose column
            col (int): Column index
        """

        key = tuple(board)
        self._t_table[key] = [value, col]

    def check_match(self, board):
        """Check if the key matches. Converts list into the tuple
        which is used as a dictionary key.

        Args:
            board (list): list of two 64 bit integers

        Returns:
            list: Returns list containing heuristic value and column index
            if key matches. Else returns None.
        """

        key = tuple(board)
        if key in self._t_table.keys():
            return self._t_table[key]
        return None

    def reset(self):
        self._t_table = {}
