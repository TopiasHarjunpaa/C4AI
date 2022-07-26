import unittest
from services.board_service import BoardService
from entities.sprites import Sprites


class TestSprites(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.board = BoardService(self.width, self.height)
        self.sprites = Sprites(self.board, self.width, self.height)

    def test_init_game_board_creates_game_grid(self):
        self.assertEqual(len(self.sprites.all_sprites), 42)
        self.assertEqual(len(self.sprites.grids), 42)

    def test_draw_new_coin_adds_coins_to_sprite_groups(self):
        self.assertEqual(len(self.sprites.coins), 0)
        self.sprites.draw_new_coin(5, 0, 1)
        self.sprites.draw_new_coin(4, 0, 2)
        self.sprites.draw_new_coin(5, 1, 1)
        self.assertEqual(len(self.sprites.coins), 3)
        self.assertEqual(len(self.sprites.all_sprites), 45)
