import unittest
from services.bitboard_service import BitboardService
from tests.test_grids import G_1W1, G_AE1, G_VE1, G_HO1, G_UD1, G_DD1, G_SF1, G_WO1, G_SF2,G_AE2


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