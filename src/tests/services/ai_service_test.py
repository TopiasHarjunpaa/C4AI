import unittest
from services.ai_service import AiService
from services.board_service import BoardService


class TestAiService(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.board = BoardService(self.width, self.height)
        self.ai = AiService(self.board)

    def test_nothing(self):
        pass
