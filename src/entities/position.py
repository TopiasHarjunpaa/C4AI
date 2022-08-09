from config import TOP_ROW

class Position:

    def __init__(self, bitboard=None, heights=None, counter=0, moves=None):
        self.bitboard = bitboard
        if bitboard is None:
            self.bitboard = [0, 0]
        self.heights = heights
        if heights is None:
            self.heights = [0, 7, 14, 21, 28, 35, 42]
        self.counter = counter
        self.moves = moves
        if moves is None:
            self.moves = []

    def get_bitboard(self):
        return self.bitboard

    def get_heights(self):
        return self.heights

    def get_counter(self):
        return self.counter

    def get_moves(self):
        return self.moves

    def get_params(self):
        bitboard = self.bitboard.copy()
        heights = self.heights.copy()
        counter = self.counter
        moves = self.moves.copy()
        return [bitboard, heights, counter, moves]

    def make_move(self, col):
        move = 1 << self.heights[col]
        self.heights[col] += 1
        self.bitboard[(self.counter & 1)] ^= move
        self.counter += 1
        self.moves.append(col)

    def get_available_columns(self):
        cols = []
        column_order = [3,2,4,1,5,0,6]
        for col in column_order:
            if (TOP_ROW & (1 << self.heights[col])) == 0:
                cols.append(col)
        return cols
