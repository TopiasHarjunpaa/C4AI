import unittest
from services.board_service import BoardService
from services.situation_service import SituationService
from tests.test_grids import G_VE1, G_HO1, G_UD1, G_DD1, G_SF1, G_WO1, G_SF2,G_AE2


class TestSituationService(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.board = BoardService(self.width, self.height)
        self.situation = SituationService(self.board)

    def test_column_available_return_correct_column_number(self):
        col_number = self.situation.check_column_available(self.board.grid, 0)
        self.assertEqual(col_number, 5)
        col_number = self.situation.check_column_available(G_SF1, 0)
        self.assertEqual(col_number, 5)
        col_number = self.situation.check_column_available(G_SF1, 1)
        self.assertEqual(col_number, -1)
        col_number = self.situation.check_column_available(G_SF1, 4)
        self.assertEqual(col_number, 1)

    def test_get_available_locations_returns_all_available_columns(self):
        available_columns = self.situation.get_available_locations(
            self.board.grid)
        self.assertEqual(available_columns, [
                         (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)])
        available_columns = self.situation.get_available_locations(G_SF1)
        self.assertEqual(available_columns, [(5, 0), (1, 3), (1, 4)])
        available_columns = self.situation.get_available_locations(G_DD1)
        self.assertEqual(available_columns, [
                         (5, 0), (3, 2), (1, 3), (2, 4), (3, 5), (2, 6)])

    def test_get_available_locations_ranked_returns_locations_in_ranked_order(self):
        available_columns = self.situation.get_available_locations_ranked(
            self.board.grid)
        self.assertEqual(available_columns, [
                         (5, 3), (5, 2), (5, 4), (5, 1), (5, 5), (5, 0), (5, 6)])
        available_columns = self.situation.get_available_locations_ranked(G_SF1)
        self.assertEqual(available_columns, [(1, 3), (1, 4), (5, 0)])
        available_columns = self.situation.get_available_locations_ranked(G_WO1)
        self.assertEqual(available_columns, [])

    def test_check_win_finds_vertical_win(self):
        self.assertFalse(self.situation.check_win(self.board.grid, 1))
        self.assertFalse(self.situation.check_win(self.board.grid, 2))
        self.assertFalse(self.situation.check_win(G_VE1, 2))
        self.assertTrue(self.situation.check_win(G_VE1, 1))

    def test_check_win_finds_horizontal_win(self):
        self.assertFalse(self.situation.check_win(self.board.grid, 1))
        self.assertFalse(self.situation.check_win(self.board.grid, 2))
        self.assertFalse(self.situation.check_win(G_HO1, 1))
        self.assertTrue(self.situation.check_win(G_HO1, 2))

    def test_check_win_finds_up_diagonal_win(self):
        self.assertFalse(self.situation.check_win(self.board.grid, 1))
        self.assertFalse(self.situation.check_win(self.board.grid, 2))
        self.assertFalse(self.situation.check_win(G_UD1, 1))
        self.assertTrue(self.situation.check_win(G_UD1, 2))

    def test_check_win_finds_down_diagonal_win(self):
        self.assertFalse(self.situation.check_win(G_SF1, 1))
        self.assertFalse(self.situation.check_win(G_SF1, 2))
        self.assertFalse(self.situation.check_win(G_DD1, 2))
        self.assertTrue(self.situation.check_win(G_DD1, 1))
        self.assertFalse(self.situation.check_win(G_WO1, 1))
        self.assertFalse(self.situation.check_win(G_WO1, 2))

    def test_check_draw(self):
        self.assertFalse(self.situation.check_draw(self.board.grid))
        self.assertFalse(self.situation.check_draw(G_SF1))
        self.assertTrue(self.situation.check_draw(G_WO1))
    
    def test_count_free_slots_counts_correctly(self):
        slots = self.situation.count_free_slots(G_WO1)
        self.assertEqual(slots, 0)
        slots = self.situation.count_free_slots(G_SF2)
        self.assertEqual(slots, 9)
        slots = self.situation.count_free_slots(G_AE2)
        self.assertEqual(slots, 40)
    
    def test_check_win_with_bitboards_finds_win_correctly(self):
        self.assertFalse(self.situation.check_win_bb(G_SF1, 1))
        self.assertFalse(self.situation.check_win_bb(G_SF1, 2))
        self.assertFalse(self.situation.check_win_bb(G_DD1, 2))
        self.assertTrue(self.situation.check_win_bb(G_DD1, 1))
        self.assertFalse(self.situation.check_win_bb(G_WO1, 1))
        self.assertFalse(self.situation.check_win_bb(G_WO1, 2))
        self.assertFalse(self.situation.check_win_bb(self.board.grid, 1))
        self.assertFalse(self.situation.check_win_bb(self.board.grid, 2))
        self.assertFalse(self.situation.check_win_bb(G_UD1, 1))
        self.assertTrue(self.situation.check_win_bb(G_UD1, 2))
        self.assertFalse(self.situation.check_win_bb(G_HO1, 1))
        self.assertTrue(self.situation.check_win_bb(G_HO1, 2))
        self.assertFalse(self.situation.check_win_bb(G_VE1, 2))
        self.assertTrue(self.situation.check_win_bb(G_VE1, 1))