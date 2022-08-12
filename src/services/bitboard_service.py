from config import ROWS, COLUMNS, FULL_GRID, MID_COL
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
            return 22 - self.count_coins(bitboard[player_index])

        if self.check_win(bitboard[opponent_index]):
            return -22 + self.count_coins(bitboard[opponent_index])

        if self.check_draw(bitboard):
            return 0

        return None

    def count_coins(self, player_bitboard):
        coins = bin(player_bitboard).count('1')
        return coins

    def calculate_heuristic_value(self, position, player_index):
        #player_bitboard = position.get_bitboard()[player_index]
        #middle_coins = bin(player_bitboard & MID_COL).count('1')
        #return middle_coins

        #points = 0
        #current_board = position.get_bitboard()[player_index]
        #for col in position.get_available_columns():
        #    new_board = current_board ^ (1 << position.get_heights()[col])
        #    if self.check_win(new_board):
        #        points += 1
        #return points

        return 0
