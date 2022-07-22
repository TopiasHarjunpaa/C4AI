import unittest
from services.board_service import BoardService
from entities.sprites import Sprites

GRID_VE1 = [[0,1,0,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,1,0,2,0,0,0],
            [0,2,0,2,0,0,0],
            [0,1,2,2,0,0,0]]

GRID_HO1 = [[0,2,0,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,1,0,1,0,0,0],
            [0,1,0,2,0,0,0],
            [0,2,2,2,2,0,0],
            [0,1,2,2,1,1,1]]

GRID_UD1 = [[0,2,0,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,1,0,1,0,2,1],
            [0,1,0,2,2,0,2],
            [0,2,2,2,1,1,2],
            [0,1,2,2,1,1,1]]

GRID_DD1 = [[0,2,0,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,1,0,1,0,0,0],
            [0,1,0,2,1,0,2],
            [0,2,2,2,1,1,2],
            [0,1,2,2,1,1,1]]

class TestBoardService(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.board = BoardService(self.width, self.height)
        self.sprites = Sprites(self, self.width, self.height)

    def test_add_token_updates_grid_correctly(self):
        self.board.add_token(0, 1)
        self.board.add_token(0, 2)
        self.board.add_token(0, 1)
        self.assertEqual(self.board.grid[5][0], 1)
        self.assertEqual(self.board.grid[4][0], 2)
        self.assertEqual(self.board.grid[3][0], 1)
        self.assertEqual(self.board.grid[2][0], 0)

    def test_add_token_returns_boolean_correctly(self):
        for i in range(6):
            self.assertTrue(self.board.add_token(0, 1))
        self.assertFalse(self.board.add_token(0, 1))
        self.assertTrue(self.board.add_token(4, 1))
        self.assertTrue(self.board.add_token(6, 1))

    def test_add_token_creates_sprites_correctly(self):
        self.assertEqual(len(self.board.sprites.all_sprites), 42)
        self.board.add_token(0, 1)
        self.board.add_token(1, 2)
        self.board.add_token(2, 1)
        self.assertEqual(len(self.board.sprites.all_sprites), 45)
        for i in range(10):
            self.board.add_token(0, 1)
        self.assertEqual(len(self.board.sprites.all_sprites), 50)
    
    def test_check_win_finds_vertical_win(self):
        self.assertFalse(self.board.check_win(1))
        self.assertFalse(self.board.check_win(2))
        self.board.grid = GRID_VE1
        self.assertFalse(self.board.check_win(2))
        self.assertTrue(self.board.check_win(1))
    
    def test_check_win_finds_horizontal_win(self):
        self.assertFalse(self.board.check_win(1))
        self.assertFalse(self.board.check_win(2))
        self.board.grid = GRID_HO1
        self.assertFalse(self.board.check_win(1))
        self.assertTrue(self.board.check_win(2))
    
    def test_check_win_finds_up_diagonal_win(self):
        self.assertFalse(self.board.check_win(1))
        self.assertFalse(self.board.check_win(2))
        self.board.grid = GRID_UD1
        self.assertFalse(self.board.check_win(1))
        self.assertTrue(self.board.check_win(2))

    def test_check_win_finds_down_diagonal_win(self):
        self.assertFalse(self.board.check_win(1))
        self.assertFalse(self.board.check_win(2))
        self.board.grid = GRID_DD1
        self.assertFalse(self.board.check_win(2))
        self.assertTrue(self.board.check_win(1))