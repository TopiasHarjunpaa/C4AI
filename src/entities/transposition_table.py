class TranspositionTable:

    def __init__(self):
        self._t_table = {}

    def get(self):
        return self._t_table

    def add(self, board, value, col):
        key = tuple(board)
        self._t_table[key] = [value, col]

    def check_match(self, board):
        key = tuple(board)
        if key in self._t_table.keys():
            return self._t_table[key]
        return None

    def reset(self):
        self._t_table = {}
