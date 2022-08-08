import unittest
import math
from services.ai_service import AiService
from services.board_service import BoardService
from services.situation_service import SituationService
from tests.test_grids import (G_AE1, G_AE2, G_AE3, G_AE4, G_1W1,
                              G_1W2, G_WO1, G_SF1, G_SF2, G_VE1)


class TestAiService(unittest.TestCase):
    def setUp(self):
        self.board = BoardService(640, 480)
        self.situation = SituationService(self.board)
        self.ai = AiService(self.situation)

    def copy_grid_allows_changes_without_modifying_original(self):
        original_grid1 = self.board.grid
        original_grid2 = G_AE4
        copy_grid1 = self.ai._copy_grid(original_grid1)
        copy_grid2 = self.ai._copy_grid(original_grid2)
        self.assertEqual(original_grid1, copy_grid1)
        self.assertEqual(original_grid2, copy_grid2)
        copy_grid1[0][0] = 9
        self.assertNotEqual(original_grid1, copy_grid1)
        self.assertNotEqual(original_grid1[0][0], copy_grid1[0][0])
        self.assertEqual(copy_grid1[0][0], 9)
        self.assertEqual(original_grid1[0][0], 0)

    def test_calculate_next_move_basic_returns_correct_choice(self):
        location = self.ai.calculate_next_move_basic(G_AE1, 1)
        self.assertEqual(location, (5, 2))
        location = self.ai.calculate_next_move_basic(G_AE4, 2)
        self.assertEqual(location, (5, 3))
        location = self.ai.calculate_next_move_basic(G_SF2, 1)
        self.assertEqual(location, (1, 4))
        location = self.ai.calculate_next_move_basic(G_1W1, 2)
        self.assertEqual(location, (4, 2))

    def test_heuristic_value_returns_correct_value(self):
        value = self.ai._heuristic_value(G_AE1, 1)
        self.assertEqual(value, 2)
        value = self.ai._heuristic_value(G_AE2, 2)
        self.assertEqual(value, 1)
        value = self.ai._heuristic_value(G_AE3, 2)
        self.assertEqual(value, 2)

    def test_check_terminal_node(self):
        answer = self.ai._check_terminal_node(G_AE1, 1, 2)
        self.assertEqual(answer, None)
        answer = self.ai._check_terminal_node(G_VE1, 1, 2)
        self.assertEqual(answer, math.inf)
        answer = self.ai._check_terminal_node(G_VE1, 2, 1)
        self.assertEqual(answer, -math.inf)
        answer = self.ai._check_terminal_node(G_WO1, 1, 2)
        self.assertEqual(answer, 0)
        answer = self.ai._check_terminal_node(G_WO1, 2, 1)
        self.assertEqual(answer, 0)

    def test_minimax_finds_terminal_situations(self):
        value = self.ai._minimax(G_1W1, 2, 4, True)[0]
        self.assertEqual(value, -math.inf)
        value, location, cols = self.ai._minimax(G_1W2, 1, 4, True)
        self.assertEqual(value, math.inf)
        self.assertEqual(location, (5, 1))
        value, location, cols = self.ai._minimax(G_WO1, 1, 4, True)
        self.assertEqual(value, 0)
        self.assertEqual(location, None)
        self.assertEqual(cols, None)
        value, location, cols = self.ai._minimax(G_WO1, 2, 4, True)
        self.assertEqual(value, 0)
        self.assertEqual(location, None)
        self.assertEqual(cols, None)
        value = self.ai._minimax(G_SF1, 1, 7, True)[0]
        self.assertEqual(value, -math.inf)

    def test_minimax_returns_best_move(self):
        value, location, cols = self.ai._minimax(G_SF2, 2, 6, True)
        self.assertEqual(value, math.inf)
        self.assertEqual(location, (1, 4))      
