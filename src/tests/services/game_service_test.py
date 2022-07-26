import unittest
import pygame
from services.game_service import GameService
from services.board_service import BoardService
from tests.test_grids import G_WO1


class StubClock:
    def tick(self):
        pass


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def __init__(self):
        self.width = 640
        self.height = 480

    def render_game(self, board, player_number, game_ended, draw):
        pass


class StubUI:
    def __init__(self):
        pass

    def start_menu(self):
        pass

    def quit(self):
        pass

    def show_game_ended_view(self, player_number):
        pass


class TestGameService(unittest.TestCase):
    def setUp(self):
        self.board = BoardService(640, 480)
        self.menu = StubUI()

    def test_player_one_wins(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_1),
                  StubEvent(pygame.KEYDOWN, pygame.K_2),
                  StubEvent(pygame.KEYDOWN, pygame.K_1),
                  StubEvent(pygame.KEYDOWN, pygame.K_2),
                  StubEvent(pygame.KEYDOWN, pygame.K_1),
                  StubEvent(pygame.KEYDOWN, pygame.K_2),
                  StubEvent(pygame.KEYDOWN, pygame.K_1), ]

        gameloop = GameService(
            self.menu,
            self.board,
            StubRenderer(),
            StubEventQueue(events),
            StubClock()
        )

        gameloop._player_setup = {1: 1, 2: 1}
        gameloop.start_gameloop()
        setup = gameloop.get_player_setup()
        self.assertEqual(setup, ("Player", "Player"))
        self.assertFalse(gameloop.playing)
        self.assertEqual(gameloop.player_number, 1)

    def test_player_two_wins(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_5),
                  StubEvent(pygame.KEYDOWN, pygame.K_2),
                  StubEvent(pygame.KEYDOWN, pygame.K_1),
                  StubEvent(pygame.KEYDOWN, pygame.K_2),
                  StubEvent(pygame.KEYDOWN, pygame.K_1),
                  StubEvent(pygame.KEYDOWN, pygame.K_2),
                  StubEvent(pygame.KEYDOWN, pygame.K_1),
                  StubEvent(pygame.KEYDOWN, pygame.K_2), ]

        gameloop = GameService(
            self.menu,
            self.board,
            StubRenderer(),
            StubEventQueue(events),
            StubClock()
        )

        gameloop._player_setup = {1: 1, 2: 1}
        gameloop.start_gameloop()
        setup = gameloop.get_player_setup()
        self.assertEqual(setup, ("Player", "Player"))
        self.assertFalse(gameloop.playing)
        self.assertEqual(gameloop.player_number, 2)

    def test_returns_correct_player_setup(self):
        events = [StubEvent(None, None), ]

        gameloop = GameService(
            self.menu,
            self.board,
            StubRenderer(),
            StubEventQueue(events),
            StubClock()
        )

        gameloop._player_setup = {1: 1, 2: 1}
        setup = gameloop.get_player_setup()
        self.assertEqual(setup, ("Player", "Player"))
        gameloop._player_setup = {1: 3, 2: 1}
        setup = gameloop.get_player_setup()
        self.assertEqual(setup, ("AI (Minimax depth 7)", "Player"))
        gameloop._player_setup = {1: 1, 2: 4}
        setup = gameloop.get_player_setup()
        self.assertEqual(setup, ("Player", "AI (Minimax opt.)"))

    def test_escape_key_ends_loop(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_ESCAPE),
                    StubEvent(pygame.KEYDOWN, pygame.K_ESCAPE), ]

        gameloop = GameService(
            self.menu,
            self.board,
            StubRenderer(),
            StubEventQueue(events),
            StubClock()
        )

        gameloop._player_setup = {1: 1, 2: 1}
        gameloop.start_gameloop()
        self.assertFalse(gameloop.playing)

    def test_draw_ends_game_loop(self):
        events = [StubEvent(None, None), ]

        gameloop = GameService(
            self.menu,
            self.board,
            StubRenderer(),
            StubEventQueue(events),
            StubClock()
        )

        gameloop._player_setup = {1: 1, 2: 1}
        self.board.grid = G_WO1
        gameloop._check_terminal_situation()
        self.assertFalse(gameloop.playing)

    def test_player_setup_changes_correctly(self):
        events = [StubEvent(None, None), ]

        gameloop = GameService(
            self.menu,
            self.board,
            StubRenderer(),
            StubEventQueue(events),
            StubClock()
        )

        gameloop._player_setup = {1: 1, 2: 1}
        setup = gameloop.get_player_setup()
        self.assertEqual(setup, ("Player", "Player"))
        gameloop.change_player_setup(2)
        gameloop.change_player_setup(2)
        setup = gameloop.get_player_setup()
        self.assertEqual(setup, ("Player", "AI (Minimax depth 7)"))
        gameloop.change_player_setup(2)
        setup = gameloop.get_player_setup()
        self.assertEqual(setup, ("Player", "AI (Minimax opt.)"))
        gameloop.change_player_setup(1)
        setup = gameloop.get_player_setup()
        self.assertEqual(setup, ("AI (basic)", "AI (Minimax opt.)"))

