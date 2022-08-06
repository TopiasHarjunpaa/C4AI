import math
from config import ROWS, COLUMNS


class BitboardService:
    """A class to represent Bitboard services"""

    def __init__(self):
        self._full_grid = int('0' * 14 + '0111111' * COLUMNS, 2)

    def convert_to_bitboard(self, grid):
        first_player = '0' * 14
        second_player = '0' * 14
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

    def check_win(self, bitboards, player_number):
        bitboard = bitboards[player_number - 1]
        multipliers = [1, 7, 6, 8]

        for mul in multipliers:
            inter_res = bitboard & (bitboard >> mul)
            if inter_res & (inter_res >> (2 * mul)) != 0:
                return True
        return False

    def check_draw(self, bitboards):
        if (bitboards[0] | bitboards[1]) == self._full_grid:
            return True
        return False

    def check_terminal_situations(self, grid, player_number):
        opponent_number = player_number % 2 + 1
        bitboards = self.convert_to_bitboard(grid)

        if self.check_win(bitboards, player_number):
            return math.inf

        if self.check_win(bitboards, opponent_number):
            return -math.inf

        if self.check_draw(bitboards):
            return 0

        return None
