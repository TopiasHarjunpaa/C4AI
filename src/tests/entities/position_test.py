import unittest
from services.bitboard_service import BitboardService
from services.situation_service import SituationService
from services.board_service import BoardService
from tests.test_grids import G_AE1

class TestPosition(unittest.TestCase):
    def setUp(self):
        self.bb = BitboardService()
        self.board = BoardService(640, 480)
        self.situation = SituationService(self.board)
    
    def test_make_move_updates_positions_correctly(self):
        bb_ae1 = self.situation.copy_grid(G_AE1)
        position = self.bb.convert_to_position(G_AE1)
        position.make_move(0, 0)
        bb_ae1[5][0] = 1
        self.assertEqual(self.bb.convert_to_bitboard(bb_ae1), position.bitboard)
        self.assertEqual(self.bb.convert_to_heights(bb_ae1), position.heights)
        position.make_move(1, 1)
        bb_ae1[5][1] = 2
        self.assertEqual(self.bb.convert_to_bitboard(bb_ae1), position.bitboard)
        self.assertEqual(self.bb.convert_to_heights(bb_ae1), position.heights)
        position.make_move(3, 0)
        bb_ae1[3][3] = 1
        self.assertEqual(self.bb.convert_to_bitboard(bb_ae1), position.bitboard)
        self.assertEqual(self.bb.convert_to_heights(bb_ae1), position.heights)
        new_position = self.bb.convert_to_position(bb_ae1)
        new_position.make_move(3, 1)
        bb_ae1[2][3] = 2
        self.assertEqual(self.bb.convert_to_bitboard(bb_ae1), new_position.bitboard)
        self.assertEqual(self.bb.convert_to_heights(bb_ae1), new_position.heights)
        bb_ae1[2][3] = 0
        self.assertEqual(self.bb.convert_to_bitboard(bb_ae1), position.bitboard)