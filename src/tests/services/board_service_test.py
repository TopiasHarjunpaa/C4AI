import unittest
from services.board_service import BoardService
from tests.test_grids import G_VE1

class TestBoardService(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.board = BoardService(self.width, self.height)

    def test_after_reset_there_are_only_grid_sprites(self):
        self.board.add_coin(0, 5, 1)
        self.assertEqual(len(self.board.sprites.all_sprites), 43)
        self.board.reset()
        self.assertEqual(len(self.board.sprites.all_sprites), 42)

    def test_after_reset_grid_has_only_zeros(self):
        self.board.grid = G_VE1
        zeros = sum([row.count(0) for row in self.board.grid])
        self.assertEqual(zeros, 32)
        self.board.reset()
        zeros = sum([row.count(0) for row in self.board.grid])
        self.assertEqual(zeros, 42)

    def test_add_coin_updates_grid_correctly(self):
        self.board.add_coin(0, 5, 1)
        self.board.add_coin(0, 4, 2)
        self.board.add_coin(0, 3, 1)
        self.assertEqual(self.board.grid[5][0], 1)
        self.assertEqual(self.board.grid[4][0], 2)
        self.assertEqual(self.board.grid[3][0], 1)
        self.assertEqual(self.board.grid[2][0], 0)

    def test_add_coin_creates_sprites_correctly(self):
        self.assertEqual(len(self.board.sprites.all_sprites), 42)
        self.board.add_coin(0, 5, 1)
        self.board.add_coin(1, 5, 2)
        self.board.add_coin(2, 5, 1)
        self.assertEqual(len(self.board.sprites.all_sprites), 45)
