import unittest
import math
from services.ai_service import AiService
from services.board_service import BoardService
from services.situation_service import SituationService
from tests.test_grids import (G_AE1, G_AE2, G_AE3, G_AE4, G_1W1, 
                                G_1W2, G_WO1, G_SF1, G_SF2)


class TestAiService(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.board = BoardService(self.width, self.height)
        self.situation = SituationService(self.board)
        self.ai = AiService(self.situation)

    def test_positional_values_returns_correct_value(self):
        value = self.ai.get_positional_values(G_AE1, 1)
        self.assertEqual(value, 2)

    def test_get_vertical_values(self):
        value = self.ai.get_vertical_values(G_AE1, 1)
        self.assertEqual(value, 0)

    def test_heuristic_value_returns_correct_value(self):
        value = self.ai.heuristic_value(G_AE1, 1)
        self.assertEqual(value, 2)
        value = self.ai.heuristic_value(G_AE2, 2)
        self.assertEqual(value, 1)
        value = self.ai.heuristic_value(G_AE3, 2)
        self.assertEqual(value, 2)

    def test_minimax_finds_terminal_situations(self):
        value = self.ai.minimax(G_1W1, 2, 4, True)[0]
        self.assertEqual(value, -math.inf)
        value, location = self.ai.minimax(G_1W2, 1, 4, True)
        self.assertEqual(value, math.inf)
        self.assertEqual(location, (5, 1))
        value, location = self.ai.minimax(G_WO1, 1, 4, True)
        self.assertEqual(value, 0)
        self.assertEqual(location, None)
        value, location = self.ai.minimax(G_WO1, 2, 4, True)
        self.assertEqual(value, 0)
        self.assertEqual(location, None)
        value, location = self.ai.minimax(G_SF1, 1, 7, True)
        self.assertEqual(value, -math.inf)
        value, location = self.ai.minimax(G_SF2, 2, 6, True)
        self.assertEqual(value, math.inf)
        self.assertEqual(location, (1, 4))

    def test_minimax_returns_best_move(self):
        value, location = self.ai.minimax(G_AE4, 2, 5, True)
        #self.assertEqual(value, 2)
        #self.assertEqual(location, (5, 3))      
