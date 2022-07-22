from os import sys
import pygame
from ui.menu_view import MenuView
from services.board_service import BoardService
from services.game_service import GameService


class UI:
    """A class to represent main UI which handles every view.
    """

    def __init__(self, renderer, event_queue, clock):
        """Constructs all the necessary attributes for UI.

        Args:
            renderer (Renderer): Renderer object.
            event_queue (EventQueueService: Event and queue service object.
            clock (Clock): Clock object.
        """

        self._renderer = renderer
        self.event_queue = event_queue
        self._clock = clock
        self._menu_view_is_open = False
        self._board = BoardService(renderer.width, renderer.height)
        self._game = GameService(
            self, self._board, renderer, event_queue, clock)

    def start_menu(self):
        """Starts main menu. Is used to launch the game.
        """

        self._show_menu_view()

    def _show_menu_view(self):
        """Shows the menu view.
        Waits for key and forwards to the next view:
        n = new game view
        s = game setup view
        """

        self._menu_view_is_open = True
        MenuView(self._renderer).show()
        key = self._wait_and_check_accepted_keys(
            [pygame.K_n, pygame.K_s])
        self._menu_view_is_open = False
        if key == pygame.K_n:
            self._game.start_gameloop()
        if key == pygame.K_s:
            pass
            # self._show_setup_view()

    def _show_setup_view(self):
        """Shows the game setup view.
        """

        pass

    def show_game_over_view(self):
        """Shows the game over view
        """

        pass

    def quit(self):
        """Quits the game.
        """

        pygame.quit()
        sys.exit()

    def _wait_and_check_accepted_keys(self, keys: list, event_type=pygame.KEYUP):
        """Waits and checks accepted keys.
        Check escape and quit keys:
        1. QUIT = game ends
        2. ESC = returns to menu and game ends if menu view is open
        Waits for accepted keys. When proper key is found:
        1. Save the key
        2. Stop wait loop

        Args:
            keys (list): List of accepted keys
            event_type ((pygame.event), optional): Defaults to pygame.KEYUP.

        Returns:
            int: Returns ascii number of pressed key.
        """

        input_key = None
        waiting = True
        while waiting:
            self._clock.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        waiting = False
                        if self._menu_view_is_open:
                            self.quit()
                        self._show_menu_view()
                if event.type == event_type:
                    if event.key in keys:
                        input_key = event.key
                        waiting = False
        return input_key
