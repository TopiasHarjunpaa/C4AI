from config import ROWS, COLUMNS


class BitboardService:
    """A class to represent Bitboard services"""

    def __init__(self):
        pass

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

    def check_win (self, grid, player_number):
        bitboards = self.convert_to_bitboard(grid)
        bitboard = bitboards[player_number - 1]
        multipliers = [1, 7, 6, 8]

        for mul in multipliers:
            inter_res = bitboard & (bitboard >> mul)
            if inter_res & (inter_res >> (2 * mul)) != 0:
                return True
        return False
