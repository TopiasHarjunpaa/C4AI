class TranspositionTable:

    def __init__(self):
        self._t_table = {}

    def add(self, board, value, depth, col, maximising_player):
        key = tuple(board)
        self._t_table[key] = [value, depth, col, maximising_player]

    def check_match(self, board, search_depth, maximizing_player):
        key = tuple(board)
        if key in self._t_table.keys():
            value, saved_depth, col, max_player = self._t_table[key]
            if saved_depth >= search_depth and max_player == maximizing_player:
                return value, col
        return None

    def reset(self):
        self._t_table = {}
