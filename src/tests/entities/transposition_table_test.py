import unittest
from entities.transposition_table import TranspositionTable


class TestTranspositionTable(unittest.TestCase):
    def setUp(self):
        self.tt = TranspositionTable()
        self.boards = [[0, 0], [15, 10], [100, 0], [127, 351]]
        self.values = [0, 10, 20, -5]
        self.cols = [0, 1, 2, 6]
        for i in range(4):
            self.tt.add(self.boards[i], self.values[i], self.cols[i])

    def test_add(self):
        self.assertEqual(len(self.tt._t_table), 4)

    def test_check_match_finds_key_correctly(self):
        for i in range(len(self.boards)):
            result = self.tt.check_match(self.boards[i])
            self.assertEqual(result, [self.values[i], self.cols[i]])
        result = self.tt.check_match([10, 15])
        self.assertEqual(result, None)
        result = self.tt.check_match([0, 100])
        self.assertEqual(result, None)
