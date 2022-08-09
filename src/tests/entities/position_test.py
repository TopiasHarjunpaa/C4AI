import unittest
from services.bitboard_service import BitboardService
from services.situation_service import SituationService
from services.board_service import BoardService
from entities.position import Position
from tests.test_grids import G_1W1, G_AE1, G_DD1, G_SF1, G_WO1, G_UD1, G_HO1, G_VE1

class TestPosition(unittest.TestCase):
    def setUp(self):
        self.bb = BitboardService()
        self.board = BoardService(640, 480)
        self.situation = SituationService(self.board)
        self.position = Position()
    
    def test_make_move_updates_positions_correctly(self):
        bb_ae1 = self.situation.copy_grid(G_AE1)
        locations = self.situation.get_available_locations(bb_ae1)
        self.position.bitboard = self.bb.convert_to_bitboard(bb_ae1)
        self.position.heights = self.bb.convert_to_heights(locations)
        self.position.counter = self.bb.convert_to_counter(bb_ae1)
        self.assertEqual(self.position.counter, 2)
        self.position.make_move(0)
        self.assertEqual(self.position.counter, 3)
        bb_ae1[5][0] = 1
        self.assertEqual(self.bb.convert_to_bitboard(bb_ae1), self.position.bitboard)
        self.position.make_move(1)
        self.assertEqual(self.position.counter, 4)
        bb_ae1[5][1] = 2
        self.assertEqual(self.bb.convert_to_bitboard(bb_ae1), self.position.bitboard)
        self.position.make_move(3)
        self.assertEqual(self.position.counter, 5)
        bb_ae1[3][3] = 1
        self.assertEqual(self.bb.convert_to_bitboard(bb_ae1), self.position.bitboard)
        
        board, heights, counter, moves = self.position.get_params()
        new_position = Position(board, heights, counter, moves)
        new_position.make_move(3)
        bb_ae1[2][3] = 2
        self.assertEqual(self.bb.convert_to_bitboard(bb_ae1), new_position.bitboard)
        bb_ae1[2][3] = 0
        self.assertEqual(self.bb.convert_to_bitboard(bb_ae1), self.position.bitboard)