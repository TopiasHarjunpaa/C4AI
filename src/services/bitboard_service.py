from config import ROWS, COLUMNS, FULL_GRID, MID_COL


class BitboardService:
    """A class to represent Bitboard services"""

    def __init__(self):
        pass

    def convert_to_bitboard(self, grid):
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

    def convert_to_heights(self, locations):
        heights = []
        for location in locations:
            row = location[0]
            col = location[1]
            height = col * 7 + (5 - row)
            heights.append(height)
        return heights

    def convert_to_counter(self, grid):
        counter = 42
        for row in grid:
            counter -= row.count(0)
        return counter

    def check_win(self, bitboard, index):
        board = bitboard[index]
        multipliers = [1, 7, 6, 8]

        for mul in multipliers:
            inter_res = board & (board >> mul)
            if inter_res & (inter_res >> (2 * mul)) != 0:
                return True
        return False

    def check_draw(self, bitboard):
        if (bitboard[0] | bitboard[1]) == FULL_GRID:
            return True
        return False

    def check_terminal_node(self, position):
        bitboard = position.get_bitboard()
        counter = position.get_counter()
        player_index = counter & 1
        opponent_index = (player_index + 1) % 2

        if self.check_win(bitboard, player_index):
            return 22 - self.count_coins(bitboard, player_index)

        if self.check_win(bitboard, opponent_index):
            return -22 + self.count_coins(bitboard, opponent_index)

        if self.check_draw(bitboard):
            return 0

        return None

    def count_coins(self, bitboard, player_index):
        coins = bin(bitboard[player_index]).count('1')
        return coins

    def calculate_heuristic_value(self, position):
        bitboard = position.get_bitboard()
        counter = position.get_counter()
        middle_coins = bin(bitboard[counter & 1] & MID_COL).count('1')
        return middle_coins
