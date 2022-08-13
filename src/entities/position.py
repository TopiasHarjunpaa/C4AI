from config import TOP_ROW


class Position:

    def __init__(self, bitboard, heights):
        self.bitboard = bitboard
        self.heights = heights

    def get_bitboard(self):
        return self.bitboard

    def get_heights(self):
        return self.heights

    def get_params(self):
        bitboard = self.bitboard.copy()
        heights = self.heights.copy()
        return [bitboard, heights]

    def make_move(self, col, player_index):
        move = 1 << self.heights[col]
        self.heights[col] += 1
        self.bitboard[player_index] ^= move

    def get_available_columns(self):
        cols = []
        column_order = [3, 2, 4, 1, 5, 0, 6]

        for col in column_order:
            if (TOP_ROW & (1 << self.heights[col])) == 0:
                cols.append(col)
        return cols
