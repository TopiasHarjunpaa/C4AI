import unittest
import math
from services.heuristic_service import HeuristicService
from services.bitboard_service import BitboardService
from tests.test_grids import G_1W1, G_AE1, G_AE2, G_AE3, G_1W2, G_CG1, G_CG2, G_WO1, G_HO1, G_UD1, G_DD1
from tests.test_locs import L1W, L1T1, L1T2, L1F1, L1F2, L2TW1, L2F1


class TestHeuristicService(unittest.TestCase):
    def setUp(self):
        self.bb = BitboardService()
        self.heuristic = HeuristicService(self.bb)

    def test_count_values_correctly(self):
        value = self.heuristic._count_values(L1W, 1)
        self.assertEqual(value, math.inf)
        value = self.heuristic._count_values(L1W, 2)
        self.assertEqual(value, -math.inf)
        value = self.heuristic._count_values(L1T1, 1)
        self.assertEqual(value, 10)
        value = self.heuristic._count_values(L1T1, 2)
        self.assertEqual(value, -10)
        value = self.heuristic._count_values(L1T2, 1)
        self.assertEqual(value, 10)
        value = self.heuristic._count_values(L1F1, 1)
        self.assertEqual(value, 0)
        value = self.heuristic._count_values(L1F2, 2)
        self.assertEqual(value, 0)
        value = self.heuristic._count_values(L2TW1, 2)
        self.assertEqual(value, 2)
        value = self.heuristic._count_values(L2F1, 2)
        self.assertEqual(value, 0)

    def test_positional_values_returns_correct_value(self):
        value = self.heuristic._get_positional_values(G_AE1, 1)
        self.assertEqual(value, 2)

    def test_get_vertical_values(self):
        value = self.heuristic._get_vertical_values(G_AE1, 1)
        self.assertEqual(value, 0)

    def test_get_inc_diagonal_values(self):
        value = self.heuristic._get_inc_diagonal_values(G_HO1, 1)
        self.assertEqual(value, -6)
        value = self.heuristic._get_inc_diagonal_values(G_HO1, 2)
        self.assertEqual(value, 6)
        value = self.heuristic._get_inc_diagonal_values(G_UD1, 2)
        self.assertEqual(value, math.inf)

    def test_get_dec_diagonal_values(self):
        value = self.heuristic._get_dec_diagonal_values(G_WO1, 1)
        self.assertEqual(value, 0)
        value = self.heuristic._get_dec_diagonal_values(G_WO1, 2)
        self.assertEqual(value, 0)
        value = self.heuristic._get_dec_diagonal_values(G_DD1, 1)
        self.assertEqual(value, math.inf)
        value = self.heuristic._get_dec_diagonal_values(G_1W2, 2)
        self.assertEqual(value, 2)

    def test_heuristic_value_returns_correct_value(self):
        value = self.heuristic.calculate_heuristic_value(G_AE1, 1)
        self.assertEqual(value, 2)
        value = self.heuristic.calculate_heuristic_value(G_AE2, 2)
        self.assertEqual(value, 1)
        value = self.heuristic.calculate_heuristic_value(G_AE3, 2)
        self.assertEqual(value, 2)
    
    def test_heuristic_value_with_bitboards_returns_correct_value(self):
        position = self.bb.convert_to_position(G_AE1)
        value = self.heuristic.calculate_heuristic_value_with_bitboards(position, 0)
        self.assertEqual(value, 1)
        value = self.heuristic.calculate_heuristic_value_with_bitboards(position, 1)
        self.assertEqual(value, 1)
        position = self.bb.convert_to_position(G_CG1)
        value = self.heuristic.calculate_heuristic_value_with_bitboards(position, 0)
        self.assertEqual(value, 0)
        position = self.bb.convert_to_position(G_CG2)
        value = self.heuristic.calculate_heuristic_value_with_bitboards(position, 0)
        self.assertEqual(value, -2)
        value = self.heuristic.calculate_heuristic_value_with_bitboards(position, 1)
        self.assertEqual(value, 5)
        position = self.bb.convert_to_position(G_1W1)
        value = self.heuristic.calculate_heuristic_value_with_bitboards(position, 0)
        self.assertEqual(value, 3)
        value = self.heuristic.calculate_heuristic_value_with_bitboards(position, 1)
        self.assertEqual(value, -1)
