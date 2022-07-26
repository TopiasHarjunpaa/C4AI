import unittest
from services.bitboard_service import BitboardService
from services.situation_service import SituationService
from services.board_service import BoardService
from tests.test_grids import G_1W1, G_1W2, G_1W3, G_AE1, G_CG1, G_CG2, G_DD1, G_MG1, G_MG2, G_SF1, G_SF2, G_SF3, G_SG1, G_SG2, G_WO1, G_UD1, G_HO1, G_VE1


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
        self.assertFalse(self.bb.check_win(bb[0]))
        self.assertFalse(self.bb.check_win(bb[1]))
        bb = self.bb.convert_to_bitboard(G_DD1)
        self.assertFalse(self.bb.check_win(bb[1]))
        self.assertTrue(self.bb.check_win(bb[0]))
        bb = self.bb.convert_to_bitboard(G_WO1)
        self.assertFalse(self.bb.check_win(bb[0]))
        self.assertFalse(self.bb.check_win(bb[1]))
        bb = self.bb.convert_to_bitboard(G_UD1)
        self.assertFalse(self.bb.check_win(bb[0]))
        self.assertTrue(self.bb.check_win(bb[1]))
        bb = self.bb.convert_to_bitboard(G_HO1)
        self.assertFalse(self.bb.check_win(bb[0]))
        self.assertTrue(self.bb.check_win(bb[1]))
        bb = self.bb.convert_to_bitboard(G_VE1)
        self.assertFalse(self.bb.check_win(bb[1]))
        self.assertTrue(self.bb.check_win(bb[0]))

    def test_check_terminal_node_finds_terminal_situations(self):
        position = self.bb.convert_to_position(G_VE1)
        result = self.bb.check_terminal_node(position, 0)
        self.assertEqual(result, 17000)
        result = self.bb.check_terminal_node(position, 1)
        self.assertEqual(result, -17000)
        position = self.bb.convert_to_position(G_WO1)
        result = self.bb.check_terminal_node(position, 0)
        self.assertEqual(result, 0)
        result = self.bb.check_terminal_node(position, 1)
        self.assertEqual(result, 0)
        position = self.bb.convert_to_position(G_HO1)
        result = self.bb.check_terminal_node(position, 0)
        self.assertEqual(result, -14000)
        result = self.bb.check_terminal_node(position, 1)
        self.assertEqual(result, 14000)
        position = self.bb.convert_to_position(G_MG1)
        result = self.bb.check_terminal_node(position, 0)
        self.assertEqual(result, None)
        result = self.bb.check_terminal_node(position, 1)
        self.assertEqual(result, None)

    def test_check_three_connect(self):
        position = self.bb.convert_to_position(G_1W1)
        bitboard = position.get_bitboard()
        result = self.bb.check_three_connect(bitboard[0], bitboard[1])
        self.assertEqual(result, 2)
        position = self.bb.convert_to_position(G_1W2)
        bitboard = position.get_bitboard()
        result = self.bb.check_three_connect(bitboard[0], bitboard[1])
        self.assertEqual(result, 1)
        position = self.bb.convert_to_position(G_1W3)
        bitboard = position.get_bitboard()
        result = self.bb.check_three_connect(bitboard[0], bitboard[1])
        self.assertEqual(result, 1)
        result = self.bb.check_three_connect(bitboard[1], bitboard[0])
        self.assertEqual(result, 0)
        position = self.bb.convert_to_position(G_SF2)
        bitboard = position.get_bitboard()
        result = self.bb.check_three_connect(bitboard[0], bitboard[1])
        self.assertEqual(result, 2)
        position = self.bb.convert_to_position(G_SF3)
        bitboard = position.get_bitboard()
        result = self.bb.check_three_connect(bitboard[1], bitboard[0])
        self.assertEqual(result, 2)
        position = self.bb.convert_to_position(G_CG1)
        bitboard = position.get_bitboard()
        result = self.bb.check_three_connect(bitboard[0], bitboard[1])
        self.assertEqual(result, 0)
        position = self.bb.convert_to_position(G_CG2)
        bitboard = position.get_bitboard()
        result = self.bb.check_three_connect(bitboard[0], bitboard[1])
        self.assertEqual(result, 1)
        result = self.bb.check_three_connect(bitboard[1], bitboard[0])
        self.assertEqual(result, 3)

    def test_symmetry_check_works_properly(self):
        position = self.bb.convert_to_position(G_MG2)
        bitboard = position.get_bitboard()
        result = self.bb.is_symmetrical(bitboard)
        self.assertFalse(result)
        position = self.bb.convert_to_position(G_AE1)
        bitboard = position.get_bitboard()
        result = self.bb.is_symmetrical(bitboard)
        self.assertTrue(result)
        position = self.bb.convert_to_position(G_SG1)
        bitboard = position.get_bitboard()
        result = self.bb.is_symmetrical(bitboard)
        self.assertTrue(result)
        position = self.bb.convert_to_position(G_SG2)
        bitboard = position.get_bitboard()
        result = self.bb.is_symmetrical(bitboard)
        self.assertTrue(result)
