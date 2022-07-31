import unittest
from services.ai_service import AiService
from services.board_service import BoardService
from services.situation_service import SituationService
from tests.test_grids import G_AE1, G_AE2, G_AE3, G_AE4


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
    
    def test_minimax_returns_best_move(self):
        value, location = self.ai.minimax(G_AE4, 2, 5, True)
        #self.assertEqual(value, 2)
        #self.assertEqual(location, (5, 3))      
