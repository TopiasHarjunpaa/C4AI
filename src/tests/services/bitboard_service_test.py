import unittest
from services.bitboard_service import BitboardService
from tests.test_grids import G_1W1, G_AE1, G_DD1, G_SF1, G_WO1, G_UD1, G_HO1, G_VE1

class TestBitboardService(unittest.TestCase):
    def setUp(self):
        self.bb = BitboardService()

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