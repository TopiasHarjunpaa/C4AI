import unittest
import math
from services.ai_service import AiService
from services.board_service import BoardService
from services.situation_service import SituationService
from config import ROWS, COLUMNS
from tests.test_grids import (G_AE1, G_AE2, G_AE3, G_AE4, G_1W1,
                              G_1W2, G_WO1, G_SF1, G_SF2, G_VE1)


class TestAiService(unittest.TestCase):
    def setUp(self):
        self.board = BoardService(640, 480)
        self.situation = SituationService(self.board)
        self.ai = AiService(self.situation)

    def test_sort_column_order_sorts_scores_in_descending_order(self):
        order = [(0, 5), (10, 1), (-5, 2)]
        res = [1, 5, 2]
        sorted_order = self.ai.sort_column_order(order)
        self.assertEqual(sorted_order, res)

    def test_sort_column_order_sorts_columns_secondary_ranked_by_middle(self):
        order = [(0, 5), (0, 3), (-5, 2), (100, 4)]
        res = [4, 3, 5, 2]
        sorted_order = self.ai.sort_column_order(order)
        self.assertEqual(sorted_order, res)
        order = [(0, 6), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0)]
        res = [3, 2, 4, 1, 5, 0, 6]
        sorted_order = self.ai.sort_column_order(order)
        self.assertEqual(sorted_order, res)
        order = [(-5, 6), (-50, 5)]
        res = [6, 5]
        sorted_order = self.ai.sort_column_order(order)
        self.assertEqual(sorted_order, res)
        order = [(0, 0)]
        res = [0]
        sorted_order = self.ai.sort_column_order(order)
        self.assertEqual(sorted_order, res)

    def test_calculate_next_move_basic_returns_correct_choice(self):
        location = self.ai.calculate_next_move_basic(G_AE1, 1)
        self.assertEqual(location, (5, 2))
        location = self.ai.calculate_next_move_basic(G_AE4, 2)
        self.assertEqual(location, (5, 3))
        location = self.ai.calculate_next_move_basic(G_SF2, 1)
        self.assertEqual(location, (1, 4))
        location = self.ai.calculate_next_move_basic(G_1W1, 2)
        self.assertEqual(location, (4, 2))

    def test_minimax_finds_terminal_situations(self):
        value = self.ai._minimax(G_1W1, 2, 4, True)[0]
        self.assertEqual(value, -math.inf)
        value, location = self.ai._minimax(G_1W2, 1, 4, True)
        self.assertEqual(value, math.inf)
        self.assertEqual(location, (5, 1))
        value, location = self.ai._minimax(G_WO1, 1, 4, True)
        self.assertEqual(value, 0)
        self.assertEqual(location, None)
        value, location = self.ai._minimax(G_WO1, 2, 4, True)
        self.assertEqual(value, 0)
        self.assertEqual(location, None)
        value = self.ai._minimax(G_SF1, 1, 7, True)[0]
        self.assertEqual(value, -math.inf)

    def test_minimax_returns_best_move(self):
        value, location = self.ai._minimax(G_SF2, 2, 6, True)
        self.assertEqual(value, math.inf)
        self.assertEqual(location, (1, 4))

    def test_calculate_next_move_minimax_returns_valid_location(self):
        result = self.ai.calculate_next_move_minimax(G_AE2, 1, 3)
        self.assertEqual(result, (5, 3))
        result = self.ai.calculate_next_move_minimax(G_WO1, 1, 3)
        self.assertEqual(result, None)

    def test_calculate_next_move_iterative_minimax_returns_valid_column(self):
        result = self.ai.calculate_next_move_iterative_minimax(G_AE3, 1, 0.5)
        self.assertEqual(result, 3)
        result = self.ai.calculate_next_move_iterative_minimax(G_WO1, 1, 0.5)
        self.assertEqual(result, None)
