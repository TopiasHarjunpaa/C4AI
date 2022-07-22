import unittest
from services.board_service import BoardService
from entities.sprites import Sprites


class TestBoardService(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.level = BoardService(self.width, self.height)
        self.sprites = Sprites(self, self.width, self.height)

    def test_add_token_updates_grid_correctly(self):
        self.level.add_token(0, 1)
        self.level.add_token(0, 2)
        self.level.add_token(0, 1)
        self.assertEqual(self.level.grid[5][0], 1)
        self.assertEqual(self.level.grid[4][0], 2)
        self.assertEqual(self.level.grid[3][0], 1)
        self.assertEqual(self.level.grid[2][0], 0)