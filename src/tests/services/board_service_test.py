import unittest
from services.board_service import BoardService
from tests.test_grids import G_VE1, G_HO1, G_UD1, G_DD1, G_SF1

class TestBoardService(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.board = BoardService(self.width, self.height)

    def test_after_reset_there_are_only_grid_sprites(self):
        self.board.add_coin(0, 1)
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

    def test_column_available_return_correct_column_number(self):
        col_number = self.board.check_column_available(0)
        self.assertEqual(col_number, 5)
        self.board.grid = G_SF1
        col_number = self.board.check_column_available(0)
        self.assertEqual(col_number, 5)
        col_number = self.board.check_column_available(1)
        self.assertEqual(col_number, -1)
        col_number = self.board.check_column_available(4)
        self.assertEqual(col_number, 1)

    def test_get_available_columns_returns_all_available_columns(self):
        available_columns = self.board.get_available_columns()
        self.assertEqual(available_columns, [0,1,2,3,4,5,6])
        self.board.grid = G_SF1
        available_columns = self.board.get_available_columns()
        self.assertEqual(available_columns, [0,3,4])
        self.board.grid = G_DD1
        available_columns = self.board.get_available_columns()
        self.assertEqual(available_columns, [0,2,3,4,5,6])

    def test_add_coin_updates_grid_correctly(self):
        self.board.add_coin(0, 1)
        self.board.add_coin(0, 2)
        self.board.add_coin(0, 1)
        self.assertEqual(self.board.grid[5][0], 1)
        self.assertEqual(self.board.grid[4][0], 2)
        self.assertEqual(self.board.grid[3][0], 1)
        self.assertEqual(self.board.grid[2][0], 0)

    def test_add_coin_returns_boolean_correctly(self):
        for i in range(6):
            self.assertTrue(self.board.add_coin(0, 1))
        self.assertFalse(self.board.add_coin(0, 1))
        self.assertTrue(self.board.add_coin(4, 1))
        self.assertTrue(self.board.add_coin(6, 1))

    def test_add_coin_creates_sprites_correctly(self):
        self.assertEqual(len(self.board.sprites.all_sprites), 42)
        self.board.add_coin(0, 1)
        self.board.add_coin(1, 2)
        self.board.add_coin(2, 1)
        self.assertEqual(len(self.board.sprites.all_sprites), 45)
        for i in range(10):
            self.board.add_coin(0, 1)
        self.assertEqual(len(self.board.sprites.all_sprites), 50)

    def test_check_win_finds_vertical_win(self):
        self.assertFalse(self.board.check_win(1))
        self.assertFalse(self.board.check_win(2))
        self.board.grid = G_VE1
        self.assertFalse(self.board.check_win(2))
        self.assertTrue(self.board.check_win(1))

    def test_check_win_finds_horizontal_win(self):
        self.assertFalse(self.board.check_win(1))
        self.assertFalse(self.board.check_win(2))
        self.board.grid = G_HO1
        self.assertFalse(self.board.check_win(1))
        self.assertTrue(self.board.check_win(2))

    def test_check_win_finds_up_diagonal_win(self):
        self.assertFalse(self.board.check_win(1))
        self.assertFalse(self.board.check_win(2))
        self.board.grid = G_UD1
        self.assertFalse(self.board.check_win(1))
        self.assertTrue(self.board.check_win(2))

    def test_check_win_finds_down_diagonal_win(self):
        self.board.grid = G_SF1
        self.assertFalse(self.board.check_win(1))
        self.assertFalse(self.board.check_win(2))
        self.board.grid = G_DD1
        self.assertFalse(self.board.check_win(2))
        self.assertTrue(self.board.check_win(1))
