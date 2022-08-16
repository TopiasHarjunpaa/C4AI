from config import ROWS, COLUMNS, FULL_GRID, MID_COL, BORDERS
from entities.position import Position


class BitboardService:
    """A class to represent Bitboard services"""

    def __init__(self):
        pass

    def convert_to_position(self, grid):
        bitboard = self.convert_to_bitboard(grid)
        heights = self.convert_to_heights(grid)
        return Position(bitboard, heights)

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

    def convert_to_heights(self, grid):
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
        multipliers = [1, 7, 6, 8]

        for mul in multipliers:
            inter_res = player_bitboard & (player_bitboard >> mul)
            if inter_res & (inter_res >> (2 * mul)) != 0:
                return True
        return False

    def check_draw(self, bitboard):
        if (bitboard[0] | bitboard[1]) == FULL_GRID:
            return True
        return False

    def check_terminal_node(self, position, player_index):
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
        coins = bin(player_bitboard).count('1')
        return coins

    def calculate_heuristic_value(self, position, player_index):
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

    def get_available_non_losing_columns(self, position, player_index):
        cols = []
        available_cols = position.get_available_columns()
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
