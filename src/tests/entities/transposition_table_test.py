import unittest
from entities.transposition_table import TranspositionTable

class TestTranspositionTable(unittest.TestCase):
    def setUp(self):
        self.tt = TranspositionTable()
        self.boards = [[0,0], [15, 10], [100, 0], [127, 351]]
        self.values = [0, 10, 20, -5]
        self.depths = [5, 6, 7, 10]
        self.cols = [0, 1, 2, 6]
        self.maxes = [True, True, False, False]
        for i in range(4):
            self.tt.add(self.boards[i], self.values[i], self.depths[i], self.cols[i], self.maxes[i])
    
    def test_add(self):
        self.assertEqual(len(self.tt._t_table), 4)
    
    def check_match_returns_none_if_too_low_depth_or_wrong_player(self):
        for i in range(4):
            result = self.tt.check_match(self.boards[i], 7, True)
            self.assertEqual(result, None)
        result = self.tt.check_match(self.boards[3], 1, False)
        self.assertEqual(result, None)

    def check_match_finds_key_correctly(self):
        result = self.tt.check_match(self.boards[0], 1, True)
        self.assertEqual(result, (0, 0))
        result = self.tt.check_match(self.boards[2], 1, False)
        self.assertEqual(result, (20, 2))
        result = self.tt.check_match([10, 15], 0, False)
        self.assertEqual(result, None)
        result = self.tt.check_match([10, 15], 0, True)
        self.assertEqual(result, None)
        result = self.tt.check_match(None, 0, True)
        self.assertEqual(result, None)

