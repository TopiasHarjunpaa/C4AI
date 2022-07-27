import unittest
from services.ai_service import AiService
from services.board_service import BoardService
from tests.test_grids import G_AE1


class TestAiService(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.board = BoardService(self.width, self.height)
        self.ai = AiService(self.board)

    def test_positional_values_returns_correct_value(self):
        value = self.ai.get_positional_values(G_AE1, 1)
        self.assertEqual(value, 2)

    def test_get_vertical_values(self):
        value = self.ai.get_vertical_values(G_AE1, 1)
        self.assertEqual(value, 0)

    def test_heurestic_value_returns_correct_value(self):
        value = self.ai.heurestic_value(G_AE1, 1)
        self.assertEqual(value, 2)
