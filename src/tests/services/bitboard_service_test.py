import unittest
from services.bitboard_service import BitboardService
from services.situation_service import SituationService
from services.board_service import BoardService
from tests.test_grids import G_1W1, G_AE1, G_DD1, G_SF1, G_WO1, G_UD1, G_HO1, G_VE1

class TestBitboardService(unittest.TestCase):
    def setUp(self):
        self.bb = BitboardService()
        self.board = BoardService(640, 480)
        self.situation = SituationService(self.board)

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
        self.assertFalse(self.bb.check_win(bb, 1))
        self.assertFalse(self.bb.check_win(bb, 2))
        bb = self.bb.convert_to_bitboard(G_DD1)
        self.assertFalse(self.bb.check_win(bb, 2))
        self.assertTrue(self.bb.check_win(bb, 1))
        bb = self.bb.convert_to_bitboard(G_WO1)
        self.assertFalse(self.bb.check_win(bb, 1))
        self.assertFalse(self.bb.check_win(bb, 2))
        bb = self.bb.convert_to_bitboard(G_UD1)
        self.assertFalse(self.bb.check_win(bb, 1))
        self.assertTrue(self.bb.check_win(bb, 2))
        bb = self.bb.convert_to_bitboard(G_HO1)
        self.assertFalse(self.bb.check_win(bb, 1))
        self.assertTrue(self.bb.check_win(bb, 2))
        bb = self.bb.convert_to_bitboard(G_VE1)
        self.assertFalse(self.bb.check_win(bb, 2))
        self.assertTrue(self.bb.check_win(bb, 1))
    
    def test_make_move_updates_bitboard_correctly(self):
        matrix = self.situation.copy_grid(G_AE1)
        start_bb = self.bb.convert_to_bitboard(G_AE1)       
        updated_bb = self.bb.make_move(start_bb, (5, 0), 1)
        matrix[5][0] = 1
        self.assertEqual(self.bb.convert_to_bitboard(matrix), updated_bb)
        updated_bb = self.bb.make_move(updated_bb, (5, 1), 2)
        matrix[5][1] = 2
        self.assertEqual(self.bb.convert_to_bitboard(matrix), updated_bb)
        updated_bb = self.bb.make_move(updated_bb, (3, 3), 1)
        matrix[3][3] = 1
        self.assertEqual(self.bb.convert_to_bitboard(matrix), updated_bb)