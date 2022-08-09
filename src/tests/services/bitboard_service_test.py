import unittest
from services.bitboard_service import BitboardService
from services.situation_service import SituationService
from services.board_service import BoardService
from entities.position import Position
from tests.test_grids import G_1W1, G_AE1, G_DD1, G_SF1, G_WO1, G_UD1, G_HO1, G_VE1

class TestBitboardService(unittest.TestCase):
    def setUp(self):
        self.bb = BitboardService()
        self.board = BoardService(640, 480)
        self.situation = SituationService(self.board)
        self.position = Position()

    def convert_grid_to_position(self, grid):
        new_position = Position()
        locations = self.situation.get_available_locations(grid)
        new_position.bitboard = self.bb.convert_to_bitboard(grid)
        new_position.heights = self.bb.convert_to_heights(locations)
        new_position.counter = self.bb.convert_to_counter(grid)
        return new_position  
    
    def test_check_draw(self):
        bb = self.bb.convert_to_bitboard(G_SF1)
        self.assertFalse(self.bb.check_draw(bb))
        bb = self.bb.convert_to_bitboard(G_1W1)
        self.assertFalse(self.bb.check_draw(bb))
        bb = self.bb.convert_to_bitboard(G_AE1)
        self.assertFalse(self.bb.check_draw(bb))
        bb = self.bb.convert_to_bitboard(G_DD1)
        self.assertFalse(self.bb.check_draw(bb))
        bb = self.bb.convert_to_bitboard(G_WO1)
        self.assertTrue(self.bb.check_draw(bb))

    def test_check_win_with_bitboards_finds_win_correctly(self):
        bb = self.bb.convert_to_bitboard(G_SF1)
        self.assertFalse(self.bb.check_win(bb, 0))
        self.assertFalse(self.bb.check_win(bb, 1))
        bb = self.bb.convert_to_bitboard(G_DD1)
        self.assertFalse(self.bb.check_win(bb, 1))
        self.assertTrue(self.bb.check_win(bb, 0))
        bb = self.bb.convert_to_bitboard(G_WO1)
        self.assertFalse(self.bb.check_win(bb, 0))
        self.assertFalse(self.bb.check_win(bb, 1))
        bb = self.bb.convert_to_bitboard(G_UD1)
        self.assertFalse(self.bb.check_win(bb, 0))
        self.assertTrue(self.bb.check_win(bb, 1))
        bb = self.bb.convert_to_bitboard(G_HO1)
        self.assertFalse(self.bb.check_win(bb, 0))
        self.assertTrue(self.bb.check_win(bb, 1))
        bb = self.bb.convert_to_bitboard(G_VE1)
        self.assertFalse(self.bb.check_win(bb, 1))
        self.assertTrue(self.bb.check_win(bb, 0))
    
    def test_calculate_heuristic_returns_correct_value(self):
        self.assertEqual(self.bb.calculate_heuristic_value(self.position), 0)
        new_pos = self.convert_grid_to_position(G_AE1)
        self.assertEqual(self.bb.calculate_heuristic_value(new_pos), 1)
        new_pos = self.convert_grid_to_position(G_VE1)
        self.assertEqual(self.bb.calculate_heuristic_value(new_pos), 0)
        new_pos.make_move(0)
        self.assertEqual(self.bb.calculate_heuristic_value(new_pos), 3)