import unittest
from services.board_service import BoardService
from services.situation_service import SituationService
from tests.test_grids import G_VE1, G_HO1, G_UD1, G_DD1, G_SF1

class TestSituationService(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.board = BoardService(self.width, self.height)
        self.situation = SituationService(self.board)

    def test_column_available_return_correct_column_number(self):
        col_number = self.situation.check_column_available(0)
        self.assertEqual(col_number, 5)
        self.board.grid = G_SF1
        col_number = self.situation.check_column_available(0)
        self.assertEqual(col_number, 5)
        col_number = self.situation.check_column_available(1)
        self.assertEqual(col_number, -1)
        col_number = self.situation.check_column_available(4)
        self.assertEqual(col_number, 1)

    def test_get_available_columns_returns_all_available_columns(self):
        available_columns = self.situation.get_available_columns()
        self.assertEqual(available_columns, [0,1,2,3,4,5,6])
        self.board.grid = G_SF1
        available_columns = self.situation.get_available_columns()
        self.assertEqual(available_columns, [0,3,4])
        self.board.grid = G_DD1
        available_columns = self.situation.get_available_columns()
        self.assertEqual(available_columns, [0,2,3,4,5,6])

    def test_check_win_finds_vertical_win(self):
        self.assertFalse(self.situation.check_win(1))
        self.assertFalse(self.situation.check_win(2))
        self.board.grid = G_VE1
        self.assertFalse(self.situation.check_win(2))
        self.assertTrue(self.situation.check_win(1))

    def test_check_win_finds_horizontal_win(self):
        self.assertFalse(self.situation.check_win(1))
        self.assertFalse(self.situation.check_win(2))
        self.board.grid = G_HO1
        self.assertFalse(self.situation.check_win(1))
        self.assertTrue(self.situation.check_win(2))

    def test_check_win_finds_up_diagonal_win(self):
        self.assertFalse(self.situation.check_win(1))
        self.assertFalse(self.situation.check_win(2))
        self.board.grid = G_UD1
        self.assertFalse(self.situation.check_win(1))
        self.assertTrue(self.situation.check_win(2))

    def test_check_win_finds_down_diagonal_win(self):
        self.board.grid = G_SF1
        self.assertFalse(self.situation.check_win(1))
        self.assertFalse(self.situation.check_win(2))
        self.board.grid = G_DD1
        self.assertFalse(self.situation.check_win(2))
        self.assertTrue(self.situation.check_win(1))